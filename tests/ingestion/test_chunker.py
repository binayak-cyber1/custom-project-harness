from app.ingestion.chunker import chunk_text
import pytest

def test_short_text_returns_one_chunk():
    assert chunk_text("Payment succeeded", chunk_size=100) == ["Payment succeeded"] 

def test_long_text_returns_multiple_chunks():
    text = "Payment succeeded. Payment succeeded. Payment succeeded."
    chunks = chunk_text(text, chunk_size=20, overlap=5)
    assert len(chunks) > 1
    assert all(len(chunk) <= 20 for chunk in chunks)

def test_chunks_overlap():
    chunks = chunk_text("Payment succeeded.", chunk_size=8, overlap=2)
    assert chunks == ["Payment", "t succee", "eeded."]

def test_empty_text_returns_no_chunks():
    assert chunk_text(" ") == []

@pytest.mark.parametrize("chunk_size,overlap", 
                         [(0, 0),
                          (-1, 0),
                          (10, -1),
                          (10, 11)
                          ]
)
def test_invalid_configuration_raises(chunk_size, overlap):
    text = "Some payment text"
    with pytest.raises(ValueError):
        chunk_text(text, chunk_size=chunk_size, overlap=overlap)