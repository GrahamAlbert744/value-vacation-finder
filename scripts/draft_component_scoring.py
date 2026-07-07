"""
Draft component scoring skeleton for Value Vacation Finder.

This script contains early scoring functions for individual vacation-score
components. It does NOT produce a final total score, final recommendation tier,
or undervalued label.

Reason:
Benchmarking and fair-value estimation have not been implemented yet.

Phase 6.6 goal:
- Create draft component scoring function skeletons.
- Allow limited draft scoring where data is available.
- Preserve caveats.
- Block final scoring.
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_CSV_PATH = (
    PROJECT_ROOT
    / "references"
    / "sample_processed"
    / "vacation_candidates_sample.csv"
)


def read_first_row(path: Path) -> dict[str, Any]:
    """Read the first candidate row from a processed-style CSV."""
    if not path.exists():
        raise FileNotFoundError(f"Candidate CSV not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        raise ValueError(f"No candidate rows found in: {path}")

    return rows[0]


def to_float(value: Any, default: float | None = None) -> float | None:
    """Safely convert a value to float."""
    try:
        if value is None or str(value).strip() == "":
            return default
        return float(value)
    except ValueError:
        return default


def to_int(value: Any, default: int | None = None) -> int | None:
    """Safely convert a value to integer."""
    try:
        if value is None or str(value).strip() == "":
            return default
        return int(float(value))
    except ValueError:
        return default


def has_flag(row: dict[str, Any], flag: str) -> bool:
    """Check whether a data-quality flag is present."""
    flags = row.get("data_quality_flags", "")
    return flag in str(flags).split("|")


def score_price_undervaluation(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft placeholder for price undervaluation scoring.

    This should remain blocked until benchmark/fair-value logic exists.
    """
    return {
        "component": "price_undervaluation",
        "max_points": 30,
        "score": None,
        "status": "not_ready",
        "reason": "Fair-value benchmark is not built yet.",
        "blocking_flags": [
            flag
            for flag in ["fair_value_estimate_missing"]
            if has_flag(row, flag)
        ],
    }


