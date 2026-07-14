# Project Status

## Project Name

Value Vacation Finder

## Current Phase

Phase 7 — Benchmarking (first real, low-confidence pass complete)

> Note: this document previously said "Phase 1" while the project had
> already progressed through candidate construction, processed-CSV tooling,
> and draft scoring. Updated 2026-07-07 during a full project audit, and
> again 2026-07-13 after the first real benchmark pass, to reflect actual
> repo state. See `docs/known_limitations.md` for the matching
> "completed / not yet completed" list and
> `references/project_full_instructions.md` for the full operating policy.

## Project Goal

Value Vacation Finder identifies potentially undervalued vacation opportunities from Boston by combining:

- Flight data
- Hotel and lodging data
- Hotel review and quality data
- Tours and attractions data
- Travel advisory and safety data
- Benchmark/fair-value estimates

The final output will be a ranked shortlist of vacation candidates.

---

## Core Rule

A valid vacation candidate must match on:

- Same origin
- Same destination
- Same departure date
- Same return date
- Same traveler count
- Same currency where possible
- Same search run ID

For the MVP:

- Origin: Boston / BOS
- Travelers: 2 adults
- Trip length: 7 to 21 days
- Currency: USD
- Manual run only

---

## Completed Phases

### Phase 0 — Project scaffold and GitHub setup

Status: Complete

Completed items:

- Created project folder
- Created conda environment
- Created GitHub repository
- Initialized Git
- Added starter folder structure
- Added `.gitignore`
- Added `.env.example`
- Added starter README
- Pushed project to GitHub

---

### Phase 1.1 — Traveler profile

Status: Complete

File:

`config/traveler_profile.yaml`

Purpose:

Stores stable traveler assumptions, including origin airport, traveler count, citizenship, residency, trip length rules, and travel style preferences.

---

### Phase 1.2 — Destination universe

Status: Complete

File:

`config/destinations_watchlist.yaml`

Purpose:

Stores the large destination universe, including EU capitals, EU major cities, South and Central American destinations, ASEAN destinations, Japan, South Korea, and selected African destinations.

Important note:

This is a broad candidate universe, not the MVP search list.

---

### Phase 1.3 — Destination filter config

Status: Complete

Files:

- `config/destination_filter.yaml`
- `docs/destination_filtering.md`

Purpose:

Controls which destinations are active for a given manual search run.

This lets the project keep a large destination universe while only searching a small subset during the MVP.

---

### Phase 1.4 — Source configuration

Status: Complete

Files:

- `config/source_config.yaml`
- `docs/source_config_notes.md`

Purpose:

Defines which source handles each part of the project.

Source roles:

- Travel Advisory: safety and risk
- Skyscanner: flights
- Expedia: hotel pricing and package-style comps
- Tripadvisor: hotel quality and reviews
- Viator: attractions, tours, and experiences

---

### Phase 1.5 — Data dictionary skeleton

Status: Complete

File:

`docs/data_dictionary.md`

Purpose:

Defines the expected fields for the final `vacation_candidate` table.

---

### Phase 1.6 — Manual workflow document

Status: Complete

File:

`docs/manual_workflow.md`

Purpose:

Documents the manual process for collecting data without mixing destinations, dates, traveler assumptions, or source outputs.

---

### Phase 1.7 — Connector prompt library

Status: Complete

File:

`prompts/connector_prompts.md`

Purpose:

Stores reusable prompts for Travel Advisory, Skyscanner, Expedia, Tripadvisor, and Viator.

These prompts are not run automatically. They are copied and used later during manual data collection.

---

### Phase 1.8 — Known limitations

Status: Complete

File:

`docs/known_limitations.md`

Purpose:

Documents what the project cannot do yet, including limitations around connector data, airport validation, travel advisories, visas, benchmarking, and scoring.

---

## Completed Phases (continued)

### Phase 2 — Search run setup

Status: Complete

Files:

- `config/search_run_template.yaml`
- `config/search_runs/run_20260625_lisbon_20261005_20261016.yaml`
- `docs/search_run_protocol.md`

First search run: Lisbon, Portugal, BOS origin, 2026-10-05 to 2026-10-16, 2 adults.

