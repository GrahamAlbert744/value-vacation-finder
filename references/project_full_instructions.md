# Full Instructions for Value Vacation Finder

Below is the safe refresh, development, and operating workflow for a Python-based Value Vacation Finder decision-support system.

The bias of this project is toward:

- Small controlled connector captures
- Cached local raw notes
- Reproducible Python workflows
- Explicit search run IDs
- Run manifests
- File hashes
- Git commit tracking
- No silent score inflation
- No unverified live-data assumptions
- No blind booking recommendations
- Human review before any travel decision
- No final "undervalued vacation" label until fair-value benchmarking exists

---

# Project Purpose

Build a Python-based vacation decision-support system that helps Graham identify undervalued vacations from Boston.

The system should help evaluate:

1. Known-destination trips
2. Flexible-destination trips
3. Flight value
4. Lodging value
5. Attractions and tours value
6. Destination safety
7. Entry, passport, and visa friction
8. Total estimated trip cost
9. Fair-value benchmarks
10. Whether a vacation appears meaningfully underpriced versus comparable trips

The system does not automatically book travel.

The system does not update on a schedule.

The project only runs manually when Graham says he is interested in planning a vacation.

---

# Guiding Policy

```yaml
value_vacation_refresh_policy:
  principles:
    - preflight_local_repo_before_connector_capture
    - use_manual_run_only
    - preserve_raw_connector_outputs_locally
    - preserve_transformed_candidate_outputs
    - never_treat_sample_data_as_live_booking_advice
    - separate_sample_runs_from_live_runs
    - use_same_destination_same_dates_same_travelers_across_sources
    - use_run_ids_for_every_search_run
    - use_manifest_files_for_run_history
    - use_file_hashes_for_auditability
    - no_final_score_without_benchmark_logic
    - no_undervalued_label_without_fair_value_estimate
    - no_booking_recommendation_without_human_review
    - no_safety_clearance_without_travel_advisory_review
    - no_entry_assumption_without_us_and_canadian_passport_context
    - commit_code_docs_configs_and_small_sample_outputs_after_clean_milestones
    - keep_raw_connector_outputs_sensitive_files_and_api_keys_out_of_git
```

---

# Important Project Rules

```yaml
project_rules:
  project_name: value-vacation-finder
  project_path: C:\Users\graha\Documents\Data_Projects\value-vacation-finder
  conda_environment: value-vacation-finder

  origin:
    city: Boston
    airport: BOS

  travelers:
    adults: 2
    children: 0
    traveler_1:
      residency: USA
      citizenship: Canada
      passport_country: Canada
    traveler_2:
      residency: USA
      citizenship: USA
      passport_country: USA

  trip_length:
    min_days: 7
    max_days: 21

  primary_sources:
    flights:
      - Skyscanner
    lodging:
      - Expedia
      - Tripadvisor
    attractions:
      - Viator
      - Tripadvisor
      - Expedia
    safety:
      - Travel Advisory
      - U.S. travel advisory
      - Government of Canada travel advisory
    benchmarks:
      - historical/comparable flight prices
      - comparable hotel prices
      - comparable destination package costs

  outputs_are:
    - search_run_configs
    - raw_connector_notes
    - structured_candidates
    - processed_candidate_csvs
    - scoring_readiness_reports
    - draft_component_scores
    - benchmark_reports
    - shortlist_reports
    - run_manifests
    - human_review_notes

  outputs_are_not:
    - automatic bookings
    - guaranteed live prices
    - final travel advice without human review
    - final undervalued labels without benchmarks
    - safety guarantees
    - visa/legal guarantees
```

---

# 1. Preflight Stage

## Standard Preflight Commands

Every work session should start this way:

```bat
cd C:\Users\graha\Documents\Data_Projects\value-vacation-finder
conda activate value-vacation-finder
git status
```

Optional but recommended before code-heavy phases:

```bat
python --version
python -c "import yaml, csv, pathlib; print('imports ok')"
```

If tests exist:

```bat
pytest
```

## Preflight Checks

```yaml
preflight_checks:
  local_environment:
    check:
      - conda_environment_active
      - python_available
      - yaml_imports_successfully
      - project_root_is_correct
    expected_environment: value-vacation-finder

  git_state:
    check:
      - git_status_reviewed
      - branch_is_main_or_intended_feature_branch
      - no_uncommitted_work_unless_intentional
      - remote_origin_points_to_project_repo

  project_structure:
    required_directories:
      - config
      - data/raw
      - data/interim
      - data/processed
      - docs
      - prompts
      - references
      - reports
      - scripts
      - src
      - tests

  prior_outputs:
    check:
      - latest_phase_document_exists_if_prior_phase_completed
      - sample_candidate_exists_after_phase_5
      - processed_sample_csv_exists_after_phase_5_9
      - scoring_config_exists_after_phase_6_1
      - scoring_readiness_script_exists_after_phase_6_5
```

