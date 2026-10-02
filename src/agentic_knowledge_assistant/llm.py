from __future__ import annotations

import os
from typing import Any

from .config import AWS_ACCESS_KEY_ID, AWS_REGION, AWS_SECRET_ACCESS_KEY, OPENAI_API_KEY, OPENAI_MODEL, BEDROCK_MODEL_ID


class LocalFallbackLLM:
    def generate(self, question: str, context: str) -> str:
        context_lines = [line.strip() for line in context.splitlines() if line.strip()]
        first_chunks = "\n".join(context_lines[:5])
        answer = (
            "I used the local knowledge base to ground the answer. "
            "Based on the available documents, here is the most relevant guidance:\n\n"
            f"{first_chunks[:1800]}\n\n"
            "Recommended next action: review the cited source material, validate assumptions with stakeholders, "
            "and turn the guidance into a concrete action plan for your team."
        )
        return answer


def generate_answer(question: str, context_docs: list[dict]) -> str:
    context_text = "\n\n".join(
        f"Source: {doc['title']}\n{doc['content'][:900]}" for doc in context_docs
    )

    if OPENAI_API_KEY:
        try:
            from openai import OpenAI

            client = OpenAI(api_key=OPENAI_API_KEY)
            response = client.responses.create(
                model=OPENAI_MODEL,
                input=[
                    {
                        "role": "system",
                        "content": "You are a helpful enterprise AI assistant. Answer with grounded, concise guidance and cite the topic source."
                    },
                    {
                        "role": "user",
                        "content": f"Question: {question}\n\nContext:\n{context_text}"
                    }
                ],
            )
            return response.output_text.strip()
        except Exception:
            pass

    if AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY:
        try:
            import boto3

            client = boto3.client(
                "bedrock-runtime",
                region_name=AWS_REGION,
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
            )
            prompt = (
                "You are an expert enterprise AI assistant. Use the provided context to answer the user's question. "
                "Keep the answer practical and concise.\n\n"
                f"Question: {question}\n\nContext:\n{context_text}"
            )
            body = {
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 500,
                "messages": [{"role": "user", "content": prompt}],
            }
            result = client.invoke_model(modelId=BEDROCK_MODEL_ID, body=str(body).replace("'", '"'))
            import json

            payload = json.loads(result["body"].read())
            return payload["content"][0]["text"].strip()
        except Exception:
            pass

    return LocalFallbackLLM().generate(question, context_text)
