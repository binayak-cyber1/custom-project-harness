import math

def validate_embedding(vector: list[float], expected_dimension: int) -> bool:
    if expected_dimension is None:
        raise ValueError("Expected dimension cannot be None.")
    if expected_dimension <= 0:
        raise ValueError("Expected dimension must be a positive integer.")
    if not vector:
        raise ValueError("Embedding vector cannot be None.")
    if expected_dimension is not None and len(vector) != expected_dimension:
        raise ValueError(f"Embedding vector length {len(vector)} does not match the expected dimension: {expected_dimension}")
    if not all(math.isfinite(v) for v in vector):
        raise ValueError("Embedding vector contains non-finite numbers.")
    if any(math.isnan(v) for v in vector):
        raise ValueError("Embedding vector contains NaN values.")
            
    return True