"""
Build a processed-style vacation candidates CSV from candidate YAML input.

For Phase 5.9, this script reads one GitHub-safe sample candidate YAML,
validates that it has the expected MVP schema, flattens it into one row,
and writes a processed-style CSV to a GitHub-safe reference folder.

This is not yet the final production processed dataset builder.
It is a safe MVP bridge from:
    candidate YAML -> validated candidate -> flattened row -> CSV dataset
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import Any

from flatten_candidate_to_row import flatten_candidate, load_yaml
from validate_candidate_schema import validate_candidate


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_INPUT_PATH = (
    PROJECT_ROOT
    / "references"
    / "sample_candidates"
    / "sample_lisbon_candidate.yaml"
)

DEFAULT_OUTPUT_PATH = (
    PROJECT_ROOT
    / "references"
    / "sample_processed"
    / "vacation_candidates_sample.csv"
)


def write_rows_to_csv(rows: list[dict[str, Any]], output_path: Path) -> None:
    """Write processed-style candidate rows to a CSV file."""
    if not rows:
        raise ValueError("No rows were provided for CSV output.")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(rows[0].keys())

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build_processed_candidate_row(input_path: Path) -> dict[str, Any]:
    """Validate and flatten one candidate YAML into one processed-style row."""
    validation_errors = validate_candidate(input_path)

    if validation_errors:
        error_text = "\n".join(f"- {error}" for error in validation_errors)
        raise ValueError(f"Candidate validation failed:\n{error_text}")

    candidate_data = load_yaml(input_path)
    row = flatten_candidate(candidate_data)

    return row


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Build a processed-style vacation candidates CSV."
    )

    parser.add_argument(
        "--input",
        type=str,
        default=str(DEFAULT_INPUT_PATH),
        help="Path to input candidate YAML file.",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=str(DEFAULT_OUTPUT_PATH),
        help="Path to output processed-style CSV file.",
    )

    return parser.parse_args()


def main() -> None:
    """Run the processed candidate CSV builder."""
    args = parse_args()

    input_path = Path(args.input)
    if not input_path.is_absolute():
        input_path = PROJECT_ROOT / input_path

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = PROJECT_ROOT / output_path

    print("Building processed-style vacation candidates CSV")
    print("------------------------------------------------")
    print(f"Input candidate YAML: {input_path}")
    print(f"Output CSV: {output_path}")

    row = build_processed_candidate_row(input_path)
    write_rows_to_csv([row], output_path)

    print("\nSUCCESS")
    print("-------")
    print(f"Wrote 1 processed-style candidate row to: {output_path}")
    print(f"Trip ID: {row.get('trip_id')}")
    print(f"Destination: {row.get('destination_city')}, {row.get('destination_country')}")
    print(f"Ready for scoring: {row.get('ready_for_scoring')}")
    print(f"Ready for benchmarking: {row.get('ready_for_benchmarking')}")


if __name__ == "__main__":
    main()