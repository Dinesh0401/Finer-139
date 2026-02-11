"""Metric helpers for experiment evaluation."""


def accuracy(correct: int, total: int) -> float:
    """Return simple accuracy percentage in [0, 100]."""
    if total <= 0:
        return 0.0
    return (correct / total) * 100.0
