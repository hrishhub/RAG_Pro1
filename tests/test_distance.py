from src.retriever import Retriever


def test_distance():

    retriever = Retriever(
        db_path="storage/chroma_db"
    )

    questions = [
        "What is RAG?",
        "What are embeddings?",
        "What is a vector database?",
        "What is the capital of France?"
    ]

    print("\n")
    print("=" * 70)
    print("                 DISTANCE ANALYSIS")
    print("=" * 70)

    for question in questions:

        results = retriever.retrieve(
            question,
            n_results=3
        )

        print("\n")
        print("QUESTION:")
        print(question)

        print("-" * 70)

        for i, result in enumerate(results):

            print(
                f"Result {i + 1} | "
                f"Distance: {result['distance']}"
            )

            print(
                f"Source: "
                f"{result['metadata'].get('source')}"
            )

            print(
                f"Chunk: "
                f"{result['metadata'].get('chunk_id')}"
            )

    print("\n")
    print("=" * 70)

    assert True