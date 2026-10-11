def make_chunk_id(
        document_id: str,
        version: str,
        chunk_index: int,
        ) -> str:
    """Generate a unique chunk ID based on document ID, version, and chunk index."""
    if not document_id.strip():
        raise ValueError("document_id must be a non-empty string")
    if not version.strip():
        raise ValueError("version must be a non-empty string")
    if chunk_index < 0:
        raise ValueError("chunk_index must be a non-negative integer")
    
    return f"{document_id}:v{version}:chunk-{chunk_index}"