from app.ingestion.models import DocumentChunk

class FakeEmbeddingProvider:
    def __init__(self):
        self.expected_dimension = 1536

    def embed_text(self, chunk: DocumentChunk) -> list[float]:
        # Return a fake embedding of the expected dimension
        return [0.0] * 1536  # Replace 1536 with the actual expected dimension if known