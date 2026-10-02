from __future__ import annotations

from pathlib import Path
from typing import List

from .config import KNOWLEDGE_BASE_DIR


class KnowledgeBase:
    def __init__(self, base_dir: Path | str | None = None):
        self.base_dir = Path(base_dir) if base_dir else KNOWLEDGE_BASE_DIR
        self.documents = self._load_documents()

    def _load_documents(self) -> list[dict]:
        items: list[dict] = []
        if not self.base_dir.exists():
            return items

        for file_path in sorted(self.base_dir.glob("*.md")):
            text = file_path.read_text(encoding="utf-8")
            items.append({
                "title": file_path.stem.replace("_", " ").title(),
                "path": str(file_path),
                "content": text.strip(),
            })
        return items

    def search(self, query: str, limit: int = 3) -> list[dict]:
        query_terms = [term.lower() for term in query.split() if term.strip()]
        if not query_terms:
            return self.documents[:limit]

        ranked: list[tuple[float, dict]] = []
        for doc in self.documents:
            content = doc["content"].lower()
            title = doc["title"].lower()
            score = 0.0
            for term in query_terms:
                score += content.count(term) * 2
                score += title.count(term) * 5
            if score > 0:
                ranked.append((score, doc))

        if not ranked:
            return self.documents[:limit]

        ranked.sort(key=lambda item: item[0], reverse=True)
        return [doc for _, doc in ranked[:limit]]

    def get_summary(self, query: str) -> str:
        matches = self.search(query)
        if not matches:
            return "No match found in the local knowledge base."

        summary = []
        for match in matches:
            snippet = match["content"]
            summary.append(f"## {match['title']}\n{snippet[:500]}\n")
        return "\n".join(summary)
