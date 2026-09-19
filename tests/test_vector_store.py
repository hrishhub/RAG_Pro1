from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


def test_vector_store():

    embedding_model = EmbeddingModel()

    documents = [
        "RAG retrieves relevant information from documents.",
        "Vector databases store embeddings for semantic search.",
        "Python is a programming language."
    ]

    embeddings = embedding_model.embed_documents(documents)

    store = VectorStore(
        path="storage/test_chroma_db"
    )

    store.add_documents(
        documents,
        embeddings
    )

    query = "How does RAG find information?"

    query_embedding = embedding_model.embed_text(query)

    results = store.search(
        query_embedding,
        n_results=2
    )

    print("\n========== SEARCH RESULTS ==========")

    for document in results["documents"][0]:
        print("\n", document)

    print("\n=====================================")

    assert results is not None
    assert len(results["documents"][0]) == 2