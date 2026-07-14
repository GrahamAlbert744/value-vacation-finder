"""
Guardrail tests for the project's most important policy rule:

    no_final_score_without_benchmark_logic
    no_undervalued_label_without_fair_value_estimate

See references/project_full_instructions.md, Sections 8 and 9.

price_undervaluation scoring is real as of Phase 7 (once a row has a built
benchmark it scores using config/scoring_weights.yaml's bands, scaled by
benchmark_confidence). These tests make sure that unblocking stayed
deliberate and bounded: still blocked with no benchmark, never scores
above what the confidence multiplier allows, and the overall final
score/tier/undervalued label stays blocked regardless, because
attractions_activity_value stays unimplemented and the MVP policy switch
in scoring_weights.yaml is still off.
"""

from __future__ import annotations

import pytest

from draft_component_scoring import (
    blocking_reasons,
    final_total_score_is_blocked,
    read_first_row,
    run_draft_component_scoring,
    score_attractions_activity_value,
    score_price_undervaluation,
    DEFAULT_CSV_PATH,
)
from value_vacation_finder.benchmarking.fair_value import (
    BENCHMARKING_STATUS_NOT_READY,
    build_benchmark_result,
    calculate_discount_pct,
    classify_undervalued_flag,
    estimate_fair_value,
)


@pytest.fixture()
def sample_row():
    return read_first_row(DEFAULT_CSV_PATH)


def test_price_undervaluation_blocked_without_benchmark(sample_row):
    """The sample candidate has no built benchmark, so it must stay blocked."""
    assert sample_row["benchmark_method"] == "not_yet_built"

    result = score_price_undervaluation(sample_row)
    assert result["score"] is None
    assert result["status"] == "not_ready"


def test_price_undervaluation_scores_when_benchmark_ready():
    row = {
        "benchmark_method": "published_cost_index_peer_average_v1",
        "estimated_discount_pct": "0.1804",
        "benchmark_confidence": "low",
    }

    result = score_price_undervaluation(row)

    assert result["status"] == "draft_ready_with_caveats"
    # "good" band is 20 points; low confidence applies a 0.5 multiplier.
    assert result["score"] == 10


def test_price_undervaluation_never_exceeds_confidence_scaled_max():
    """A low-confidence benchmark can never score as high as a high-confidence one."""
    low_row = {
        "benchmark_method": "x",
        "estimated_discount_pct": "0.35",
        "benchmark_confidence": "low",
    }
    high_row = {
        "benchmark_method": "x",
        "estimated_discount_pct": "0.35",
        "benchmark_confidence": "high",
    }

    low_result = score_price_undervaluation(low_row)
    high_result = score_price_undervaluation(high_row)

    assert low_result["score"] < high_result["score"]
    assert high_result["score"] == 30  # exceptional band, full confidence


def test_price_undervaluation_blocked_if_confidence_missing():
    row = {"benchmark_method": "x", "estimated_discount_pct": "0.20"}

    result = score_price_undervaluation(row)
    assert result["score"] is None
    assert result["status"] == "not_ready"


def test_attractions_activity_value_is_always_blocked(sample_row):
    result = score_attractions_activity_value(sample_row)
    assert result["score"] is None
    assert result["status"] == "not_ready"


def test_final_total_score_stays_blocked_by_mvp_policy_switch():
    """
    Even an all-ready result set stays blocked, because
    config/scoring_weights.yaml mvp_scoring_policy.allow_final_total_score
    is a project-level switch this script never flips on its own.
    """
    results = [{"component": "anything", "score": 100, "status": "draft_ready", "blocking_flags": []}]
    assert final_total_score_is_blocked(results) is True
    assert any("allow_final_total_score is false" in reason for reason in blocking_reasons(results))


def test_final_total_score_blocked_by_not_ready_component():
    results = [
        {
            "component": "attractions_activity_value",
            "score": None,
            "status": "not_ready",
            "reason": "Activity source validation is not available yet.",
            "blocking_flags": [],
        }
    ]
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


def test_estimate_fair_value_refuses_missing_components():
    with pytest.raises(ValueError):
        estimate_fair_value({})

    with pytest.raises(ValueError):
        estimate_fair_value({"flights_usd": 100.0})


def test_estimate_fair_value_sums_real_components():
    total = estimate_fair_value(
        {"flights_usd": 1500.0, "hotel_usd": 1540.0, "activities_usd": 770.0, "food_transport_usd": 1430.0}
    )
    assert total == 5240.0


def test_calculate_discount_pct_matches_expected_value():
    assert calculate_discount_pct(5240.0, 4294.94) == pytest.approx(0.1804, abs=0.0001)


def test_classify_undervalued_flag_always_carries_confidence():
    flag = classify_undervalued_flag(0.18, "low")
    assert flag.endswith("_low_confidence")
    assert "undervalued" in flag


def test_build_benchmark_result_rejects_invalid_confidence():
    with pytest.raises(ValueError):
        build_benchmark_result(
            {"flights_usd": 1.0, "hotel_usd": 1.0, "activities_usd": 1.0, "food_transport_usd": 1.0},
            2.0,
            "method",
            "very_confident",  # not a valid confidence level
        )
