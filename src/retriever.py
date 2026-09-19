from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


class Retriever:

    def __init__(
        self,
        db_path="storage/chroma_db"
    ):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore(
            path=db_path
        )

    def retrieve(
        self,
        query,
        n_results=3,
        distance_threshold=1.4
    ):

        query_embedding = (
            self.embedding_model.embed_text(query)
        )

        results = self.vector_store.search(
            query_embedding,
            n_results=n_results
        )

        documents = results["documents"][0]
        distances = results["distances"][0]
        metadatas = results["metadatas"][0]

        retrieved = []

        for document, distance, metadata in zip(
            documents,
            distances,
            metadatas
        ):

            # Reject irrelevant results
            if distance > distance_threshold:
                continue

            retrieved.append(
                {
                    "document": document,
                    "distance": distance,
                    "metadata": metadata
                }
            )

        return retrieved