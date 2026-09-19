from src.loaders import load_document
from src.chunker import chunk_text
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


def ingest_document(
    file_path="data/raw/rag_notes.txt",
    db_path="storage/chroma_db"
):

    # ==========================================
    # 1. LOAD DOCUMENT
    # ==========================================

    document = load_document(file_path)

    if not document:
        raise ValueError(
            f"Could not load document: {file_path}"
        )

    print(f"Loaded document: {file_path}")

    # ==========================================
    # 2. CHUNK DOCUMENT
    # ==========================================

    chunks = chunk_text(document)

    if not chunks:
        raise ValueError(
            "No chunks were generated."
        )

    print(f"Number of chunks: {len(chunks)}")

    # ==========================================
    # 3. GENERATE EMBEDDINGS
    # ==========================================

    embedding_model = EmbeddingModel()

    embeddings = (
        embedding_model.embed_documents(chunks)
    )

    print(
        f"Generated embeddings: {len(embeddings)}"
    )

    # ==========================================
    # 4. CREATE METADATA
    # ==========================================

    metadatas = []

    for i, chunk in enumerate(chunks):

        metadatas.append(
            {
                "source": file_path,
                "chunk_id": i
            }
        )

    # ==========================================
    # 5. STORE IN VECTOR DATABASE
    # ==========================================

    vector_store = VectorStore(
        path=db_path
    )

    vector_store.add_documents(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadatas
    )

    print(
        "Documents, embeddings, and metadata "
        "successfully stored."
    )

    return chunks