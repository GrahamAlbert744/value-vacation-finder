"""
Validate the Value Vacation Finder scoring configuration.

This script checks that config/scoring_weights.yaml has the required structure
before the project starts using it for scoring logic.

Phase 6.2 checks:
1. The scoring config YAML exists and loads.
2. The scoring system total_points equals 100.
3. Category weights sum to 100.
4. Required categories exist.
5. Required top-level sections exist.
6. Recommendation tiers exist and include expected labels.
7. MVP policy blocks final total scores and undervalued labels before benchmarking.
8. Categories that should require benchmarking/source validation are properly flagged.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[1]

DEFAULT_SCORING_CONFIG_PATH = PROJECT_ROOT / "config" / "scoring_weights.yaml"


REQUIRED_TOP_LEVEL_SECTIONS = [
    "scoring_system",
    "categories",
    "hard_rejection_rules",
    "recommendation_tiers",
    "mvp_scoring_policy",
]


REQUIRED_CATEGORIES = {
    "price_undervaluation": 30,
    "flight_quality_value": 15,
    "lodging_quality_value": 20,
    "destination_attractiveness": 10,
    "attractions_activity_value": 10,
    "safety_travel_advisory_risk": 10,
    "practicality_friction": 5,
}


REQUIRED_RECOMMENDATION_TIERS = [
    "exceptional_value",
    "strong_candidate",
    "worth_considering",
    "only_if_personally_exciting",
    "reject",
]


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a YAML file and return a dictionary."""
    if not path.exists():
        raise FileNotFoundError(f"Scoring config not found: {path}")

    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError("Scoring config did not load as a dictionary.")

    return data


def validate_top_level_sections(data: dict[str, Any]) -> list[str]:
    """Validate required top-level sections."""
    errors = []

    for section in REQUIRED_TOP_LEVEL_SECTIONS:
        if section not in data:
            errors.append(f"Missing top-level section: {section}")

    return errors


def validate_total_points(data: dict[str, Any]) -> list[str]:
    """Validate total points and category sum."""
    errors = []

    scoring_system = data.get("scoring_system", {})
    categories = data.get("categories", {})

    expected_total = scoring_system.get("total_points")

    if expected_total != 100:
        errors.append(
            f"scoring_system.total_points should be 100; got {expected_total!r}"
        )

    if not isinstance(categories, dict):
        errors.append("categories must be a dictionary.")
        return errors

    category_total = 0

    for category_name, category_config in categories.items():
        if not isinstance(category_config, dict):
            errors.append(f"Category is not a dictionary: {category_name}")
            continue

        points = category_config.get("points")

        if not isinstance(points, int):
            errors.append(f"Category points must be an integer: {category_name}")
            continue

        category_total += points

    if category_total != 100:
        errors.append(f"Category points should sum to 100; got {category_total}")

    return errors


def validate_required_categories(data: dict[str, Any]) -> list[str]:
    """Validate required categories and expected point values."""
    errors = []

    categories = data.get("categories", {})

    if not isinstance(categories, dict):
        errors.append("categories must be a dictionary.")
        return errors

    for category_name, expected_points in REQUIRED_CATEGORIES.items():
        if category_name not in categories:
            errors.append(f"Missing required category: {category_name}")
            continue

        actual_points = categories[category_name].get("points")

        if actual_points != expected_points:
            errors.append(
                f"Unexpected points for {category_name}: "
                f"expected {expected_points}, got {actual_points}"
            )

    return errors


def validate_category_required_fields(data: dict[str, Any]) -> list[str]:
    """Validate each category has minimum metadata."""
    errors = []

    categories = data.get("categories", {})

    if not isinstance(categories, dict):
        return ["categories must be a dictionary."]

    required_fields = ["points", "status", "description", "inputs_required"]

    for category_name, category_config in categories.items():
        for field in required_fields:
            if field not in category_config:
                errors.append(f"Missing {category_name}.{field}")

        inputs_required = category_config.get("inputs_required")
        if not isinstance(inputs_required, list):
            errors.append(f"{category_name}.inputs_required must be a list.")

    return errors


