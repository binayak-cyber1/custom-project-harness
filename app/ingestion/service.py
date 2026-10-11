
from app.ingestion.models import DocumentChunk
from app.ingestion.models import EmbeddedChunk
from app.ingestion.embeddings import EmbeddingProvider
from app.ingestion.validate_embedding import validate_embedding
from app.ingestion.fake_embedding_provider import FakeEmbeddingProvider

def embed_chunks(
        chunks: list[DocumentChunk],
        embedding_provider: EmbeddingProvider,
        expected_dimension: int,
        ) -> list[EmbeddedChunk]:
    embedded_chunks: list[EmbeddedChunk] = []
    for chunk in chunks:
        embedding = embedding_provider.embed_text(chunk)
        validate_embedding(expected_dimension)
        embedded_chunks.append(EmbeddedChunk(chunk=chunk, embedding=embedding))
    return embedded_chunks

provider = FakeEmbeddingProvider()
provider.embed_text(DocumentChunk(content="test"))