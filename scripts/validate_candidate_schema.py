"""
Validate a structured vacation candidate YAML file.

This script checks whether a manually created vacation_candidate record
contains the minimum required sections and fields needed before later
cleaning, scoring, benchmarking, or reporting.

It is intentionally simple for the MVP.
"""

from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_CANDIDATE_PATH = (
    PROJECT_ROOT
    / "data"
    / "interim"
    / "manual_candidates"
    / "lisbon_candidate_001.yaml"
)


REQUIRED_SECTIONS = [
    "candidate",
    "origin",
    "destination",
    "dates",
    "travelers",
    "flight",
    "lodging",
    "attractions",
    "risk",
    "cost_estimate",
    "benchmark",
    "data_quality_flags",
    "candidate_decision",
]


REQUIRED_FIELDS = {
    "candidate": [
        "trip_id",
        "search_run_id",
        "candidate_status",
        "destination_slug",
    ],
    "origin": [
        "city",
        "airport_code",
    ],
    "destination": [
        "city",
        "country",
        "airport_code",
    ],
    "dates": [
        "departure_date",
        "return_date",
        "trip_length_days",
        "trip_length_valid",
    ],
    "travelers": [
        "adults",
        "children",
        "traveler_count",
    ],
    "flight": [
        "source",
        "route",
        "estimated_total_flight_cost_usd",
    ],
    "lodging": [
        "source",
        "hotel_name",
        "total_price_usd",
    ],
    "attractions": [
        "estimated_attraction_cost_total_usd",
    ],
    "risk": [
        "advisory_decision",
        "risk_flag",
    ],
    "cost_estimate": [
        "actual_estimated_trip_cost_usd",
    ],
    "benchmark": [
        "benchmark_method",
    ],
    "candidate_decision": [
        "mvp_candidate_usable",
        "ready_for_scoring",
    ],
}


EXPECTED_MVP_VALUES = {
    ("origin", "airport_code"): "BOS",
    ("destination", "airport_code"): "LIS",
    ("travelers", "adults"): 2,
    ("travelers", "children"): 0,
    ("dates", "trip_length_valid"): True,
}


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file and return a dictionary."""
    if not path.exists():
        raise FileNotFoundError(f"Candidate file not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError("YAML file did not load as a dictionary.")

    return data


def is_missing(value: Any) -> bool:
    """Return True if a value should count as missing."""
    return value is None or value == ""


def validate_required_sections(data: dict[str, Any]) -> list[str]:
    """Check that all required top-level sections exist."""
    errors = []

    for section in REQUIRED_SECTIONS:
        if section not in data:
            errors.append(f"Missing required section: {section}")

    return errors


def validate_required_fields(data: dict[str, Any]) -> list[str]:
    """Check that required fields exist and are not blank."""
    errors = []

    for section, fields in REQUIRED_FIELDS.items():
        section_data = data.get(section)

        if not isinstance(section_data, dict):
            errors.append(f"Section is missing or not a dictionary: {section}")
            continue

        for field in fields:
            if field not in section_data:
                errors.append(f"Missing required field: {section}.{field}")
            elif is_missing(section_data[field]):
                errors.append(f"Required field is blank/null: {section}.{field}")

    return errors


def validate_mvp_values(data: dict[str, Any]) -> list[str]:
    """Check MVP-specific expectations such as BOS origin and 2 adults."""
    errors = []

    for (section, field), expected_value in EXPECTED_MVP_VALUES.items():
        actual_value = data.get(section, {}).get(field)

        if actual_value != expected_value:
            errors.append(
                f"Unexpected MVP value: {section}.{field} "
                f"expected {expected_value!r}, got {actual_value!r}"
            )

    return errors


def validate_trip_length(data: dict[str, Any]) -> list[str]:
    """Check that trip length is between 7 and 21 days."""
    errors = []

    trip_length = data.get("dates", {}).get("trip_length_days")

    if not isinstance(trip_length, int):
        errors.append("dates.trip_length_days must be an integer.")
        return errors

    if trip_length < 7 or trip_length > 21:
        errors.append(
            f"dates.trip_length_days must be between 7 and 21; got {trip_length}."
        )

    return errors


def validate_cost_formula(data: dict[str, Any]) -> list[str]:
    """Check whether total trip cost matches its components."""
    errors = []

    cost = data.get("cost_estimate", {})

    required_cost_fields = [
        "estimated_total_flight_cost_usd",
        "hotel_total_price_usd",
        "estimated_attraction_cost_total_usd",
        "estimated_food_transport_buffer_usd",
        "actual_estimated_trip_cost_usd",
    ]

    for field in required_cost_fields:
        if field not in cost:
            errors.append(f"Missing cost field: cost_estimate.{field}")
            return errors

    expected_total = (
        float(cost["estimated_total_flight_cost_usd"])
        + float(cost["hotel_total_price_usd"])
        + float(cost["estimated_attraction_cost_total_usd"])
        + float(cost["estimated_food_transport_buffer_usd"])
    )

    actual_total = float(cost["actual_estimated_trip_cost_usd"])

    if round(expected_total, 2) != round(actual_total, 2):
        errors.append(
            "Cost formula mismatch: "
            f"expected {expected_total:.2f}, got {actual_total:.2f}"
        )

    return errors


def validate_data_quality_flags(data: dict[str, Any]) -> list[str]:
    """Check that data_quality_flags exists and is a list."""
    errors = []

    flags = data.get("data_quality_flags")

    if not isinstance(flags, list):
        errors.append("data_quality_flags must be a list.")

    return errors


def validate_candidate(path: Path = DEFAULT_CANDIDATE_PATH) -> list[str]:
    """Run all validation checks and return a list of errors."""
    data = load_yaml(path)

    errors = []
    errors.extend(validate_required_sections(data))
    errors.extend(validate_required_fields(data))
    errors.extend(validate_mvp_values(data))
    errors.extend(validate_trip_length(data))
    errors.extend(validate_cost_formula(data))
    errors.extend(validate_data_quality_flags(data))

    return errors


def main() -> None:
    """Run validation from the command line."""
    print(f"Validating candidate file: {DEFAULT_CANDIDATE_PATH}")

    errors = validate_candidate(DEFAULT_CANDIDATE_PATH)

    if errors:
        print("\nVALIDATION FAILED")
        print("-----------------")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("\nVALIDATION PASSED")
    print("-----------------")
    print("Candidate has the required MVP schema fields.")


if __name__ == "__main__":
    main()