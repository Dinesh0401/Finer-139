"""Common utility helpers."""

from datetime import datetime, timezone


def utc_timestamp() -> str:
    """Return a compact UTC timestamp for artifact naming."""
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
