"""Tests for the candidate flattening + processed CSV build/check pipeline."""

from __future__ import annotations

import csv

from build_processed_candidate_csv import (
    DEFAULT_INPUT_PATH,
    DEFAULT_OUTPUT_PATH,
    build_processed_candidate_row,
)
from check_processed_candidate_csv import check_processed_csv
from flatten_candidate_to_row import flatten_candidate, load_yaml


def test_flatten_candidate_produces_expected_key_columns():
    data = load_yaml(DEFAULT_INPUT_PATH)
    row = flatten_candidate(data)

    for expected_column in [
        "trip_id",
        "destination_city",
        "estimated_total_flight_cost_usd",
        "actual_estimated_trip_cost_usd",
        "fair_value_estimate_usd",
        "data_quality_flags",
    ]:
        assert expected_column in row


def test_build_processed_candidate_row_matches_reference_csv():
    row = build_processed_candidate_row(DEFAULT_INPUT_PATH)

    with DEFAULT_OUTPUT_PATH.open("r", encoding="utf-8", newline="") as file:
        reference_row = next(csv.DictReader(file))

    assert row["trip_id"] == reference_row["trip_id"]
    assert row["destination_city"] == reference_row["destination_city"]


def test_reference_csv_passes_checks():
    errors = check_processed_csv(DEFAULT_OUTPUT_PATH)
    assert errors == []


def test_reference_csv_still_blocks_scoring_readiness():
    with DEFAULT_OUTPUT_PATH.open("r", encoding="utf-8", newline="") as file:
        row = next(csv.DictReader(file))

    assert row["ready_for_benchmarking"] in ("False", "false", "0", "")
    assert row["fair_value_estimate_usd"] in ("", "None")
