"""
Check scoring readiness for a processed-style vacation candidate CSV.

This script reads the sample processed candidate CSV and reports whether each
scoring component is ready, draft-ready with caveats, or not ready.

It does not calculate scores.
It does not rank candidates.
It does not call any travel connectors.
"""

from __future__ import annotations

import argparse
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


SCORING_COMPONENTS = [
    "price_undervaluation",
    "flight_quality_value",
    "lodging_quality_value",
    "destination_attractiveness",
    "attractions_activity_value",
    "safety_travel_advisory_risk",
    "practicality_friction",
]


def read_first_row(path: Path) -> dict[str, Any]:
    """Read the first row from a CSV file."""
    if not path.exists():
        raise FileNotFoundError(f"Candidate CSV not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        raise ValueError(f"No rows found in candidate CSV: {path}")

    return rows[0]


def is_blank(value: Any) -> bool:
    """Return True if a CSV value should count as missing."""
    return value is None or str(value).strip() == "" or str(value).strip().lower() == "none"


def has_flag(row: dict[str, Any], flag: str) -> bool:
    """Return True if the pipe-separated data_quality_flags field contains a flag."""
    flags = row.get("data_quality_flags", "")
    return flag in flags.split("|")


def check_required_fields(row: dict[str, Any], fields: list[str]) -> list[str]:
    """Return missing or blank required fields."""
    missing = []

    for field in fields:
        if field not in row:
            missing.append(f"{field} is missing")
        elif is_blank(row[field]):
            missing.append(f"{field} is blank")

    return missing


def check_price_undervaluation(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for price undervaluation scoring."""
    required_fields = [
        "actual_estimated_trip_cost_usd",
        "fair_value_estimate_usd",
        "estimated_discount_pct",
        "benchmark_method",
        "benchmark_confidence",
        "undervalued_flag",
    ]

    missing = check_required_fields(row, required_fields)

    if has_flag(row, "fair_value_estimate_missing"):
        missing.append("fair_value_estimate_missing flag is present")

    if row.get("benchmark_method") == "not_yet_built":
        missing.append("benchmark_method is not_yet_built")

    if missing:
        return {
            "component": "price_undervaluation",
            "status": "not_ready",
            "reason": "; ".join(missing),
        }

    if has_flag(row, "benchmark_confidence_low") or row.get("benchmark_confidence") == "low":
        return {
            "component": "price_undervaluation",
            "status": "draft_ready_with_caveats",
            "reason": "benchmark_confidence is low; treat discount estimate as directional only.",
        }

    return {
        "component": "price_undervaluation",
        "status": "ready",
        "reason": "Benchmark fields exist with medium/high confidence.",
    }


def check_flight_quality(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for draft flight quality/value scoring."""
    required_fields = [
        "flight_source",
        "flight_route",
        "flight_airline",
        "outbound_stops",
        "return_stops",
        "outbound_duration_minutes",
        "return_duration_minutes",
        "listed_flight_price_usd",
        "estimated_total_flight_cost_usd",
        "flight_price_interpretation",
        "assumed_price_basis_for_mvp",
    ]

    missing = check_required_fields(row, required_fields)

    caveats = []
    if has_flag(row, "flight_price_interpretation_needs_verification"):
        caveats.append("flight price interpretation needs verification")

    if missing:
        return {
            "component": "flight_quality_value",
            "status": "not_ready",
            "reason": "; ".join(missing),
        }

    if caveats:
        return {
            "component": "flight_quality_value",
            "status": "draft_ready_with_caveats",
            "reason": "; ".join(caveats),
        }

    return {
        "component": "flight_quality_value",
        "status": "draft_ready",
        "reason": "Required flight fields exist.",
    }


def check_lodging_quality(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for draft lodging quality/value scoring."""
    required_fields = [
        "lodging_source",
        "hotel_name",
        "hotel_total_price_usd",
        "hotel_nightly_price_usd",
        "hotel_guest_rating",
        "hotel_review_count",
        "lodging_validation_source",
        "tripadvisor_validation_status",
        "hotel_cancellation_policy_status",
        "hotel_location_quality_status",
    ]

    missing = check_required_fields(row, required_fields)

    caveats = []
    for flag in [
        "tripadvisor_validation_unavailable",
        "hotel_cancellation_policy_missing",
        "hotel_location_quality_missing",
        "expedia_inventory_only",
    ]:
        if has_flag(row, flag):
            caveats.append(flag)

    if missing:
        return {
            "component": "lodging_quality_value",
            "status": "not_ready",
            "reason": "; ".join(missing),
        }

    if caveats:
        return {
            "component": "lodging_quality_value",
            "status": "draft_ready_with_caveats",
            "reason": "; ".join(caveats),
        }

    return {
        "component": "lodging_quality_value",
        "status": "draft_ready",
        "reason": "Required lodging fields exist.",
    }


def check_destination_attractiveness(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for draft destination attractiveness scoring."""
    required_fields = [
        "destination_city",
        "destination_country",
        "destination_region",
        "departure_date",
        "return_date",
        "trip_length_days",
    ]

    missing = check_required_fields(row, required_fields)

    return {
        "component": "destination_attractiveness",
        "status": "not_ready" if missing else "draft_ready",
        "reason": "; ".join(missing) if missing else "Required destination fields exist.",
    }


def check_attractions_activity(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for attractions/activity value scoring."""
    required_fields = [
        "attractions_source",
        "estimated_attraction_cost_total_usd",
        "viator_validation_status",
        "activity_budget_method",
    ]

    missing = check_required_fields(row, required_fields)

    caveats = []
    for flag in [
        "viator_validation_unavailable",
        "activity_budget_placeholder_used",
    ]:
        if has_flag(row, flag):
            caveats.append(flag)

    if missing:
        return {
            "component": "attractions_activity_value",
            "status": "not_ready",
            "reason": "; ".join(missing),
        }

    if caveats:
        return {
            "component": "attractions_activity_value",
            "status": "not_ready",
            "reason": "; ".join(caveats),
        }

    return {
        "component": "attractions_activity_value",
        "status": "draft_ready",
        "reason": "Activity fields exist and are source-based.",
    }


def check_safety_risk(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for safety/travel advisory scoring."""
    required_fields = [
        "risk_source",
        "advisory_country",
        "us_travel_advisory_level",
        "us_travel_advisory_label",
        "advisory_decision",
        "risk_flag",
    ]

    missing = check_required_fields(row, required_fields)

    caveats = []
    if "canada_travel_advisory_level" not in row or is_blank(row.get("canada_travel_advisory_level")):
        caveats.append("Canadian travel advisory not yet implemented")

    if missing:
        return {
            "component": "safety_travel_advisory_risk",
            "status": "not_ready",
            "reason": "; ".join(missing),
        }

    if caveats:
        return {
            "component": "safety_travel_advisory_risk",
            "status": "draft_ready_with_caveats",
            "reason": "; ".join(caveats),
        }

    return {
        "component": "safety_travel_advisory_risk",
        "status": "draft_ready",
        "reason": "Required advisory fields exist.",
    }


def check_practicality_friction(row: dict[str, Any]) -> dict[str, Any]:
    """Check readiness for practicality/friction scoring."""
    required_fields = [
        "visa_entry_status",
        "passport_requirement_status",
        "traveler_citizenship_context",
        "language_or_logistics_notes",
    ]

    missing = check_required_fields(row, required_fields)

    return {
        "component": "practicality_friction",
        "status": "not_ready" if missing else "draft_ready",
        "reason": "; ".join(missing) if missing else "Required practicality fields exist.",
    }


def check_scoring_readiness(row: dict[str, Any]) -> list[dict[str, Any]]:
    """Run all scoring readiness checks."""
    return [
        check_price_undervaluation(row),
        check_flight_quality(row),
        check_lodging_quality(row),
        check_destination_attractiveness(row),
        check_attractions_activity(row),
        check_safety_risk(row),
        check_practicality_friction(row),
    ]


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Check scoring readiness for a processed-style vacation candidate CSV."
    )

    parser.add_argument(
        "--path",
        type=str,
        default=str(DEFAULT_CSV_PATH),
        help="Path to a processed-style candidate CSV. Defaults to the GitHub-safe sample.",
    )

    return parser.parse_args()


def main() -> None:
    """Run scoring readiness check from the command line."""
    args = parse_args()

    csv_path = Path(args.path)
    if not csv_path.is_absolute():
        csv_path = PROJECT_ROOT / csv_path

    print(f"Checking scoring readiness for: {csv_path}")

    row = read_first_row(csv_path)
    results = check_scoring_readiness(row)

    print("\nSCORING READINESS REPORT")
    print("------------------------")

    for result in results:
        print(f"{result['component']}: {result['status']}")
        print(f"  Reason: {result['reason']}")

    statuses = [result["status"] for result in results]

    print("\nSUMMARY")
    print("-------")
    print(f"ready: {statuses.count('ready')}")
    print(f"draft_ready: {statuses.count('draft_ready')}")
    print(f"draft_ready_with_caveats: {statuses.count('draft_ready_with_caveats')}")
    print(f"not_ready: {statuses.count('not_ready')}")

    if "not_ready" in statuses or "draft_ready_with_caveats" in statuses:
        print("\nDECISION")
        print("--------")
        print("Candidate is not ready for final total scoring.")
        print("Draft component scoring may proceed only where caveats are preserved.")
    else:
        print("\nDECISION")
        print("--------")
        print("Candidate appears ready for draft scoring.")


if __name__ == "__main__":
    main()