import pytest
from app.ingestion.loader import load_markdown

def test_load_markdown_returns_raw_text(tmp_path):
    file_path= tmp_path / "inventory_runbook.md"
    expected_content = "# Payment Runbook\n\nThis is a test runbook."
    file_path.write_text(expected_content, encoding="utf-8")
    actual = load_markdown(file_path)

    assert actual == expected_content

def test_load_markdown_raises_for_missing_file(tmp_path):
    file_path = tmp_path / "nonexistent_file.md"
    with pytest.raises(FileNotFoundError):
        load_markdown(file_path)

def test_load_markdown_raises_for_non_markdown_file(tmp_path):
    file_path = tmp_path / "inventory_runbook.txt"
    file_path.write_text("# Inventory Runbook\n\nThis is a test runbook.", encoding="utf-8")
    with pytest.raises(ValueError):
        load_markdown(file_path)