---

# 2. Connector Policy

## Connector Roles

```yaml
connector_policy:
  Travel Advisory:
    role: safety_and_country_risk
    use_first: true
    allowed_uses:
      - country_advisory_level
      - major risks
      - safety summary
      - continue_or_reject_decision

  Skyscanner:
    role: flight_search
    allowed_uses:
      - BOS_to_destination_round_trip_flights
      - prices
      - stops
      - duration
      - airline
      - departure_and_return_dates

  Expedia:
    role: lodging_and_possible_attractions
    allowed_uses:
      - hotel_prices
      - hotel_ratings
      - hotel_review_counts
      - total_stay_costs
      - amenities
      - cancellation_info_if_available

  Tripadvisor:
    role: hotel_quality_and_destination_validation
    allowed_uses:
      - hotel_quality_validation
      - review_strength
      - destination_quality
      - attraction_quality
      - location_quality

  Viator:
    role: attractions_and_tours
    allowed_uses:
      - activity_prices
      - tour_ratings
      - review_counts
      - representative_activity_budget
      - date_availability
```

## Connector Rules

```yaml
connector_rules:
  always_do:
    - check_travel_advisory_before_price_search
    - use_same_origin_destination_dates_and_travelers_across_sources
    - save_raw_connector_notes_locally
    - record_connector_failures_or_blocked_results
    - preserve_uncertainty_flags
    - use_placeholders_only_when_explicitly_labeled

  never_do:
    - mix_dates_across_sources
    - mix_destinations_across_sources
    - treat_expedia_only_hotel_data_as_market_benchmark
    - treat_blocked_tripadvisor_or_viator_search_as_negative_evidence
    - call_sample_outputs_live_booking_advice
    - call_candidate_undervalued_without_benchmark
```

---

# 3. Run Mode Policy

Every vacation run should have a run mode.

```yaml
run_modes:
  sample:
    meaning:
      - uses sanitized sample candidate data
      - uses GitHub-safe sample files
      - suitable_for_pipeline_testing_only
      - not suitable for booking decisions

  live_manual:
    meaning:
      - uses current manually captured connector outputs
      - uses one active search_run_id
      - uses same destination and date range across all sources
      - suitable_for decision support after human review

  historical_manual:
    meaning:
      - uses previously captured connector outputs
      - suitable for pipeline testing or comparison
      - not necessarily current enough for booking decisions
```

Default run mode:

```yaml
default_run_mode: sample
```

Rules:

```yaml
run_mode_rules:
  use_sample_if:
    - any_candidate_file_is_sample
    - any_connector_data_is_mock_or_sanitized
    - data_is_from_references_folder
    - prices_are_not_current
    - benchmark_logic_is_not_built

  use_live_manual_only_if:
    - travel_advisory_was_checked_for_current_run
    - flight_data_was_captured_for_same_dates
    - lodging_data_was_captured_for_same_dates
    - attractions_data_or_placeholder_is_explicitly_recorded
    - run_manifest_points_to_correct_inputs
    - report_date_matches_decision_date
```

---

# 4. Search Run Stage

Every vacation search must have a `search_run_id`.

Format:

```text
run_YYYYMMDD_destination_startdate_enddate
```

Example:

```text
run_20260625_lisbon_20261005_20261016
```

Search run configs belong in:

```text
config/search_runs/
```

Example:

```text
config/search_runs/run_20260625_lisbon_20261005_20261016.yaml
```

Required fields:

```yaml
search_run_required_fields:
  - search_run_id
  - status
  - created_at
  - origin_city
  - origin_airport
  - destination_city
  - destination_country
  - destination_airport
  - departure_date
  - return_date
  - trip_length_days
  - adults
  - children
  - currency
  - source_order
  - validation_rules
```

---

# 5. Raw Connector Capture Stage

Raw connector outputs should be saved locally under `data/raw/`.

Recommended folders:

```yaml
raw_folders:
  - data/raw/travel_advisory
  - data/raw/skyscanner
  - data/raw/expedia
  - data/raw/tripadvisor
  - data/raw/viator
  - data/raw/benchmark_prices
```

Raw file naming convention:

```text
search_run_id_source_destination_startdate_enddate.md
```

Examples:

```text
run_20260625_lisbon_20261005_20261016_skyscanner_lisbon.md
run_20260625_lisbon_20261005_20261016_expedia_lisbon.md
run_20260625_lisbon_20261005_20261016_tripadvisor_lisbon.md
```

