from typing import Protocol

class EmbeddingProvider(Protocol):
    """ Contract for a component that converts text into embeddings."""
    def embed_text(self, text: str) -> list[float]:
        ...