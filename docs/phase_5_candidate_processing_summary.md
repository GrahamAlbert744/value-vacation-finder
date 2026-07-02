\# Phase 5 Candidate Processing Summary



\## Purpose



Phase 5 converts the project from raw/manual vacation notes into structured candidate records and processed-style tabular outputs.



The main goal is to prove that the project can take one vacation candidate and move it through this path:



`structured candidate YAML -> schema validation -> flattened row -> processed-style CSV -> lightweight quality check`



This phase does not score vacations yet.



\---



\## Phase 5 Outputs



| Phase | Output | Purpose |

|---|---|---|

| 5.1 | First structured Lisbon candidate | Create the first manual vacation candidate |

| 5.2 | Candidate schema validation checklist | Define required candidate fields and validation rules |

| 5.3 | Candidate validation script | Check candidate YAML structure |

| 5.4 | Sanitized sample candidate | Create a GitHub-safe sample record |

| 5.5 | Validator sample/local support | Allow validation of local or sample candidate files |

| 5.6 | Processed candidate schema plan | Define the future flat vacation candidates dataset |

| 5.7 | Candidate flattening script | Convert nested YAML into one flat row |

| 5.8 | Flattening workflow documentation | Explain the flattening process |

| 5.9 | Processed candidate CSV builder | Build a sample processed-style CSV |

| 5.10 | Processed CSV check script | Verify the sample processed CSV |

| 5.11 | Phase 5 workflow summary | Summarize the completed candidate-processing pipeline |



\---



\## Important Files Created



\### Documentation



\- `docs/candidate\_schema\_validation.md`

\- `docs/processed\_candidate\_schema\_plan.md`

\- `docs/candidate\_flattening\_workflow.md`

\- `docs/processed\_candidate\_csv\_workflow.md`

\- `docs/processed\_candidate\_csv\_checks.md`

\- `docs/phase\_5\_candidate\_processing\_summary.md`



\### Scripts



\- `scripts/validate\_candidate\_schema.py`

\- `scripts/flatten\_candidate\_to\_row.py`

\- `scripts/build\_processed\_candidate\_csv.py`

\- `scripts/check\_processed\_candidate\_csv.py`



\### GitHub-Safe Sample Data



\- `references/sample\_candidates/sample\_lisbon\_candidate.yaml`

\- `references/sample\_candidates/sample\_lisbon\_candidate\_flattened.csv`

\- `references/sample\_processed/vacation\_candidates\_sample.csv`



\---



\## Candidate Processing Pipeline



The current sample pipeline is:



1\. Validate the sample candidate YAML.

2\. Flatten the nested candidate YAML into a processed-style row.

3\. Build a processed-style CSV from the candidate.

4\. Check the processed-style CSV for required fields and expected values.



\---



\## How to Run the Phase 5 Pipeline



From the project root:



```bash

cd C:\\Users\\graha\\Documents\\Data\_Projects\\value-vacation-finder

conda activate value-vacation-finder

