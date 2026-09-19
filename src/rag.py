from src.retriever import Retriever
from src.prompt import build_prompt
from src.llm import LLM


class RAG:

    def __init__(
        self,
        db_path="storage/chroma_db",
        distance_threshold=1.4
    ):

        self.retriever = Retriever(
            db_path=db_path
        )

        self.llm = LLM()

        self.distance_threshold = distance_threshold

    def ask(
        self,
        question,
        n_results=3
    ):

        # Retrieve relevant documents
        retrieved = self.retriever.retrieve(
            question,
            n_results=n_results,
            distance_threshold=self.distance_threshold
        )

        # No relevant information
        if not retrieved:

            return {
                "question": question,
                "context": [],
                "answer": (
                    "I don't know based on the "
                    "provided documents."
                )
            }

        # Build prompt
        prompt = build_prompt(
            question,
            retrieved
        )

        # Generate answer
        answer = self.llm.generate(
            prompt
        )

        return {
            "question": question,
            "context": retrieved,
            "answer": answer
        }