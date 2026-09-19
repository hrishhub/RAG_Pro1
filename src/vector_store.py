import chromadb


class VectorStore:

    def __init__(self, path="storage/chroma_db"):

        self.client = chromadb.PersistentClient(
            path=path
        )

        self.collection = self.client.get_or_create_collection(
            name="rag_documents"
        )

    def add_documents(
        self,
        documents,
        embeddings,
        metadatas=None
    ):

        ids = [
            f"doc_{i}"
            for i in range(len(documents))
        ]

        if metadatas is None:
            metadatas = [
                {
                    "source": "unknown",
                    "chunk_id": i
                }
                for i in range(len(documents))
            ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding,
        n_results=3
    ):

        results = self.collection.query(
            query_embeddings=[
                query_embedding.tolist()
            ],
            n_results=n_results,
            include=[
                "documents",
                "distances",
                "metadatas"
            ]
        )

        return results