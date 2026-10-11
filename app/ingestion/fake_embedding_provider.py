from app.ingestion.models import DocumentChunk

class FakeEmbeddingProvider:
    def embed_text(chunk: DocumentChunk) -> list[float]:
        # Return a fake embedding of the expected dimension
        return [0.0] * 5  # Replace 1536 with the actual expected dimension if known