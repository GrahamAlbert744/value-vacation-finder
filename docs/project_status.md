# Project Status

## Project Name

Value Vacation Finder

## Current Phase

Phase 1 — Project configuration and documentation

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

## Current Step

### Phase 1.9 — Project status and phase checklist

Status: In progress

File:

`docs/project_status.md`

Purpose:

Records the current state of the project so the next session can resume cleanly.

---

## Upcoming Phases

### Phase 2 — Search run setup

Goal:

Create a specific manual search run using one destination and one date range.

Planned files:

- `config/search_run_template.yaml`
- `data/raw/search_runs/`
- `docs/search_run_protocol.md`

Example search run:

- Destination: Lisbon, Portugal
- Origin: BOS
- Departure date: 2026-10-05
- Return date: 2026-10-16
- Travelers: 2 adults

---

### Phase 3 — Manual connector data collection

Goal:

Use connectors in the correct order:

1. Travel Advisory
2. Skyscanner
3. Expedia
4. Tripadvisor
5. Viator

Output:

Raw markdown or structured notes saved under:

- `data/raw/travel_advisory/`
- `data/raw/skyscanner/`
- `data/raw/expedia/`
- `data/raw/tripadvisor/`
- `data/raw/viator/`

Important:

Raw travel data should not be committed to GitHub unless it is mock/sample data.

---

### Phase 4 — Raw data review

Goal:

Check whether all connector outputs match the same destination, dates, traveler count, and currency.

---

### Phase 5 — Cleaning modules

Goal:

Build Python modules to convert raw connector outputs into standardized interim tables.

---

### Phase 6 — Matching logic

Goal:

Build valid vacation candidates only when flight, lodging, attractions, and advisory data match correctly.

---

### Phase 7 — Benchmarking

Goal:

Estimate fair trip value and calculate whether the trip appears undervalued.

---

### Phase 8 — Risk filtering

Goal:

Reject or flag trips with serious travel advisory, conflict, safety, or entry-risk issues.

---

### Phase 9 — Scoring

Goal:

Score valid vacation candidates using the 100-point scoring model.

---

### Phase 10 — Reporting

Goal:

Generate a ranked vacation shortlist as CSV and markdown.

---

## Next Immediate Step

After Phase 1.9 is committed, begin:

`Phase 2.1 — Create search_run_template.yaml`

This will define the first actual manual vacation search.