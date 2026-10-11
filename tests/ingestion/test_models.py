from datetime import datetime
from app.ingestion.models import DocumentChunk

def test_document_chunk_can_be_created():
    chunk = DocumentChunk(
        chunk_id="oms-payment-runbook-v4-2-p31-c02",
        document_id="oms-payment-runbook",
        version="4.2",
        is_current=True,
        source="oms-payment-runbook.pdf",
        page=31,
        system="oms",
        service="payment-service",
        environment="runbook",
        document_types="runbook",
        created_at=datetime.fromisoformat("2024-06-01T00:00:00Z"),
        created_by="commerce-platform-team",
        content=(
            "Payment authorization failures are retired twice"
            "with a 30 second interval."
        )
    )
    assert chunk.chunk_id == "oms-payment-runbook-v4-2-p31-c02"
    assert chunk.document_id == "oms-payment-runbook"
    assert chunk.version == "4.2"
    assert chunk.is_current is True
    assert chunk.source == "oms-payment-runbook.pdf"
    assert chunk.page == 31
    assert chunk.system == "oms"
    assert chunk.service == "payment-service"
    assert chunk.environment == "runbook"
    assert chunk.document_types == "runbook"
    assert chunk.created_at == datetime.fromisoformat("2024-06-01T00:00:00Z")
    assert chunk.created_by == "commerce-platform-team"
    assert chunk.content == (
        "Payment authorization failures are retired twice"
        "with a 30 second interval."
    )