from src.llm import LLM


def test_llm():

    llm = LLM()

    prompt = """
    Explain RAG in simple terms.
    """

    response = llm.generate(prompt)

    print("\n========== LLM RESPONSE ==========")
    print(response)
    print("===================================")

    assert response is not None
    assert len(response) > 0