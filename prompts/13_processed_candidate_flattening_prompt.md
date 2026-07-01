# Processed Candidate Flattening Prompt

Use this for Phase 5.7 or later.

```text
Help me create a Python script for value-vacation-finder that flattens a structured candidate YAML file into a processed-style row.

Input options:
- Local interim candidate: data/interim/manual_candidates/lisbon_candidate_001.yaml
- GitHub-safe sample candidate: references/sample_candidates/sample_lisbon_candidate.yaml

Output:
- A flattened dictionary printed to console
- Optional CSV output under data/processed/vacation_candidates/

Requirements:
1. Use argparse with --sample and --path options.
2. Preserve data quality flags.
3. Convert nested YAML fields to flat column names.
4. Add derived boolean flags:
   - has_flight_price_uncertainty
   - has_missing_hotel_validation
   - has_placeholder_activity_budget
   - has_missing_benchmark
5. Validate the cost formula.
6. Do not overwrite raw or interim data.
7. Make the script simple and MVP-friendly.
8. Tell me how to test it.
9. Tell me when to commit.
```
