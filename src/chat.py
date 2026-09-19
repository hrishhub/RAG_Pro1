from src.rag import RAG


def start_chat():

    rag = RAG(
        db_path="storage/chroma_db",
        distance_threshold=1.4
    )

    print("=" * 60)
    print("                 LOCAL RAG ASSISTANT")
    print("=" * 60)

    print()
    print("Ask questions about your documents.")
    print("Type 'exit' to quit.")
    print()

    while True:

        question = input("You: ").strip()

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        if not question:
            continue

        try:

            result = rag.ask(
                question,
                n_results=3
            )

            print("\nAssistant:")
            print(result["answer"])

            if result["context"]:

                print("\nRetrieved Sources:")

                for i, item in enumerate(
                    result["context"]
                ):

                    metadata = item["metadata"]

                    source = metadata.get(
                        "source",
                        "Unknown"
                    )

                    chunk_id = metadata.get(
                        "chunk_id",
                        "Unknown"
                    )

                    distance = item["distance"]

                    print(
                        f"[{i + 1}] "
                        f"{source} — "
                        f"Chunk {chunk_id} "
                        f"(distance: {distance:.4f})"
                    )

            print()

        except Exception as e:

            print(f"\nError: {e}\n")


if __name__ == "__main__":
    start_chat()