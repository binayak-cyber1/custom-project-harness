
import datetime

from app.ingestion import chunker
from app.ingestion.identity import make_chunk_id
from app.ingestion.models import DocumentChunk
from app.ingestion.models import EmbeddedChunk
from app.ingestion.embeddings import EmbeddingProvider
from app.ingestion.validate_embedding import validate_embedding
from app.ingestion.fake_embedding_provider import FakeEmbeddingProvider
from app.ingestion.loader import load_markdown;
from pathlib import Path

def create_document_chunk(
        content: str,
        document_id: str,
        version: str,
        is_current: bool,
        source: str,
        page: int,
        system: str,
        service: str,
        environment: str,
        document_type: str,
        created_at: datetime,
        created_by: str,
        chunk_index: int
) -> DocumentChunk:
    return DocumentChunk(
        chunk_id=make_chunk_id(document_id, version, chunk_index),
        document_id=document_id,
        version=version,
        is_current=is_current,
        source=source,
        page=page,
        system=system,
        service=service,
        environment=environment,
        document_type=document_type,
        created_at=created_at,
        created_by=created_by,
        content=content
)

def embed_chunks(
        chunks: list[DocumentChunk],
        embedding_provider: EmbeddingProvider,
        expected_dimension: int,
        ) -> list[EmbeddedChunk]:
    embedded_chunks: list[EmbeddedChunk] = []
    for chunk in chunks:
        embedding = embedding_provider.embed_text(chunk)
        validate_embedding(embedding, expected_dimension = expected_dimension)
        embedded_chunks.append(EmbeddedChunk(chunk=chunk, embedding=embedding))
    return embedded_chunks

 