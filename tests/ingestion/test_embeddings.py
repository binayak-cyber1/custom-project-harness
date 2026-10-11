from app.ingestion.embeddings import EmbeddingProvider

class FakeEmbeddingProvider:
    def embed_text(self, text: str) -> list[float]:
        return [0.1,0.2, 0.3]  # Fake embedding for testing purposes

def test_fake_provider_returns_vector():
    provider: EmbeddingProvider = FakeEmbeddingProvider()
    vector = provider.embed_text("Payment authorization failed")
    assert vector == [0.1, 0.2, 0.3]
    assert len(vector) == 3