from pydantic import BaseModel
from datetime import datetime

class DocumentChunk(BaseModel):
    chunk_id: str
    document_id: str
    version: str
    is_current: bool

    source: str
    page: int | None = None
    
    system: str
    service: str
    environment: str
    document_type: str

    created_at: datetime
    created_by: str

    content: str

class EmbeddedChunk(BaseModel):
    chunk: DocumentChunk
    embedding: list[float]