---

### Phase 3 — Manual connector data collection

Status: Complete for the Lisbon run

Raw notes captured under `data/raw/{travel_advisory,skyscanner,expedia,tripadvisor,viator}/`.
Tripadvisor's broader hotel search was blocked (proceeded with Expedia-only
lodging validation); Viator was blocked (proceeded with a placeholder
activity budget). Both limitations are recorded in the search run config.

---

### Phase 4 — Raw data review

Status: Complete

File: `docs/raw_data_review_summary_lisbon.md` (checklist in `docs/raw_data_review_checklist.md`).

---

### Phase 5 — Candidate construction and processed CSV tooling

Status: Complete

Files:

- Candidate schema + sample candidate: `references/sample_candidates/sample_lisbon_candidate.yaml`
- `scripts/validate_candidate_schema.py`
- `scripts/flatten_candidate_to_row.py`
- `scripts/build_processed_candidate_csv.py`
- `scripts/check_processed_candidate_csv.py`
- Sample processed output: `references/sample_processed/vacation_candidates_sample.csv`

---

### Phase 6 — Scoring configuration and draft scoring

Status: Complete (draft-only, as intended)

Files:

- `config/scoring_weights.yaml`
- `scripts/validate_scoring_config.py`
- `scripts/check_scoring_readiness.py`
- `scripts/draft_component_scoring.py`

Final total score, recommendation tier, and undervalued label remain
intentionally blocked until benchmarking exists.

---

## Completed Phases (continued)

### Phase 7 — Benchmarking

Status: First real pass complete (low confidence)

`src/value_vacation_finder/benchmarking/fair_value.py` implements a
bottom-up, component-based benchmark: `estimate_fair_value()` sums sourced
comparable costs (flights, hotel, activities, food+transport) and
`calculate_discount_pct()` compares that against
`actual_estimated_trip_cost_usd`. Callers must supply real, sourced
component costs — the functions raise rather than fabricate a missing
component.

For the Lisbon run, comparable prices were researched via web search
(published cost-index/aggregator data, not a live matched-itinerary
quote) and recorded in
`data/raw/benchmark_prices/run_20260625_lisbon_20261005_20261016_benchmark_prices_lisbon.md`,
including a documented disagreement between the bottom-up estimate and a
top-down peer-basket cross-check. This is why `benchmark_confidence` is
recorded as `low` on the real candidate
(`data/interim/manual_candidates/lisbon_candidate_001.yaml`):
`fair_value_estimate_usd: $5,240`, `estimated_discount_pct: 18.04%`,
`undervalued_flag: directionally_undervalued_low_confidence`.

`scripts/draft_component_scoring.py`'s `score_price_undervaluation()` now
scores this for real (20-point "good" band, halved by the low-confidence
multiplier to 10/30) instead of always returning `not_ready`. The overall
final score/tier/undervalued label remain correctly `BLOCKED` — both
because `config/scoring_weights.yaml`'s `mvp_scoring_policy.allow_final_total_score`
is still `false`, and because `attractions_activity_value` and
`practicality_friction` are still `not_ready`.

---

## Upcoming Phases

### Phase 8 — Risk filtering

Goal:

Reject or flag trips with serious travel advisory, conflict, safety, or
entry-risk issues. Requires Canadian travel advisory integration and
passport/visa rules (see `config/entry_requirements_template.yaml`).

---

### Phase 9 — Final scoring

Goal:

Unblock final total score once benchmarking and risk filtering exist.

---

### Phase 10 — Reporting

Goal:

Generate a ranked vacation shortlist as CSV and markdown, backed by a
run manifest (`scripts/build_run_manifest.py`, `data/run_manifests/`).

---

## Next Immediate Step

Raise benchmark confidence above "low" (a live, date-matched flight/hotel
quote would let `estimated_discount_pct` be trusted more than the current
published-cost-index estimate), and/or unblock `attractions_activity_value`
and `practicality_friction` — a real Viator activity capture and a real
Canadian/U.S. entry-requirements lookup (`config/entry_requirements_template.yaml`)
are the two concrete blockers keeping the final total score off, even
though price_undervaluation now has a real draft score.