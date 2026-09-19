from src.prompt import build_prompt


def test_prompt():

    question = "What is RAG?"

    context = """
    RAG stands for Retrieval-Augmented Generation.
    It retrieves relevant information from documents
    and provides that information to a language model.
    """

    prompt = build_prompt(question, context)

    print("\n========== GENERATED PROMPT ==========")
    print(prompt)
    print("======================================")

    assert "What is RAG?" in prompt
    assert "Retrieval-Augmented Generation" in prompt
    assert "documents" in prompt