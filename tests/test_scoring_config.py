"""Tests for scripts/validate_scoring_config.py and scripts/check_scoring_readiness.py."""

from __future__ import annotations

import copy

import pytest
import yaml

from check_scoring_readiness import check_scoring_readiness, read_first_row, DEFAULT_CSV_PATH
from validate_scoring_config import (
    DEFAULT_SCORING_CONFIG_PATH,
    load_yaml,
    validate_benchmark_controls,
    validate_scoring_config,
)


def test_scoring_config_passes_validation():
    errors = validate_scoring_config(DEFAULT_SCORING_CONFIG_PATH)
    assert errors == []


def test_scoring_config_data_loads_as_dict():
    data = load_yaml(DEFAULT_SCORING_CONFIG_PATH)
    assert isinstance(data, dict)
    assert "categories" in data


def test_allow_final_total_score_true_is_rejected():
    """
    If someone flips allow_final_total_score to true without building
    benchmarking, the validator must catch it (no_final_score_without_benchmark_logic).
    """
    data = load_yaml(DEFAULT_SCORING_CONFIG_PATH)
    mutated = copy.deepcopy(data)
    mutated["mvp_scoring_policy"]["allow_final_total_score"] = True

    errors = validate_benchmark_controls(mutated)
    assert any("allow_final_total_score must be false" in error for error in errors)


def test_allow_undervalued_label_true_is_rejected():
    data = load_yaml(DEFAULT_SCORING_CONFIG_PATH)
    mutated = copy.deepcopy(data)
    mutated["mvp_scoring_policy"]["allow_undervalued_label"] = True

    errors = validate_benchmark_controls(mutated)
    assert any("allow_undervalued_label must be false" in error for error in errors)


def test_scoring_readiness_reports_price_undervaluation_not_ready():
    row = read_first_row(DEFAULT_CSV_PATH)
    results = check_scoring_readiness(row)

    price_result = next(r for r in results if r["component"] == "price_undervaluation")
    assert price_result["status"] == "not_ready"
