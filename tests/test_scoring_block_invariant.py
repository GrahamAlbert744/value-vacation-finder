"""
Guardrail tests for the project's most important policy rule:

    no_final_score_without_benchmark_logic
    no_undervalued_label_without_fair_value_estimate

See references/project_full_instructions.md, Sections 8 and 9.

These tests exist so that any future change to the scoring code that
accidentally starts producing a real final score, tier, or undervalued
label without benchmarking will fail loudly here, instead of silently
shipping a fabricated recommendation.
"""

from __future__ import annotations

import pytest

from draft_component_scoring import (
    final_total_score_is_blocked,
    read_first_row,
    run_draft_component_scoring,
    score_attractions_activity_value,
    score_price_undervaluation,
    DEFAULT_CSV_PATH,
)
from value_vacation_finder.benchmarking.fair_value import (
    BENCHMARKING_STATUS_NOT_READY,
    calculate_discount_pct,
    estimate_fair_value,
)


@pytest.fixture()
def sample_row():
    return read_first_row(DEFAULT_CSV_PATH)


def test_price_undervaluation_is_always_blocked(sample_row):
    result = score_price_undervaluation(sample_row)
    assert result["score"] is None
    assert result["status"] == "not_ready"


def test_attractions_activity_value_is_always_blocked(sample_row):
    result = score_attractions_activity_value(sample_row)
    assert result["score"] is None
    assert result["status"] == "not_ready"


def test_final_total_score_is_blocked_regardless_of_input():
    results = [{"component": "anything", "score": 100, "status": "draft_ready"}]
    assert final_total_score_is_blocked(results) is True


def test_run_draft_component_scoring_never_produces_a_total(sample_row):
    results = run_draft_component_scoring(sample_row)
    # No component result should carry a total/undervalued-style key.
    for result in results:
        assert "final_total_score" not in result
        assert "undervalued_flag" not in result
        assert "recommendation_tier" not in result


def test_benchmarking_status_not_ready_defaults():
    assert BENCHMARKING_STATUS_NOT_READY["fair_value_estimate_usd"] is None
    assert BENCHMARKING_STATUS_NOT_READY["benchmark_method"] == "not_yet_built"
    assert BENCHMARKING_STATUS_NOT_READY["ready_for_benchmarking"] is False
    assert BENCHMARKING_STATUS_NOT_READY["ready_for_scoring"] is False


def test_benchmarking_functions_refuse_to_guess():
    with pytest.raises(NotImplementedError):
        estimate_fair_value({})

    with pytest.raises(NotImplementedError):
        calculate_discount_pct(1000.0, 800.0)
