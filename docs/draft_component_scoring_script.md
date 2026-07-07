\# Draft Component Scoring Script



\## Purpose



This document explains the draft component scoring skeleton.



The script is:



`scripts/draft\_component\_scoring.py`



The current input is:



`references/sample\_processed/vacation\_candidates\_sample.csv`



This script creates draft component scores where possible, but it does not calculate a final total score.



\---



\## Important Rule



The script must block:



\- Final total vacation score

\- Recommendation tier

\- Undervalued label



Reason:



Benchmarking and fair-value estimation are not implemented yet.



\---



\## What the Script Currently Does



The script reads one processed-style candidate row and runs draft scoring functions for:



\- Price undervaluation

\- Flight quality/value

\- Lodging quality/value

\- Destination attractiveness

\- Attractions/activity value

\- Safety/travel advisory risk

\- Practicality/friction



Each function returns:



\- Component name

\- Maximum points

\- Draft score or `None`

\- Readiness status

\- Reason

\- Blocking flags



\---



\## Current Expected Status



For the Lisbon sample candidate, expected statuses are:



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



\## Why Final Scoring Is Blocked



Final scoring is blocked because the sample candidate still has major caveats:



\- Fair-value benchmark missing

\- Flight price interpretation needs verification

\- Tripadvisor hotel validation unavailable

\- Viator activity validation unavailable

\- Activity budget placeholder used

\- Canadian advisory check not implemented

\- Visa/passport practicality fields missing



\---



\## How to Run



From the project root:



```bash

python scripts\\build\_processed\_candidate\_csv.py

python scripts\\draft\_component\_scoring.py

