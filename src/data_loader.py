"""Data loading utilities for FINER-139 experiments."""

from pathlib import Path
from typing import Any


def load_jsonl(path: str | Path) -> list[dict[str, Any]]:
    """Load JSONL records from disk.

    This is a placeholder utility and should be replaced with production
    dataset parsing logic.
    """
    import json

    records: list[dict[str, Any]] = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                records.append(json.loads(line))
    return records