def score_flight_quality_value(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft score for flight quality/value.

    This is intentionally simple and caveated.
    """
    score = 0
    caveats = []

    outbound_stops = to_int(row.get("outbound_stops"))
    return_stops = to_int(row.get("return_stops"))
    outbound_duration = to_int(row.get("outbound_duration_minutes"))
    return_duration = to_int(row.get("return_duration_minutes"))
    price = to_float(row.get("estimated_total_flight_cost_usd"))

    # Price reasonableness placeholder: 0 to 5
    if price is None:
        caveats.append("missing flight price")
    elif price <= 1500:
        score += 5
    elif price <= 2200:
        score += 3
    else:
        score += 1

    # Stop count: 0 to 4
    if outbound_stops is None or return_stops is None:
        caveats.append("missing stop count")
    elif outbound_stops == 0 and return_stops == 0:
        score += 4
    elif outbound_stops <= 1 and return_stops <= 1:
        score += 2
    else:
        score += 1

    # Duration reasonableness: 0 to 3
    if outbound_duration is None or return_duration is None:
        caveats.append("missing duration")
    elif outbound_duration <= 600 and return_duration <= 600:
        score += 3
    elif outbound_duration <= 900 and return_duration <= 900:
        score += 2
    else:
        score += 1

    # Fare quality / basic economy risk: 0 to 2
    if has_flag(row, "flight_price_interpretation_needs_verification"):
        score += 1
        caveats.append("flight price interpretation needs verification")
    else:
        score += 2

    # Schedule practicality placeholder: 0 to 1
    score += 1

    status = "draft_ready_with_caveats" if caveats else "draft_ready"

    return {
        "component": "flight_quality_value",
        "max_points": 15,
        "score": min(score, 15),
        "status": status,
        "reason": "; ".join(caveats) if caveats else "Draft flight score calculated.",
        "blocking_flags": [],
    }


def score_lodging_quality_value(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft score for lodging quality/value.

    This is intentionally conservative when validation is missing.
    """
    score = 0
    caveats = []

    nightly_price = to_float(row.get("hotel_nightly_price_usd"))
    guest_rating = to_float(row.get("hotel_guest_rating"))
    review_count = to_int(row.get("hotel_review_count"))

    # Price reasonableness: 0 to 5
    if nightly_price is None:
        caveats.append("missing nightly hotel price")
    elif nightly_price <= 150:
        score += 5
    elif nightly_price <= 250:
        score += 3
    else:
        score += 1

    # Guest rating: 0 to 4
    if guest_rating is None:
        caveats.append("missing guest rating")
    elif guest_rating >= 4.5:
        score += 4
    elif guest_rating >= 4.0:
        score += 3
    elif guest_rating >= 3.5:
        score += 2
    else:
        score += 1

    # Review count strength: 0 to 3
    if review_count is None:
        caveats.append("missing review count")
    elif review_count >= 1000:
        score += 3
    elif review_count >= 250:
        score += 2
    else:
        score += 1

    # Location quality: 0 to 3
    if has_flag(row, "hotel_location_quality_missing"):
        score += 1
        caveats.append("hotel location quality missing")
    else:
        score += 3

    # Cancellation policy: 0 to 2
    if has_flag(row, "hotel_cancellation_policy_missing"):
        score += 1
        caveats.append("hotel cancellation policy missing")
    else:
        score += 2

    # Independent validation: 0 to 2
    if has_flag(row, "tripadvisor_validation_unavailable"):
        caveats.append("Tripadvisor validation unavailable")
    else:
        score += 2

    # Amenities / room quality placeholder: 0 to 1
    score += 1

    if has_flag(row, "expedia_inventory_only"):
        caveats.append("Expedia inventory only")

    status = "draft_ready_with_caveats" if caveats else "draft_ready"

    return {
        "component": "lodging_quality_value",
        "max_points": 20,
        "score": min(score, 20),
        "status": status,
        "reason": "; ".join(caveats) if caveats else "Draft lodging score calculated.",
        "blocking_flags": [],
    }


def score_destination_attractiveness(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft placeholder score for destination attractiveness.

    This is intentionally simple until destination-level data is built.
    """
    destination_city = row.get("destination_city")
    destination_country = row.get("destination_country")
    trip_length = to_int(row.get("trip_length_days"))

    caveats = []

    if not destination_city or not destination_country:
        return {
            "component": "destination_attractiveness",
            "max_points": 10,
            "score": None,
            "status": "not_ready",
            "reason": "Missing destination city or country.",
            "blocking_flags": [],
        }

    score = 0

    # Seasonality placeholder
    score += 2

    # Culture/food/history placeholder
    score += 3

    # Ease of getting around placeholder
    score += 2

    # Fit for trip length
    if trip_length is not None and 7 <= trip_length <= 21:
        score += 1
    else:
        caveats.append("trip length missing or outside allowed range")

    # Personal interest / uniqueness placeholder
    score += 1

    status = "draft_ready_with_caveats" if caveats else "draft_ready"

    return {
        "component": "destination_attractiveness",
        "max_points": 10,
        "score": min(score, 10),
        "status": status,
        "reason": "; ".join(caveats) if caveats else "Draft destination score calculated.",
        "blocking_flags": [],
    }


def score_attractions_activity_value(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft placeholder for attractions/activity value.

    This remains blocked while Viator/source activity data is unavailable.
    """
    blocking_flags = []

    for flag in [
        "viator_validation_unavailable",
        "activity_budget_placeholder_used",
    ]:
        if has_flag(row, flag):
            blocking_flags.append(flag)

    return {
        "component": "attractions_activity_value",
        "max_points": 10,
        "score": None,
        "status": "not_ready",
        "reason": "Activity source validation is not available yet.",
        "blocking_flags": blocking_flags,
    }


def score_safety_travel_advisory_risk(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft score for safety/travel advisory risk.

    This uses U.S. advisory only for now and preserves the Canadian advisory caveat.
    """
    advisory_level = to_int(row.get("us_travel_advisory_level"))
    caveats = []

    if advisory_level is None:
        return {
            "component": "safety_travel_advisory_risk",
            "max_points": 10,
            "score": None,
            "status": "not_ready",
            "reason": "Missing U.S. travel advisory level.",
            "blocking_flags": [],
        }

    if advisory_level == 1:
        score = 10
    elif advisory_level == 2:
        score = 7
    elif advisory_level == 3:
        score = 2
        caveats.append("Level 3 advisory normally requires manual review")
    elif advisory_level >= 4:
        score = 0
        caveats.append("Level 4 advisory should trigger rejection")
    else:
        score = None
        caveats.append("Unexpected advisory level")

    if "canada_travel_advisory_level" not in row or not row.get("canada_travel_advisory_level"):
        caveats.append("Canadian travel advisory not yet implemented")

    status = "draft_ready_with_caveats" if caveats else "draft_ready"

    return {
        "component": "safety_travel_advisory_risk",
        "max_points": 10,
        "score": score,
        "status": status,
        "reason": "; ".join(caveats) if caveats else "Draft safety score calculated.",
        "blocking_flags": [],
    }


def score_practicality_friction(row: dict[str, Any]) -> dict[str, Any]:
    """
    Draft placeholder for practicality/friction.

    This remains blocked until visa/passport/logistics fields are structured.
    """
    required_fields = [
        "visa_entry_status",
        "passport_requirement_status",
        "traveler_citizenship_context",
        "language_or_logistics_notes",
    ]

    missing = [
        field
        for field in required_fields
        if field not in row or row.get(field) in [None, "", "None"]
    ]

    if missing:
        return {
            "component": "practicality_friction",
            "max_points": 5,
            "score": None,
            "status": "not_ready",
            "reason": "Missing practicality fields: " + ", ".join(missing),
            "blocking_flags": [],
        }

    return {
        "component": "practicality_friction",
        "max_points": 5,
        "score": 3,
        "status": "draft_ready_with_caveats",
        "reason": "Placeholder practicality score only.",
        "blocking_flags": [],
    }


def run_draft_component_scoring(row: dict[str, Any]) -> list[dict[str, Any]]:
    """Run all draft component scoring functions."""
    return [
        score_price_undervaluation(row),
        score_flight_quality_value(row),
        score_lodging_quality_value(row),
        score_destination_attractiveness(row),
        score_attractions_activity_value(row),
        score_safety_travel_advisory_risk(row),
        score_practicality_friction(row),
    ]


def final_total_score_is_blocked(results: list[dict[str, Any]]) -> bool:
    """
    Return True because final scoring is intentionally blocked during MVP.

    This function exists to make the blocking rule explicit.
    """
    return True


def main() -> None:
    """Run draft component scoring from the command line."""
    print(f"Reading candidate CSV: {DEFAULT_CSV_PATH}")

    row = read_first_row(DEFAULT_CSV_PATH)
    results = run_draft_component_scoring(row)

    print("\nDRAFT COMPONENT SCORING REPORT")
    print("------------------------------")

    for result in results:
        print(f"{result['component']}")
        print(f"  max_points: {result['max_points']}")
        print(f"  score: {result['score']}")
        print(f"  status: {result['status']}")
        print(f"  reason: {result['reason']}")
        if result["blocking_flags"]:
            print(f"  blocking_flags: {', '.join(result['blocking_flags'])}")

    print("\nFINAL SCORING STATUS")
    print("--------------------")

    if final_total_score_is_blocked(results):
        print("Final total score: BLOCKED")
        print("Recommendation tier: BLOCKED")
        print("Undervalued label: BLOCKED")
        print("Reason: Benchmark/fair-value logic is not implemented yet.")
    else:
        print("Final total score may be calculated.")


if __name__ == "__main__":
    main()