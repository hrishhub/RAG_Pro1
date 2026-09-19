from src.loaders import load_document
from src.chunker import chunk_text


def test_real_document_chunking():

    document = load_document("data/raw/rag_notes.txt")

    chunks = chunk_text(
        document,
        chunk_size=500,
        overlap=50
    )

    print("\n========== RAG DOCUMENT ==========")
    print("Document characters:", len(document))
    print("Number of chunks:", len(chunks))

    for i, chunk in enumerate(chunks):
        print(f"\n--- Chunk {i + 1} ---")
        print(chunk)

    print("\n===================================")

    assert len(chunks) > 0