Raw rules:

```yaml
raw_capture_rules:
  preserve:
    - source_name
    - capture_date
    - search_run_id
    - destination
    - date_range
    - traveler_count
    - currency
    - returned_options
    - caveats
    - connector_failures

  do_not_commit:
    - raw_connector_outputs
    - booking_links_with_session_data
    - account_specific_data
    - API_keys
    - .env
```

---

# 6. Candidate Construction Stage

The central object is:

```text
vacation_candidate
```

A valid candidate represents:

```yaml
vacation_candidate:
  includes:
    - one_origin
    - one_destination
    - one_date_range
    - one_round_trip_flight_option
    - one_lodging_option
    - one_attractions_budget_or_activity_set
    - one_travel_advisory_assessment
    - one_total_estimated_trip_cost
    - one_benchmark_or_benchmark_placeholder
    - one_candidate_decision
```

Current sample candidate path:

```text
references/sample_candidates/sample_lisbon_candidate.yaml
```

Future local manual candidate path:

```text
data/interim/manual_candidates/
```

Candidate validation command:

```bat
python scripts\validate_candidate_schema.py --sample
```

---

# 7. Processed Candidate Stage

The workflow should convert candidate YAML into flat rows.

Current scripts:

```yaml
processed_candidate_scripts:
  validate_candidate:
    - scripts/validate_candidate_schema.py
  flatten_candidate:
    - scripts/flatten_candidate_to_row.py
  build_processed_csv:
    - scripts/build_processed_candidate_csv.py
  check_processed_csv:
    - scripts/check_processed_candidate_csv.py
```

Current sample processed output:

```text
references/sample_processed/vacation_candidates_sample.csv
```

Future real processed output:

```text
data/processed/vacation_candidates/vacation_candidates.csv
```

Standard commands:

```bat
python scripts\validate_candidate_schema.py --sample
python scripts\flatten_candidate_to_row.py --write-csv
python scripts\build_processed_candidate_csv.py
python scripts\check_processed_candidate_csv.py
```

---

# 8. Scoring Stage

The project uses a 100-point scoring model.

```yaml
scoring_categories:
  price_undervaluation:
    points: 30
    status: not_ready
    requires_benchmark: true

  flight_quality_value:
    points: 15
    status: draft

  lodging_quality_value:
    points: 20
    status: draft

  destination_attractiveness:
    points: 10
    status: draft

  attractions_activity_value:
    points: 10
    status: not_ready
    requires_source_validation: true

  safety_travel_advisory_risk:
    points: 10
    status: draft

  practicality_friction:
    points: 5
    status: not_ready
```

Important rule:

```yaml
scoring_policy:
  allow_draft_component_scores: true
  allow_final_total_score: false
  allow_undervalued_label: false
  reason: benchmarking_and_fair_value_estimation_not_built_yet
```

Commands:

```bat
python scripts\validate_scoring_config.py
python scripts\check_scoring_readiness.py
python scripts\draft_component_scoring.py
```

---

# 9. Benchmarking Stage

Benchmarking is the key future stage.

No vacation should be called "undervalued" until this exists.

Benchmarking should estimate:

```yaml
benchmarking_inputs:
  - comparable_flight_prices
  - comparable_lodging_prices
  - comparable_activity_costs
  - destination_seasonality
  - trip_length
  - traveler_count
  - hotel_quality_band
  - destination_region
```

Core formula:

```text
estimated_discount_pct =
(fair_value_estimate_usd - actual_estimated_trip_cost_usd) / fair_value_estimate_usd
```

Benchmarking outputs:

```yaml
benchmarking_outputs:
  - fair_value_estimate_usd
  - actual_estimated_trip_cost_usd
  - estimated_discount_pct
  - benchmark_method
  - benchmark_confidence
  - undervalued_flag
```

Until this is built:

```yaml
benchmarking_status:
  fair_value_estimate_usd: null
  estimated_discount_pct: null
  benchmark_method: not_yet_built
  undervalued_flag: null
  ready_for_benchmarking: false
  ready_for_scoring: false
```

---

# 10. Safety and Entry Rules

Because Graham is a Canadian citizen and U.S. resident, and Anjali is a U.S. citizen, every destination should eventually check:

```yaml
safety_and_entry_checks:
  advisory_sources:
    - U.S. travel advisory
    - Government of Canada travel advisory

  entry_requirements:
    - Canadian passport holder entry rules
    - U.S. passport holder entry rules
    - passport_validity_requirement
    - visa_requirement
    - vaccination_requirement_if_any
    - regional_conflict_or_security_alerts
```

