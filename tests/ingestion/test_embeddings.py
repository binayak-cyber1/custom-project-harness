import pytest
from app.ingestion.embeddings import EmbeddingProvider

class FakeEmbeddingProvider:
    def embed_text(self, text: str) -> list[float]:
        return [0.1,0.2, 0.3]  # Fake embedding for testing purposes
    def validate_embedding(self, vector: list[float], expected_diamensions: int) -> None:
        if any(value != value for value in vector):  # Check for NaN values
            raise ValueError("Vector contains NaN values")
        if len(vector) != expected_diamensions:
            raise ValueError(f"Vector length {len(vector)} does not match expected dimensions {expected_diamensions}")

def test_fake_provider_returns_vector():
    provider: EmbeddingProvider = FakeEmbeddingProvider()
    vector = provider.embed_text("Payment authorization failed")
    assert vector == [0.1, 0.2, 0.3]
    assert len(vector) == 3

@pytest.mark.parametrize("vector, expected_diamensions", [
    ([0.1, 0.2, float('nan')], 3),
    ([0.4, 0.5], 5),
])
def test_fake_provider_returns_invalid_vector(vector, expected_diamensions):
    provider: EmbeddingProvider = FakeEmbeddingProvider()
    with pytest.raises(ValueError):
        provider.validate_embedding(vector, expected_diamensions=expected_diamensions)