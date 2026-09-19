from src.embeddings import EmbeddingModel


def test_embedding():

    model = EmbeddingModel()

    text = "RAG retrieves relevant information from documents."

    vector = model.embed_text(text)

    print("\n========== EMBEDDING ==========")
    print("Text:")
    print(text)

    print("\nVector:")
    print(vector)

    print("\nVector dimensions:")
    print(len(vector))

    print("===============================")

    assert vector is not None
    assert len(vector) == 384