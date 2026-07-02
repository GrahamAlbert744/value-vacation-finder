\# Processed Candidate CSV Checks



\## Purpose



This document explains the lightweight quality check for the sample processed vacation candidates CSV.



The check script is:



`scripts/check\_processed\_candidate\_csv.py`



The sample processed CSV is:



`references/sample\_processed/vacation\_candidates\_sample.csv`



\---



\## Why This Check Exists



The project is moving from nested YAML candidate records into flat processed-style CSV rows.



Before scoring, benchmarking, or ranking candidates, the project needs confidence that the processed CSV contains the required fields and preserves important caveats.



This check helps catch simple errors such as:



\- Missing columns

\- Wrong destination fields

\- Wrong dates

\- Missing data-quality flags

\- Accidentally marking an incomplete candidate as ready for scoring

\- Accidentally marking an incomplete candidate as ready for benchmarking



\---



\## What the Check Verifies



The script verifies that:



1\. The sample processed CSV exists.

2\. The CSV has exactly one sample row.

3\. Required columns exist.

4\. Key Lisbon sample values are correct.

5\. Data-quality flags were preserved.

6\. Derived boolean data-quality fields are correct.

7\. The candidate is still marked as not ready for scoring.

8\. The candidate is still marked as not ready for benchmarking.



\---



\## How to Run



First rebuild the sample processed CSV:



```bash

python scripts\\build\_processed\_candidate\_csv.py

