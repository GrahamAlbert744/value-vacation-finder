\# Scoring Config Validation



\## Purpose



This document explains the scoring configuration validation script.



The script is:



`scripts/validate\_scoring\_config.py`



The config file it checks is:



`config/scoring\_weights.yaml`



\---



\## Why This Exists



The project is now moving from candidate processing into scoring design.



Before writing scoring code, the project needs to verify that the scoring configuration is internally consistent.



The validation script checks that:



\- Required top-level sections exist.

\- Required scoring categories exist.

\- Category weights sum to 100.

\- Recommendation tiers exist.

\- Hard rejection rules exist.

\- MVP policy blocks final scoring before benchmarking is built.

\- MVP policy blocks use of the word “undervalued” before benchmarking is built.



\---



\## Current Scoring Categories



The scoring config currently uses a 100-point framework:



| Category | Points |

|---|---:|

| Price undervaluation | 30 |

| Flight quality/value | 15 |

| Lodging quality/value | 20 |

| Destination attractiveness | 10 |

| Attractions/activity value | 10 |

| Safety/travel advisory risk | 10 |

| Practicality/friction | 5 |



Total:



`100 points`



\---



\## Important MVP Rule



The project may use draft component scores for testing.



The project should not yet produce:



\- Final total score

\- Final recommendation tier

\- Final undervalued label



Reason:



Benchmarking and fair-value estimation have not been implemented yet.



\---



\## How to Run



From the project root:



```bash

python scripts\\validate\_scoring\_config.py