def validate_benchmark_controls(data: dict[str, Any]) -> list[str]:
    """Validate benchmark-dependent categories and MVP scoring policy."""
    errors = []

    categories = data.get("categories", {})
    price_config = categories.get("price_undervaluation", {})
    activity_config = categories.get("attractions_activity_value", {})
    mvp_policy = data.get("mvp_scoring_policy", {})

    if price_config.get("requires_benchmark") is not True:
        errors.append("price_undervaluation.requires_benchmark must be true.")

    if price_config.get("status") != "not_ready":
        errors.append("price_undervaluation.status should be not_ready.")

    if activity_config.get("requires_source_validation") is not True:
        errors.append("attractions_activity_value.requires_source_validation must be true.")

    if activity_config.get("status") != "not_ready":
        errors.append("attractions_activity_value.status should be not_ready.")

    if mvp_policy.get("allow_final_total_score") is not False:
        errors.append("mvp_scoring_policy.allow_final_total_score must be false.")

    if mvp_policy.get("allow_undervalued_label") is not False:
        errors.append("mvp_scoring_policy.allow_undervalued_label must be false.")

    return errors


def validate_recommendation_tiers(data: dict[str, Any]) -> list[str]:
    """Validate recommendation tiers exist and have score ranges."""
    errors = []

    tiers = data.get("recommendation_tiers", {})

    if not isinstance(tiers, dict):
        errors.append("recommendation_tiers must be a dictionary.")
        return errors

    for tier_name in REQUIRED_RECOMMENDATION_TIERS:
        if tier_name not in tiers:
            errors.append(f"Missing recommendation tier: {tier_name}")
            continue

        tier_config = tiers[tier_name]

        for field in ["min_score", "max_score", "label"]:
            if field not in tier_config:
                errors.append(f"Missing recommendation_tiers.{tier_name}.{field}")

    return errors


def validate_hard_rejection_rules(data: dict[str, Any]) -> list[str]:
    """Validate hard rejection rules exist."""
    errors = []

    hard_rejection_rules = data.get("hard_rejection_rules", {})
    reject_if = hard_rejection_rules.get("reject_if")

    if not isinstance(reject_if, list):
        errors.append("hard_rejection_rules.reject_if must be a list.")
        return errors

    required_rules = [
        "advisory_level_4",
        "destination_or_date_mismatch",
        "trip_length_outside_7_to_21_days",
        "traveler_count_mismatch",
        "entry_requirements_infeasible",
    ]

    for rule in required_rules:
        if rule not in reject_if:
            errors.append(f"Missing hard rejection rule: {rule}")

    return errors


def validate_scoring_config(path: Path = DEFAULT_SCORING_CONFIG_PATH) -> list[str]:
    """Run all scoring config validation checks."""
    data = load_yaml(path)

    errors = []
    errors.extend(validate_top_level_sections(data))
    errors.extend(validate_total_points(data))
    errors.extend(validate_required_categories(data))
    errors.extend(validate_category_required_fields(data))
    errors.extend(validate_benchmark_controls(data))
    errors.extend(validate_recommendation_tiers(data))
    errors.extend(validate_hard_rejection_rules(data))

    return errors


def main() -> None:
    """Run scoring config validation from the command line."""
    print(f"Validating scoring config: {DEFAULT_SCORING_CONFIG_PATH}")

    errors = validate_scoring_config(DEFAULT_SCORING_CONFIG_PATH)

    if errors:
        print("\nVALIDATION FAILED")
        print("-----------------")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("\nVALIDATION PASSED")
    print("-----------------")
    print("Scoring config has the expected MVP structure.")
    print("Category weights sum to 100.")
    print("MVP policy correctly blocks final scoring and undervalued labels.")


if __name__ == "__main__":
    main()