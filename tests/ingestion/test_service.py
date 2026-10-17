from app.ingestion.models import DocumentChunk, EmbeddedChunk
from app.ingestion.service import create_document_chunk, embed_chunks
import datetime

""" the test for the embed_chunks function using the FakeEmbeddingProvider """
class FakeEmbeddingProvider:
    def __init__(self):
        self.expected_dimension = 3

    def embed_text(self, chunk):
        # Return a fake embedding of the expected dimension
        return [0.0] * self.expected_dimension

""" Function to preparing document chunks for testing embedding"""
def create_chunk_for_test() -> DocumentChunk:
    content1 = "This is a sample document content for testing."
    content2 = " It will be chunked and embedded using the FakeEmbeddingProvider."

    document_chunks = []
    
    document_chunks.append(create_document_chunk(
        content=content1,
        document_id="doc1",
        version="v1",
        is_current=True,
        source="source1",
        page=1,
        system="system1",
        service="service1",
        environment="env1",
        document_type="type1",
        created_at=datetime.datetime.now(),
        created_by="user1",
        chunk_index=0
    ))
    document_chunks.append(create_document_chunk(
        content=content2,
        document_id="doc1",
        version="v1",
        is_current=True,
        source="source1",
        page=1,
        system="system1",
        service="service1",
        environment="env1",
        document_type="type1",
        created_at=datetime.datetime.now(),
        created_by="user1",
        chunk_index=1
    ))

    return document_chunks

def test_embed_chunks_with_fake_provider():

    # Use the FakeEmbeddingProvider
    provider = FakeEmbeddingProvider()
    embedded_chunks = embed_chunks(create_chunk_for_test(), provider, expected_dimension=3)

    # Assertions
    assert len(embedded_chunks) == 2
    assert isinstance(embedded_chunks[0], EmbeddedChunk)
    assert embedded_chunks[0].embedding == [0.0, 0.0, 0.0]
    assert isinstance(embedded_chunks[1], EmbeddedChunk)