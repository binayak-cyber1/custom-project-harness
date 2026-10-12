from pathlib import Path


def load_markdown(path: Path) -> str:
    """Load the content of a Markdown file as a string."""

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    if path.suffix.lower() != ".md":
        raise ValueError(f"Expected a Markdown file, got: {path}")

    return path.read_text(encoding="utf-8")