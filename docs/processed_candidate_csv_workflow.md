\# Processed Candidate CSV Workflow



\## Purpose



This document explains how the project builds a processed-style vacation candidates CSV from a structured candidate YAML file.



The current script is:



`scripts/build\_processed\_candidate\_csv.py`



This is an MVP bridge from:



`candidate YAML -> validation -> flattened row -> processed-style CSV`



\---



\## Current Input



Default input:



`references/sample\_candidates/sample\_lisbon\_candidate.yaml`



This is a GitHub-safe sample candidate.



\---



\## Current Output



Default output:



`references/sample\_processed/vacation\_candidates\_sample.csv`



This output is also GitHub-safe because it is generated from a sanitized sample candidate.



\---



\## Why This Uses references Instead of data/processed



The final project will eventually write real processed outputs to:



`data/processed/vacation\_candidates/vacation\_candidates.csv`



However, `data/processed/` may be ignored by Git to avoid committing private or changing data.



For now, the sample processed CSV goes under:



`references/sample\_processed/`



This allows the repo to show the intended processed dataset shape without committing private travel data.



\---



\## How to Run



Build the sample processed CSV:



```bash

python scripts\\build\_processed\_candidate\_csv.py

