import csv
import os
import random
import re
from collections import defaultdict
from typing import Any, Optional

from tenacity import RetryError
from tqdm.auto import tqdm

from ragelo.evaluators.answer_evaluators.base_answer_evaluator import (
    AnswerEvaluatorFactory,
    BaseAnswerEvaluator,
)
from ragelo.llm_providers.base_llm_provider import BaseLLMProvider
from ragelo.logger import logger
from ragelo.types import (
    AgentAnswer,
    AnswerEvaluatorResult,
    AnswerEvaluatorTypes,
    Document,
    Query,
)
from ragelo.types.configurations import PairwiseEvaluatorConfig


@AnswerEvaluatorFactory.register(AnswerEvaluatorTypes.PAIRWISE_REASONING)
class PairwiseWithReasoningEvaluator(BaseAnswerEvaluator):
    """A evaluator that evaluates RAG-based answers pairwise, with document reasoning"""

    config: PairwiseEvaluatorConfig
    output_columns: list[str] = ["qid", "agent_a", "agent_b", "raw_answer", "answer"]
    output_file: str = "pairwise_answers_evaluations.csv"
    prompt = """
Please act as an impartial judge and evaluate the quality of the responses provided \
by two AI assistants tasked to answer the question displayed below, based on a set \
of documents retrieved by a search engine.
You should choose the assistant that best answers the user question based on a set \
of reference documents that may or not be relevant.
Answers cite documents using square brackets. For each reference document, you will \
be provided with a reasoning explaining why the document is or is not relevant.
Your evaluation should consider factors such as the correctness, helpfulness, \
completeness, accuracy, depth, and level of detail of their responses.\
Details are only useful if they answer the user question. If an answer \
contains non-relevant details, it should not be preferred over one that only \
use relevant information.
Begin your evaluation by explaining why each answer correctly answers the user \
question. Then, you should compare the two responses and provide a short explanation \
on their differences. Avoid any position biases and ensure that the order in which \
the responses were presented does not influence your decision. Do not allow the \
length of the responses to influence your evaluation. Be as objective as possible.
After providing your explanation, output your final verdict by strictly following \
this format: "[[A]]" if assistant A is better, "[[B]]" if assistant B is better, \
and "[[C]]" for a tie.

[User Question]
{query}

[Reference Documents]
{documents}

[The Start of Assistant A's Answer]
{answer_a}
[The End of Assistant A's Answer]

[The Start of Assistant B's Answer]
{answer_b}
[The End of Assistant B's Answer]
""".strip()

    def __init__(
        self,
        config: PairwiseEvaluatorConfig,
        llm_provider: BaseLLMProvider,
    ):
        super().__init__(config, llm_provider)
        self.k = self.config.k
        self.bidirectional = self.config.bidirectional
        self.pattern = re.compile(r"\[\[([^]]+)]].*$(?:(?!\[\[).)*", re.DOTALL)

    def batch_evaluate(self, queries: list[Query]) -> list[AnswerEvaluatorResult]:
        failed_evaluations = 0
        evaluations = [AnswerEvaluatorResult(**x) for x in self._get_existing_output()]
        skip_tuples = {(x.qid, x.agent_a, x.agent_b) for x in evaluations}
        tuples_to_eval = []
        all_tuples = 0
        queries = self._add_retrieved_documents_to_queries(
            queries, documents_path=self.config.documents_path, text_column="answer"
        )
        for query in queries:
            games_to_play = self.__prepare_tuples_for_query(query)
            for answer_a, answer_b in games_to_play:
                qid = query.qid
                agent_a = answer_a.agent
                agent_b = answer_b.agent
                all_tuples += 1
                if (qid, agent_a, agent_b) in skip_tuples:
                    logger.debug(f"Skipping {qid} {agent_a} {agent_b}")
                    continue
                tuples_to_eval.append((query, answer_a, answer_b))
        if len(tuples_to_eval) == 0:
            logger.info("All answers have been evaluated")
            if self.config.verbose:
                print(
                    f"All {all_tuples} answers are already evaluated.\n"
                    "If you want to re-evaluate them, use the force flag"
                )
            return evaluations

        for query, answer_a, answer_b in tqdm(
            tuples_to_eval,
            desc="Evaluating games",
            disable=not self.config.verbose,
            leave=False,
            position=0,
            ncols=100,
        ):
            agent_a = answer_a.agent
            agent_b = answer_b.agent
            try:
                raw_answer, parsed_answer = self.evaluate_pairwise(
                    query=query,
                    answer_a=answer_a,
                    answer_b=answer_b,
                    retrieved_documents=query.retrieved_docs,
                )

            except (RetryError, ValueError):
                failed_evaluations += 1
                continue
            evaluations.append(
                AnswerEvaluatorResult(
                    qid=query.qid,
                    agent_a=agent_a,
                    agent_b=agent_b,
                    raw_answer=raw_answer,
                    answer=parsed_answer,
                )
            )
            self._dump_response(evaluations[-1], self.output_columns, self.output_file)
        if self.config.verbose:
            print("✅ Done!")
            print(f"Unparsed answers: {failed_evaluations}")
            print(f"Total evaluations: {len(evaluations)}")
        return evaluations

    def evaluate_pairwise(
        self,
        query: Query | str,
        answer_a: AgentAnswer | str,
        answer_b: AgentAnswer | str,
        retrieved_documents: list[str] | list[Document],
        query_metadata: Optional[dict[str, Any]] = None,
        answer_a_metadata: Optional[dict[str, Any]] = None,
        answer_b_metadata: Optional[dict[str, Any]] = None,
        document_metadata: Optional[list[dict[str, Any]]] = None,
    ) -> tuple[str, str]:
        query = self._assemble_query(query, query_metadata)
        answer_a = self._assemble_answer(answer_a, answer_a_metadata)
        answer_b = self._assemble_answer(answer_b, answer_b_metadata)
        if isinstance(retrieved_documents, str):
            retrieved_documents = [retrieved_documents]
        if retrieved_documents:
            retrieved_and_assembled_docs = self._assemble_documents(
                retrieved_documents, document_metadata
            )
            query.retrieved_docs = retrieved_and_assembled_docs

        prompt = self._build_message_pairwise(query, (answer_a, answer_b))
        qid = query.qid
        agent_a_id = answer_a.agent
        agent_b_id = answer_b.agent

        try:
            raw_answer = self.llm_provider(prompt)
        except RetryError as e:
            logger.warning(
                f"Failed to FETCH answers for {qid} {agent_a_id}, {agent_b_id}"
            )
            raise e
        try:
            processed_answer = self._process_answer(raw_answer)
        except ValueError as e:
            logger.warning(
                f"Failed extracting answer for {qid}, {agent_a_id}, {agent_b_id}."
                "Probably not enough tokens in the answer."
                f"Full answer:\n{raw_answer}",
            )
            raise e
        return raw_answer, processed_answer

    def _build_message_pairwise(
        self, query: Query, answer: AgentAnswer | tuple[AgentAnswer, AgentAnswer]
    ) -> str:
        assert isinstance(answer, tuple)
        reasonings = self._prepare_documents(query)
        query_metadata = self._get_usable_fields_from_metadata(
            self.prompt, query.metadata, skip_fields=[self.config.query_placeholder]
        )
        answer_a_metadata = self._get_usable_fields_from_metadata(
            self.prompt,
            answer[0].metadata,
            skip_fields=[self.config.answer_placeholder],
        )
        answer_b_metadata = self._get_usable_fields_from_metadata(
            self.prompt,
            answer[1].metadata,
            skip_fields=[self.config.answer_placeholder],
        )
        formatters = {
            self.config.query_placeholder: query.query,
            self.config.documents_placeholder: reasonings,
            "answer_a": answer[0].text,
            "answer_b": answer[1].text,
            **query_metadata,
            **answer_a_metadata,
            **answer_b_metadata,
        }
        return self.prompt.format(**formatters)

    def __generate_games_per_query(self, query: Query) -> list[tuple[str, str]]:
        """Generates up to self.k random pairs of agents for the given query"""
        query_agents = list({x.agent for x in query.answers})
        # Create all possible pairs
        pairs = [(a, b) for a in query_agents for b in query_agents if a != b]
        if self.bidirectional:
            pairs += [(b, a) for a, b in pairs]
        random.shuffle(pairs)
        return pairs[: self.k]

    def __prepare_tuples_for_query(
        self,
        query: Query,
    ) -> list[tuple[AgentAnswer, AgentAnswer]]:
        all_tuples = []
        answers = {}
        for agent_answer in query.answers:
            answers[agent_answer.agent] = agent_answer
        random_pairs = self.__generate_games_per_query(query)
        for agent_a, agent_b in random_pairs:
            all_tuples.append((answers[agent_a], answers[agent_b]))
        return all_tuples

    def _process_answer(self, answer: str) -> str:
        """Extracts the relevant part of an answer."""
        match_ans = self.pattern.search(answer)
        if not match_ans:
            raise ValueError(f"Could not find answer in {answer}")
        answer = match_ans.group(1)
        if answer not in ["A", "B", "C"]:
            raise ValueError(f"Unknown answer: {answer}")
        return answer

    def _build_message(
        self, query: Query, answer: AgentAnswer
    ) -> str | list[dict[str, str]]:
        raise NotImplementedError

    @staticmethod
    def _load_reasonings(
        reasoning_path: str,
        query_id_col: str = "qid",
        document_id_col: str = "did",
        answer_col: str = "answer",
    ) -> dict[str, dict[str, str]]:
        reasoning: dict[str, dict[str, str]] = defaultdict(lambda: dict())
        reasoning_read = 0
        if not os.path.exists(reasoning_path):
            raise FileNotFoundError(f"Reasoning file {reasoning_path} not found")

        logger.info(f"Loading reasonings from {reasoning_path}")
        for line in csv.DictReader(open(reasoning_path)):
            reasoning_read += 1
            reasoning[line[query_id_col]][line[document_id_col]] = line[answer_col]
        logger.info(f"Loaded {reasoning_read} reasonings")
        return dict(reasoning)
