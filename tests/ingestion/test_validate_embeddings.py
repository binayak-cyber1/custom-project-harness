import pytest
from app.ingestion.validate_embedding import validate_embedding

def test_validate_embedding_valid():
    vector = [0.1, 0.2, 0.3, 0.4, 0.5]
    assert validate_embedding(vector, expected_dimension=5) is True

def test_validate_embedding_invalid_length():
    vector = [0.1, 0.2]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=5)

def test_validate_embedding_contains_nan():
    vector = [0.1, float("nan"), 0.3]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=3)

def test_validate_embedding_contains_inf():
    vector = [0.1, float("inf"), 0.3]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=3)

def test_validate_embedding_contains_non_finite():
    vector = [0.1, float("inf"), float("nan")]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=3)

def test_validate_embedding_empty_vector():
    vector = []
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=0)

def test_validate_embedding_none_vector():
    vector = None
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=5)

def test_validate_embedding_expected_dimensions_none():
    vector = [0.1, 0.2, 0.3]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=None)

def test_validate_embedding_expected_dimensions_negative():
    vector = [0.1, 0.2, 0.3]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=-1)

def test_validate_embedding_expected_dimensions_zero():
    vector = [0.1, 0.2, 0.3]
    with pytest.raises(ValueError):
        validate_embedding(vector, expected_dimension=0)