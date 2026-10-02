from __future__ import annotations

import json
import sys

from .knowledge_base import KnowledgeBase
from .llm import generate_answer


def run_agent(question: str) -> dict:
    kb = KnowledgeBase()
    matches = kb.search(question, limit=3)
    answer = generate_answer(question, matches)

    return {
        "question": question,
        "answer": answer,
        "sources": [
            {
                "title": match["title"],
                "path": match["path"],
                "snippet": match["content"][:250],
            }
            for match in matches
        ],
    }


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "How do we onboard a new customer?"
    result = run_agent(query)
    print(json.dumps(result, indent=2, ensure_ascii=False))
