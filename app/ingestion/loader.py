from pathlib import Path

def load_markdown(file_path:str) -> str:
    """Load the content of a markdown file as a string."""
    path = Path(file_path)
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {file_path}")
    if path.suffix.lower() != ".md":
        raise ValueError(f"Expected a markdown file, got: {file_path}")
    return path.read_text(encoding="utf-8")
