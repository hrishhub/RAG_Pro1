def build_prompt(question, retrieved_documents):
    
    context_parts = []

    for i, item in enumerate(retrieved_documents):

        document = item["document"]
        metadata = item["metadata"]

        source = metadata.get(
            "source",
            "Unknown"
        )

        chunk_id = metadata.get(
            "chunk_id",
            "Unknown"
        )

        context_parts.append(
            f"""
[Source {i + 1}]
File: {source}
Chunk: {chunk_id}

Content:
{document}
"""
        )

    context = "\n".join(context_parts)

    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using ONLY the
information provided in the context.

IMPORTANT RULES:

1. Do not use outside knowledge.
2. Do not make up information.
3. If the answer cannot be found in the context,
   say:
   "I don't know based on the provided documents."
4. Keep the answer clear and concise.
5. At the end of your answer, provide the sources
   you used.
6. Use exactly this source format:

Sources:
[1] filename — Chunk X
[2] filename — Chunk X

Only include sources that actually support
your answer.

================ CONTEXT ================

{context}

==========================================

Question:
{question}

Answer:
"""

    return prompt