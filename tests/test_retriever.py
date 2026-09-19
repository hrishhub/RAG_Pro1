from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore
from src.retriever import Retriever


def test_retriever():

    documents = [
        "RAG retrieves relevant information from documents.",
        "Vector databases store embeddings for semantic search.",
        "Python is a programming language."
    ]

    embedding_model = EmbeddingModel()
    embeddings = embedding_model.embed_documents(documents)

    # Create test database
    store = VectorStore(
        path="storage/test_retriever_db"
    )

    store.add_documents(
        documents,
        embeddings
    )

    # Create retriever
    retriever = Retriever(
        db_path="storage/test_retriever_db"
    )

    query = "How does RAG find information?"

    results = retriever.retrieve(
        query,
        n_results=2
    )

    print("\n========== RETRIEVED CHUNKS ==========")

    for i, result in enumerate(results):
        print(f"\nChunk {i + 1}:")
        print(result)

    print("\n=======================================")

    assert len(results) == 2