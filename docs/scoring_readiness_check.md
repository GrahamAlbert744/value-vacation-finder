\# Scoring Readiness Check



\## Purpose



This document explains the scoring readiness check script.



The script is:



`scripts/check\_scoring\_readiness.py`



The current input is:



`references/sample\_processed/vacation\_candidates\_sample.csv`



This script does not calculate scores.



It only checks whether each scoring component is ready, draft-ready with caveats, or not ready.



\---



\## Why This Exists



The project should not score incomplete vacation candidates as if they were fully validated.



The scoring readiness check preserves discipline before scoring code is written.



It helps identify which components can move forward and which require better data.



\---



\## Current Scoring Components



The script checks:



\- Price undervaluation

\- Flight quality/value

\- Lodging quality/value

\- Destination attractiveness

\- Attractions/activity value

\- Safety/travel advisory risk

\- Practicality/friction



\---



\## Status Labels



The script uses these status labels:



| Status | Meaning |

|---|---|

| ready | Component appears structurally ready |

| draft\_ready | Component can receive a draft score |

| draft\_ready\_with\_caveats | Component can receive a draft score only if caveats are preserved |

| not\_ready | Component should not be scored yet |



\---



\## Expected Lisbon Sample Result



The current Lisbon sample should broadly return:



| Component | Expected Status |

|---|---|

| Price undervaluation | not\_ready |

| Flight quality/value | draft\_ready\_with\_caveats |

| Lodging quality/value | draft\_ready\_with\_caveats |

| Destination attractiveness | draft\_ready |

| Attractions/activity value | not\_ready |

| Safety/travel advisory risk | draft\_ready\_with\_caveats |

| Practicality/friction | not\_ready |



\---



\## Why Lisbon Is Not Ready for Final Scoring



The Lisbon sample is not ready for final total scoring because:



\- Fair-value benchmarking is missing.

\- Flight price basis needs verification.

\- Tripadvisor hotel validation is unavailable.

\- Viator activity validation is unavailable.

\- Activity budget is placeholder-based.

\- Canadian advisory/entry checks are not yet implemented.

\- Visa/passport practicality fields are incomplete.



\---



\## How to Run



From the project root:



```bash

python scripts\\build\_processed\_candidate\_csv.py

python scripts\\check\_scoring\_readiness.py

