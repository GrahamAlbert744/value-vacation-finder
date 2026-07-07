"""Tests for scripts/validate_candidate_schema.py."""

from __future__ import annotations

import copy

import pytest
import yaml

from validate_candidate_schema import (
    DEFAULT_SAMPLE_CANDIDATE_PATH,
    load_yaml,
    validate_candidate,
    validate_cost_formula,
    validate_mvp_values,
    validate_required_fields,
    validate_trip_length,
)


def test_sample_candidate_passes_validation():
    errors = validate_candidate(DEFAULT_SAMPLE_CANDIDATE_PATH)
    assert errors == []


def test_sample_candidate_data_loads_as_dict():
    data = load_yaml(DEFAULT_SAMPLE_CANDIDATE_PATH)
    assert isinstance(data, dict)
    assert "candidate" in data


@pytest.fixture()
def sample_data():
    return load_yaml(DEFAULT_SAMPLE_CANDIDATE_PATH)


def test_missing_required_field_is_caught(sample_data):
    mutated = copy.deepcopy(sample_data)
    del mutated["origin"]["airport_code"]

    errors = validate_required_fields(mutated)
    assert any("origin.airport_code" in error for error in errors)


def test_wrong_traveler_count_is_caught(sample_data):
    mutated = copy.deepcopy(sample_data)
    mutated["travelers"]["adults"] = 3

    errors = validate_mvp_values(mutated)
    assert any("travelers.adults" in error for error in errors)


def test_trip_length_outside_range_is_caught(sample_data):
    mutated = copy.deepcopy(sample_data)
    mutated["dates"]["trip_length_days"] = 30

    errors = validate_trip_length(mutated)
    assert any("trip_length_days must be between 7 and 21" in error for error in errors)


def test_cost_formula_mismatch_is_caught(sample_data):
    mutated = copy.deepcopy(sample_data)
    mutated["cost_estimate"]["actual_estimated_trip_cost_usd"] = 1.0

    errors = validate_cost_formula(mutated)
    assert any("Cost formula mismatch" in error for error in errors)
