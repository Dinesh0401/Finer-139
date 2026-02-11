"""Evaluation orchestration stubs."""

from dataclasses import dataclass


@dataclass
class EvaluationResult:
    method: str
    pass_id: str
    score: float


def summarize(results: list[EvaluationResult]) -> dict[str, float]:
    """Summarize average score per method."""
    buckets: dict[str, list[float]] = {}
    for item in results:
        buckets.setdefault(item.method, []).append(item.score)
    return {
        method: sum(scores) / len(scores)
        for method, scores in buckets.items()
        if scores
    }
