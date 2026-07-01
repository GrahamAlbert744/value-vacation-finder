# Candidate Flattening Workflow

## Purpose

This document explains how the project converts a nested vacation candidate YAML file into a flat processed-style row.

The flattening step is the bridge between:

- Human-readable structured candidate records
- Analysis-ready tabular data
- Future scoring and ranking outputs

The main script is:

`scripts/flatten_candidate_to_row.py`

---

## Why Flattening Is Needed

The manually structured candidate YAML is easy for humans to read because it groups fields into sections:

- candidate
- origin
- destination
- dates
- travelers
- flight
- lodging
- attractions
- risk
- cost_estimate
- benchmark
- data_quality_flags
- candidate_decision

However, scoring, ranking, filtering, reporting, and exporting are easier when each vacation candidate becomes one row in a table.

The flattened row is the future shape of:

`data/processed/vacation_candidates/vacation_candidates.csv`

---

## Input File

The default sample input is:

`references/sample_candidates/sample_lisbon_candidate.yaml`

The local real/interim candidate input is:

`data/interim/manual_candidates/lisbon_candidate_001.yaml`

Because `data/interim/` may be ignored by Git, the GitHub-safe sample candidate is used for reproducible testing.

---

## Output File

The sample flattened output is:

`references/sample_candidates/sample_lisbon_candidate_flattened.csv`

This file is safe to commit because it is generated from the sanitized sample candidate.

Later, real processed outputs should go under:

`data/processed/vacation_candidates/`

but those may remain ignored by Git depending on project privacy rules.

---

## Current Script

Script:

`scripts/flatten_candidate_to_row.py`

Current behavior:

1. Loads a candidate YAML file.
2. Safely extracts nested fields.
3. Converts `data_quality_flags` from a list into a pipe-separated string.
4. Creates derived boolean data-quality fields.
5. Prints the flattened row.
6. Optionally writes the row to CSV.

---

## Basic Usage

Print the default sample candidate as a flattened row:

```bash
python scripts\flatten_candidate_to_row.py