"""
Flatten a structured vacation candidate YAML file into a processed-style row.

This script converts the nested candidate YAML structure into a flat dictionary
that can later become a row in a processed vacation_candidates CSV.

For now, the script prints the flattened row and can optionally write a CSV.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SAMPLE_CANDIDATE_PATH = (
    PROJECT_ROOT
    / "references"
    / "sample_candidates"
    / "sample_lisbon_candidate.yaml"
)

DEFAULT_OUTPUT_PATH = (
    PROJECT_ROOT
    / "references"
    / "sample_candidates"
    / "sample_lisbon_candidate_flattened.csv"
)


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file and return a dictionary."""
    if not path.exists():
        raise FileNotFoundError(f"Candidate file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError("YAML file did not load as a dictionary.")

    return data


def get_nested(data: dict[str, Any], *keys: str, default: Any = None) -> Any:
    """Safely retrieve a nested value from a dictionary."""
    current: Any = data

    for key in keys:
        if not isinstance(current, dict):
            return default
        current = current.get(key, default)

    return current


def flags_to_string(flags: Any) -> str:
    """Convert data quality flags list to a pipe-separated string."""
    if flags is None:
        return ""

    if isinstance(flags, list):
        return "|".join(str(flag) for flag in flags)

    return str(flags)


def has_flag(data: dict[str, Any], flag: str) -> bool:
    """Return True if the candidate has a specific data quality flag."""
    flags = data.get("data_quality_flags", [])

    if not isinstance(flags, list):
        return False

    return flag in flags


def flatten_candidate(data: dict[str, Any]) -> dict[str, Any]:
    """Flatten a nested candidate YAML dictionary into one row."""
    row = {
        # Identity
        "trip_id": get_nested(data, "candidate", "trip_id"),
        "search_run_id": get_nested(data, "candidate", "search_run_id"),
        "candidate_status": get_nested(data, "candidate", "candidate_status"),
        "destination_slug": get_nested(data, "candidate", "destination_slug"),
        "created_at": get_nested(data, "candidate", "created_at"),

        # Origin / destination
        "origin_city": get_nested(data, "origin", "city"),
        "origin_airport": get_nested(data, "origin", "airport_code"),
        "origin_country": get_nested(data, "origin", "country"),
        "destination_city": get_nested(data, "destination", "city"),
        "destination_country": get_nested(data, "destination", "country"),
        "destination_airport": get_nested(data, "destination", "airport_code"),
        "destination_region": get_nested(data, "destination", "region"),
        "destination_group": get_nested(data, "destination", "destination_group"),

        # Dates / travelers
        "departure_date": get_nested(data, "dates", "departure_date"),
        "return_date": get_nested(data, "dates", "return_date"),
        "trip_length_days": get_nested(data, "dates", "trip_length_days"),
        "trip_length_valid": get_nested(data, "dates", "trip_length_valid"),
        "adults": get_nested(data, "travelers", "adults"),
        "children": get_nested(data, "travelers", "children"),
        "traveler_count": get_nested(data, "travelers", "traveler_count"),

        # Flight
        "flight_source": get_nested(data, "flight", "source"),
        "flight_route": get_nested(data, "flight", "route"),
        "flight_airline": get_nested(data, "flight", "airline"),
        "outbound_stops": get_nested(data, "flight", "outbound_stops"),
        "return_stops": get_nested(data, "flight", "return_stops"),
        "outbound_duration_minutes": get_nested(data, "flight", "outbound_duration_minutes"),
        "return_duration_minutes": get_nested(data, "flight", "return_duration_minutes"),
        "listed_flight_price_usd": get_nested(data, "flight", "listed_price_usd"),
        "flight_price_interpretation": get_nested(data, "flight", "price_interpretation"),
        "assumed_price_basis_for_mvp": get_nested(data, "flight", "assumed_price_basis_for_mvp"),
        "estimated_total_flight_cost_usd": get_nested(data, "flight", "estimated_total_flight_cost_usd"),
        "flight_quality_assessment": get_nested(data, "flight", "flight_quality_assessment"),

        # Lodging
        "lodging_source": get_nested(data, "lodging", "source"),
        "hotel_name": get_nested(data, "lodging", "hotel_name"),
        "hotel_guest_rating": get_nested(data, "lodging", "guest_rating"),
        "hotel_review_count": get_nested(data, "lodging", "review_count"),
        "hotel_star_rating": get_nested(data, "lodging", "star_rating"),
        "hotel_nightly_price_usd": get_nested(data, "lodging", "nightly_price_usd"),
        "hotel_total_price_usd": get_nested(data, "lodging", "total_price_usd"),
        "lodging_quality_assessment": get_nested(data, "lodging", "lodging_quality_assessment"),
        "lodging_validation_source": get_nested(data, "lodging", "validation_source"),
        "tripadvisor_validation_status": get_nested(data, "lodging", "tripadvisor_validation_status"),
        "hotel_cancellation_policy_status": get_nested(data, "lodging", "cancellation_policy_status"),
        "hotel_location_quality_status": get_nested(data, "lodging", "location_quality_status"),

        # Attractions
        "attractions_source": get_nested(data, "attractions", "source"),
        "viator_validation_status": get_nested(data, "attractions", "viator_validation_status"),
        "estimated_attraction_cost_per_person_usd": get_nested(
            data, "attractions", "estimated_attraction_cost_per_person_usd"
        ),
        "estimated_attraction_cost_total_usd": get_nested(
            data, "attractions", "estimated_attraction_cost_total_usd"
        ),
        "activity_budget_method": get_nested(data, "attractions", "activity_budget_method"),

        # Risk
        "risk_source": get_nested(data, "risk", "source"),
        "advisory_country": get_nested(data, "risk", "country"),
        "us_travel_advisory_level": get_nested(data, "risk", "us_travel_advisory_level"),
        "us_travel_advisory_label": get_nested(data, "risk", "advisory_label"),
        "advisory_decision": get_nested(data, "risk", "advisory_decision"),
        "risk_flag": get_nested(data, "risk", "risk_flag"),
        "rejection_reason": get_nested(data, "risk", "rejection_reason"),

        # Costs
        "cost_estimate_flight_usd": get_nested(data, "cost_estimate", "estimated_total_flight_cost_usd"),
        "cost_estimate_hotel_usd": get_nested(data, "cost_estimate", "hotel_total_price_usd"),
        "cost_estimate_attractions_usd": get_nested(
            data, "cost_estimate", "estimated_attraction_cost_total_usd"
        ),
        "estimated_food_transport_buffer_usd": get_nested(
            data, "cost_estimate", "estimated_food_transport_buffer_usd"
        ),
        "actual_estimated_trip_cost_usd": get_nested(
            data, "cost_estimate", "actual_estimated_trip_cost_usd"
        ),
        "cost_estimate_status": get_nested(data, "cost_estimate", "cost_estimate_status"),

        # Benchmark
        "fair_value_estimate_usd": get_nested(data, "benchmark", "fair_value_estimate_usd"),
        "estimated_discount_pct": get_nested(data, "benchmark", "estimated_discount_pct"),
        "benchmark_method": get_nested(data, "benchmark", "benchmark_method"),
        "undervalued_flag": get_nested(data, "benchmark", "undervalued_flag"),

        # Candidate decision
        "mvp_candidate_usable": get_nested(data, "candidate_decision", "mvp_candidate_usable"),
        "ready_for_scoring": get_nested(data, "candidate_decision", "ready_for_scoring"),
        "ready_for_benchmarking": get_nested(data, "candidate_decision", "ready_for_benchmarking"),
        "candidate_summary": get_nested(data, "candidate_decision", "summary"),

        # Data quality
        "data_quality_flags": flags_to_string(data.get("data_quality_flags")),
        "has_flight_price_uncertainty": has_flag(
            data, "flight_price_interpretation_needs_verification"
        ),
        "has_missing_hotel_validation": has_flag(
            data, "tripadvisor_validation_unavailable"
        ),
        "has_placeholder_activity_budget": has_flag(
            data, "activity_budget_placeholder_used"
        ),
        "has_missing_benchmark": has_flag(
            data, "fair_value_estimate_missing"
        ),
    }

    return row


def write_csv(row: dict[str, Any], output_path: Path) -> None:
    """Write one flattened row to a CSV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(row.keys()))
        writer.writeheader()
        writer.writerow(row)


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Flatten a vacation candidate YAML file into a CSV-style row."
    )

    parser.add_argument(
        "--path",
        type=str,
        default=str(DEFAULT_SAMPLE_CANDIDATE_PATH),
        help="Path to candidate YAML file.",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=str(DEFAULT_OUTPUT_PATH),
        help="Path for output CSV file.",
    )

    parser.add_argument(
        "--write-csv",
        action="store_true",
        help="Write flattened row to CSV.",
    )

    return parser.parse_args()


def main() -> None:
    """Run the flattening script."""
    args = parse_args()

    candidate_path = Path(args.path)
    if not candidate_path.is_absolute():
        candidate_path = PROJECT_ROOT / candidate_path

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path

    data = load_yaml(candidate_path)
    row = flatten_candidate(data)

    print("Flattened candidate row")
    print("-----------------------")
    for key, value in row.items():
        print(f"{key}: {value}")

    if args.write_csv:
        write_csv(row, output_path)
        print(f"\nWrote CSV to: {output_path}")


if __name__ == "__main__":
    main()