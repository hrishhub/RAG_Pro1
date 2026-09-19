from src.rag import RAG


def test_rag():

    rag = RAG(
        db_path="storage/chroma_db",
        distance_threshold=1.4
    )

    # ==========================================
    # TEST 1: RELEVANT QUESTION
    # ==========================================

    question = "What is RAG?"

    result = rag.ask(
        question,
        n_results=3
    )

    print("\n")
    print("=" * 70)
    print("           TEST 1 — RELEVANT QUESTION")
    print("=" * 70)

    print("\nQUESTION:")
    print(result["question"])

    print("\nRETRIEVED CHUNKS:")
    print("-" * 70)

    for i, item in enumerate(
        result["context"]
    ):

        metadata = item["metadata"]

        print(
            f"\n--- Chunk {i + 1} ---"
        )

        print(
            f"Source: "
            f"{metadata.get('source', 'Unknown')}"
        )

        print(
            f"Chunk ID: "
            f"{metadata.get('chunk_id', 'Unknown')}"
        )

        print(
            f"Distance: "
            f"{item['distance']}"
        )

        print("\nDocument:")
        print(item["document"])

    print("\nANSWER:")
    print("-" * 70)
    print(result["answer"])

    # Relevant question must retrieve something
    assert len(result["context"]) >= 1

    assert result["answer"] is not None
    assert len(result["answer"]) > 0

    # ==========================================
    # TEST 2: IRRELEVANT QUESTION
    # ==========================================

    question_2 = "What is the capital of France?"

    result_2 = rag.ask(
        question_2,
        n_results=3
    )

    print("\n")
    print("=" * 70)
    print("           TEST 2 — IRRELEVANT QUESTION")
    print("=" * 70)

    print("\nQUESTION:")
    print(result_2["question"])

    print("\nRETRIEVED CHUNKS:")
    print("-" * 70)

    print(
        f"Number of relevant chunks: "
        f"{len(result_2['context'])}"
    )

    print("\nANSWER:")
    print("-" * 70)
    print(result_2["answer"])

    # Irrelevant question should retrieve nothing
    assert len(result_2["context"]) == 0

    assert (
        result_2["answer"]
        == "I don't know based on the provided documents."
    )

    print("\n" + "=" * 70)
    print("                ALL TESTS PASSED")
    print("=" * 70)