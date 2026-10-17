
from datetime import datetime, timezone
from pathlib import Path

from app.ingestion.loader import load_markdown
from app.ingestion.chunker import chunk_text
from app.ingestion.service import create_document_chunk, embed_chunks

from app.ingestion.fake_embedding_provider import FakeEmbeddingProvider


def main() -> None:
    # 1. Inject the provider and generate embeddings.
    provider = FakeEmbeddingProvider()
    # 2. Load the source document.
    path = Path(
        "/Users/binayakchakraborty/personal-workspace/custom-project-harness/tests/ingestion/test-markdown.md"
    )
    content = load_markdown(path)
    chunks = chunk_text(content)

    document_chunks = []
    # 3. Create metadata-rich chunks and deterministic IDs.
    for chunk in chunks:
        document_chunk = create_document_chunk(
            content=chunk,
            document_id=path.name,
            version="1",
            is_current=True,
            source=str(path),
            page=None,
            system="example_system",
            service="example_service",
            environment="example_environment",
            document_type="example_document_types",
            created_at=datetime.now(timezone.utc),
            created_by="example_created_by",
            chunk_index=chunks.index(chunk) 
        )
        document_chunks.append(document_chunk)
    results = embed_chunks(
        chunks=document_chunks,
        embedding_provider=provider,
        expected_dimension=1536,
    )

    # 4. Display the results.
    print(f"Created {len(document_chunks)} chunks")
    print(f"Embedded {len(results)} chunks")

    for result in results:
        print(f"Chunk ID: {result.chunk.chunk_id}")
        print(f"Embedding dimensions: {len(result.embedding)}")


if __name__ == "__main__":
    main()