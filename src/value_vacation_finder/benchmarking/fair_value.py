"""
Fair-value benchmarking for Value Vacation Finder.

Section 9 of references/project_full_instructions.md defines the
benchmarking stage: no vacation candidate may be called "undervalued"
until real comparable-price benchmarking exists.

This module implements a bottom-up, component-based benchmark: fair value
is the sum of sourced comparable costs (flights, lodging, activities,
food+transport) for a trip of the same length, party size, and season.
It does not fabricate numbers itself — callers must supply real,
sourced comparable component costs (see a run's
data/raw/benchmark_prices/*.md note for provenance). If those numbers
aren't available yet, use BENCHMARKING_STATUS_NOT_READY instead of
guessing.

Because this method is built from published aggregate cost guides rather
than live, date-matched itinerary quotes, callers must also record a
benchmark_confidence ("low" | "medium" | "high") reflecting how much
source agreement backed the estimate. See the Lisbon run's benchmark
note for an example where two methodologies disagreed and confidence was
recorded as "low" for that reason.
"""

from __future__ import annotations

from typing import Any, Literal


BENCHMARKING_STATUS_NOT_READY: dict[str, Any] = {
    "fair_value_estimate_usd": None,
    "estimated_discount_pct": None,
    "benchmark_method": "not_yet_built",
    "undervalued_flag": None,
    "ready_for_benchmarking": False,
    "ready_for_scoring": False,
}

REQUIRED_COMPONENTS = ("flights_usd", "hotel_usd", "activities_usd", "food_transport_usd")

BenchmarkConfidence = Literal["low", "medium", "high"]


def estimate_fair_value(comparable_components: dict[str, float]) -> float:
    """
    Sum sourced comparable component costs into a fair-value estimate.

    comparable_components must contain all of REQUIRED_COMPONENTS, each a
    real, sourced USD figure for a trip of the same length/party size/season
    (e.g. from a data/raw/benchmark_prices/*.md capture). Raises rather than
    filling in a missing component with a guess.
    """
    missing = [component for component in REQUIRED_COMPONENTS if component not in comparable_components]

    if missing:
        raise ValueError(
            f"Missing comparable cost components: {missing}. Real benchmarking "
            "requires sourced comparable prices for every component (see "
            "Section 9 of references/project_full_instructions.md) — do not "
            "fabricate a missing component."
        )

    return round(sum(comparable_components[component] for component in REQUIRED_COMPONENTS), 2)


def calculate_discount_pct(fair_value_estimate_usd: float, actual_estimated_trip_cost_usd: float) -> float:
    """Calculate (fair_value - actual_cost) / fair_value."""
    if fair_value_estimate_usd <= 0:
        raise ValueError("fair_value_estimate_usd must be positive.")

    return round(
        (fair_value_estimate_usd - actual_estimated_trip_cost_usd) / fair_value_estimate_usd, 4
    )


def classify_undervalued_flag(discount_pct: float, benchmark_confidence: BenchmarkConfidence) -> str:
    """
    Classify the discount as a hedged status string, not a bare boolean.

    A raw True/False for "undervalued" reads as more certain than a
    low-confidence, aggregate-cost-guide-derived estimate actually is, so
    this always carries the confidence level in the label.
    """
    if discount_pct >= 0.05:
        direction = "directionally_undervalued"
    elif discount_pct <= -0.05:
        direction = "directionally_overpriced"
    else:
        direction = "approximately_fair_value"

    return f"{direction}_{benchmark_confidence}_confidence"


def build_benchmark_result(
    comparable_components: dict[str, float],
    actual_estimated_trip_cost_usd: float,
    benchmark_method: str,
    benchmark_confidence: BenchmarkConfidence,
) -> dict[str, Any]:
    """
    Build the benchmark: section fields for a candidate YAML.

    Does not set ready_for_scoring — overall scoring readiness depends on
    every component (hotel validation, activity validation, entry
    requirements, etc.), not benchmarking alone, and is determined by
    scripts/check_scoring_readiness.py.
    """
    if benchmark_confidence not in ("low", "medium", "high"):
        raise ValueError("benchmark_confidence must be one of: low, medium, high.")

    fair_value_estimate_usd = estimate_fair_value(comparable_components)
    estimated_discount_pct = calculate_discount_pct(fair_value_estimate_usd, actual_estimated_trip_cost_usd)

    return {
        "fair_value_estimate_usd": fair_value_estimate_usd,
        "estimated_discount_pct": estimated_discount_pct,
        "benchmark_method": benchmark_method,
        "benchmark_confidence": benchmark_confidence,
        "undervalued_flag": classify_undervalued_flag(estimated_discount_pct, benchmark_confidence),
        "ready_for_benchmarking": True,
        "comparable_components": dict(comparable_components),
    }