Risk rules:

```yaml
risk_rules:
  level_1:
    decision: eligible
  level_2:
    decision: eligible_with_caution
  level_3:
    decision: usually_manual_review_or_reject
  level_4:
    decision: automatic_reject
```

---

# 11. Recommendation Rules

```yaml
recommendation_rules:
  recommend_candidate_only_if:
    - search_run_sources_match
    - dates_match
    - travelers_match
    - advisory_not_reject
    - flight_is_operationally_reasonable
    - lodging_is_acceptable_quality
    - total_cost_is_calculated
    - fair_value_benchmark_exists
    - estimated_discount_pct_is_positive_enough
    - data_quality_flags_are_visible
    - human_review_completed

  flag_for_human_review_if:
    - flight_price_basis_uncertain
    - hotel_validation_unavailable
    - cancellation_policy_missing
    - activity_budget_placeholder_used
    - Canadian_advisory_missing
    - visa_or_passport_rules_missing
    - benchmark_confidence_low

  never_do:
    - recommend_booking_from_sample_data
    - hide_data_quality_flags
    - call_placeholder_activity_budget_validated
    - call_expedia_inventory_market_benchmark
    - call_candidate_undervalued_without_fair_value
```

---

# 12. Manifest and Audit Stage

Every real manual search run should eventually create a manifest.

Recommended folder:

```text
data/run_manifests/
```

Manifest required sections:

```yaml
manifest_required_sections:
  - run_id
  - run_date
  - run_mode
  - workflow
  - environment
  - connector_capture
  - raw_inputs
  - transformed_inputs
  - processed_outputs
  - scoring_outputs
  - benchmark_outputs
  - reports
  - parameters
  - known_limitations
```

File metadata:

```yaml
file_record_fields:
  - path
  - exists
  - size_bytes
  - sha256
```

Environment metadata:

```yaml
environment_metadata:
  - python_version
  - conda_environment
  - git_branch
  - git_commit
  - run_timestamp
```

---

# 13. Git and Privacy Policy

Safe to commit:

```yaml
safe_to_commit:
  - config_files
  - docs
  - scripts
  - source_code
  - tests
  - references/sample_candidates
  - references/sample_processed
  - prompt_templates
```

Do not commit:

```yaml
do_not_commit:
  - .env
  - API_keys
  - raw_connector_outputs
  - private_booking_links
  - payment_or_account_information
  - sensitive_personal_travel_documents
  - large_data_exports
```

Standard commit pattern:

```bat
git status
git add <files>
git commit -m "Clear milestone message"
git push
git status
```

---

# 14. Standard Operating Workflow

## Sample pipeline check

```bat
cd C:\Users\graha\Documents\Data_Projects\value-vacation-finder
conda activate value-vacation-finder
git status

python scripts\validate_candidate_schema.py --sample
python scripts\build_processed_candidate_csv.py
python scripts\check_processed_candidate_csv.py
python scripts\validate_scoring_config.py
python scripts\check_scoring_readiness.py
python scripts\draft_component_scoring.py
```

Expected current decision:

```text
Final total score: BLOCKED
Recommendation tier: BLOCKED
Undervalued label: BLOCKED
```

That is correct. The project is not ready for final scoring until benchmarking is built.

---

# 15. Current Project Status

```yaml
current_status:
  completed:
    - project_scaffold
    - traveler_profile
    - destination_watchlist
    - destination_filter
    - source_config
    - manual_workflow
    - connector_prompt_library
    - known_limitations
    - first_lisbon_search_run
    - travel_advisory_capture
    - skyscanner_capture
    - expedia_capture
    - tripadvisor_limitation_recorded
    - viator_limitation_recorded
    - raw_data_review
    - candidate_schema
    - sample_candidate
    - validation_script
    - flattening_script
    - processed_csv_builder
    - processed_csv_check
    - scoring_weights
    - scoring_config_validator
    - scoring_readiness_check
    - draft_component_scoring_skeleton

  not_yet_complete:
    - real_processed_dataset_writer
    - benchmark/fair_value_logic
    - Canadian travel advisory integration
    - passport/visa rules
    - activity source validation
    - final scoring
    - ranking
    - final shortlist report
    - run manifest system
```

---

# Recommended Save Location

Save this adapted instruction document as:

```text
references/project_full_instructions.md
```

Then commit it:

```bat
cd C:\Users\graha\Documents\Data_Projects\value-vacation-finder
conda activate value-vacation-finder
notepad references\project_full_instructions.md
git status
git add references\project_full_instructions.md
git commit -m "Add full project operating instructions"
git push
git status
```
