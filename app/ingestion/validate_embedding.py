import math

def validate_embedding(vector: list[float], expected_diamensions: int = 5) -> bool:
    if expected_diamensions is None:
        raise ValueError("Expected dimensions cannot be None.")
    if expected_diamensions <= 0:
        raise ValueError("Expected dimensions must be a positive integer.")
    if not vector:
        raise ValueError("Embedding vector cannot be None.")
    if expected_diamensions is not None and len(vector) != expected_diamensions:
        raise ValueError(f"Embedding vector length does not match the expected dimensions: {expected_diamensions}")
    if not all(math.isfinite(v) for v in vector):
        raise ValueError("Embedding vector contains non-finite numbers.")
    if any(math.isnan(v) for v in vector):
        raise ValueError("Embedding vector contains NaN values.")
            
    return True