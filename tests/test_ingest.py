from src.ingest import ingest_document


def test_ingest():

    chunks = ingest_document(
        file_path="data/raw/rag_notes.txt",
        db_path="storage/chroma_db"
    )

    print("\n========== INGESTION ==========")
    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i + 1}:")
        print(chunk)

    print("===============================")

    assert len(chunks) > 0