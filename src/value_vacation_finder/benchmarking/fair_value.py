"""
Fair-value benchmarking scaffold for Value Vacation Finder.

Section 9 of references/project_full_instructions.md defines the
benchmarking stage: no vacation candidate may be called "undervalued"
until real comparable-price benchmarking exists.

This module intentionally does not implement benchmarking. It gives the
rest of the codebase one canonical, importable "not built yet" status
and loud stubs, so a future implementation is a deliberate, visible change
rather than a silent addition of invented numbers.
"""

from __future__ import annotations

from typing import Any


BENCHMARKING_STATUS_NOT_READY: dict[str, Any] = {
    "fair_value_estimate_usd": None,
    "estimated_discount_pct": None,
    "benchmark_method": "not_yet_built",
    "undervalued_flag": None,
    "ready_for_benchmarking": False,
    "ready_for_scoring": False,
}


def estimate_fair_value(candidate_row: dict[str, Any]) -> float:
    """
    Estimate the fair-value USD cost of a comparable trip.

    Not implemented. Real benchmarking requires comparable flight, lodging,
    and activity price data that has not been captured yet (see
    references/project_full_instructions.md, Section 9). Do not fabricate
    a number here; raise instead so callers fail loudly.
    """
    raise NotImplementedError(
        "estimate_fair_value() is not implemented. Benchmarking requires "
        "real comparable price data (see Section 9 of "
        "references/project_full_instructions.md). Use "
        "BENCHMARKING_STATUS_NOT_READY instead of guessing a value."
    )


def calculate_discount_pct(
    fair_value_estimate_usd: float, actual_estimated_trip_cost_usd: float
) -> float:
    """
    Calculate estimated_discount_pct = (fair_value - actual_cost) / fair_value.

    Not implemented for the same reason as estimate_fair_value(): there is
    no verified fair_value_estimate_usd to calculate against yet.
    """
    raise NotImplementedError(
        "calculate_discount_pct() is not implemented. There is no verified "
        "fair_value_estimate_usd yet (see Section 9 of "
        "references/project_full_instructions.md)."
    )
