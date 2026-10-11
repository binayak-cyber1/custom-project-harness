import pytest

from app.ingestion.identity import make_chunk_id

def test_chunk_id_is_deterministic():
    first = make_chunk_id("oms-payment-runbook", "4.3", 0)
    second = make_chunk_id("oms-payment-runbook", "4.3", 0)
    assert first == second

def test_different_versions_produce_different_ids():
    old_id = make_chunk_id("oms-payment-runbook", "4.3", 0)
    new_id = make_chunk_id("oms-payment-runbook", "4.4", 0)
    assert old_id != new_id

def test_different_chunk_indexes_produce_different_ids():
    first = make_chunk_id("oms-payment-runbook", "4.3", 0)
    second = make_chunk_id("oms-payment-runbook", "4.3", 1)
    assert first != second

@pytest.mark.parametrize(
    ("document_id, version, chunk_index"), [
    ("", "4.3", 0),
    ("oms-payment-runbook", "", 1),
    ("oms-payment-runbook", "4.4", -1),
])
def test_invalid_identity_input_raises(
    document_id, version, chunk_index
):
    with pytest.raises(ValueError):
        make_chunk_id(document_id, version, chunk_index)