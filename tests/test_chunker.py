from src.chunker import chunk_text


def test_chunk_text():

    text = "A" * 1200

    chunks = chunk_text(
        text,
        chunk_size=500,
        overlap=50
    )

    print("\n========== CHUNKS ==========")

    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i + 1}")
        print(f"Length: {len(chunk)}")
        print(chunk[:100] + "...")

    print("\nTotal chunks:", len(chunks))
    print("============================")

    assert len(chunks) > 1

    for chunk in chunks:
        assert len(chunk) <= 500