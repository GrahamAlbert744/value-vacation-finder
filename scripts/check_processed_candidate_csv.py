"""
Check the processed-style vacation candidates sample CSV.

This script is a lightweight quality check for Phase 5.10.

It verifies that:
1. The sample processed CSV exists.
2. The CSV has exactly one sample row.
3. Required columns exist.
4. Key values match the expected Lisbon sample candidate.
5. Data-quality flags were preserved.
6. The candidate is not incorrectly marked as ready for scoring or benchmarking.
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


REQUIRED_COLUMNS = [
    "trip_id",
    "search_run_id",
    "candidate_status",
    "origin_city",
    "origin_airport",
    "destination_city",
    "destination_country",
    "destination_airport",
    "departure_date",
    "return_date",
    "trip_length_days",
    "adults",
    "traveler_count",
    "flight_source",
    "lodging_source",
    "hotel_name",
    "attractions_source",
    "risk_source",
    "actual_estimated_trip_cost_usd",
    "benchmark_method",
    "ready_for_scoring",
    "ready_for_benchmarking",
    "data_quality_flags",
    "has_flight_price_uncertainty",
    "has_missing_hotel_validation",
    "has_placeholder_activity_budget",
    "has_missing_benchmark",
]


EXPECTED_VALUES = {
    "trip_id": "sample_trip_20261005_lisbon_001",
    "origin_airport": "BOS",
    "destination_city": "Lisbon",
    "destination_country": "Portugal",
    "destination_airport": "LIS",
    "departure_date": "2026-10-05",
    "return_date": "2026-10-16",
    "adults": "2",
    "traveler_count": "2",
    "benchmark_method": "not_yet_built",
    "ready_for_scoring": "False",
    "ready_for_benchmarking": "False",
}


REQUIRED_FLAGS = [
    "flight_price_interpretation_needs_verification",
    "tripadvisor_validation_unavailable",
    "viator_validation_unavailable",
    "activity_budget_placeholder_used",
    "fair_value_estimate_missing",
]


def read_csv_rows(path: Path) -> list[dict[str, Any]]:
    """Read CSV rows into a list of dictionaries."""
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return rows


def check_required_columns(row: dict[str, Any]) -> list[str]:
    """Check that required columns exist."""
    errors = []

    for column in REQUIRED_COLUMNS:
        if column not in row:
            errors.append(f"Missing required column: {column}")

    return errors


def check_expected_values(row: dict[str, Any]) -> list[str]:
    """Check that key sample values match expectations."""
    errors = []

    for column, expected_value in EXPECTED_VALUES.items():
        actual_value = row.get(column)

        if actual_value != expected_value:
            errors.append(
                f"Unexpected value for {column}: "
                f"expected {expected_value!r}, got {actual_value!r}"
            )

    return errors


def check_required_flags(row: dict[str, Any]) -> list[str]:
    """Check that required data-quality flags were preserved."""
    errors = []

    flags_text = row.get("data_quality_flags", "")

    for flag in REQUIRED_FLAGS:
        if flag not in flags_text:
            errors.append(f"Missing required data-quality flag: {flag}")

    return errors


def check_boolean_flag_values(row: dict[str, Any]) -> list[str]:
    """Check derived boolean data-quality fields."""
    errors = []

    expected_boolean_flags = {
        "has_flight_price_uncertainty": "True",
        "has_missing_hotel_validation": "True",
        "has_placeholder_activity_budget": "True",
        "has_missing_benchmark": "True",
    }

    for column, expected_value in expected_boolean_flags.items():
        actual_value = row.get(column)

        if actual_value != expected_value:
            errors.append(
                f"Unexpected value for {column}: "
                f"expected {expected_value!r}, got {actual_value!r}"
            )

    return errors


def check_processed_csv(path: Path = DEFAULT_CSV_PATH) -> list[str]:
    """Run all processed CSV checks and return errors."""
    rows = read_csv_rows(path)

    errors = []

    if len(rows) != 1:
        errors.append(f"Expected exactly 1 row, found {len(rows)}.")
        return errors

    row = rows[0]

    errors.extend(check_required_columns(row))
    errors.extend(check_expected_values(row))
    errors.extend(check_required_flags(row))
    errors.extend(check_boolean_flag_values(row))

    return errors


def main() -> None:
    """Run the processed candidate CSV check."""
    print(f"Checking processed candidate CSV: {DEFAULT_CSV_PATH}")

    errors = check_processed_csv(DEFAULT_CSV_PATH)

    if errors:
        print("\nCHECK FAILED")
        print("------------")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("\nCHECK PASSED")
    print("------------")
    print("Processed candidate sample CSV has the expected structure and values.")


if __name__ == "__main__":
    main()