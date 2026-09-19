from src.loaders import load_document


def test_load_document():
    result = load_document("data/raw/rag_notes.txt")

    print("\n========== LOADED DOCUMENT ==========")
    print(result)
    print("=====================================")

    assert result is not None