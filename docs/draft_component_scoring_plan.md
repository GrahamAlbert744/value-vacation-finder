\# Draft Component Scoring Plan



\## Purpose



This document explains how each draft vacation scoring component should eventually be calculated.



This is a planning document only.



It does not implement scoring code.



The scoring configuration lives in:



`config/scoring\_weights.yaml`



The scoring validator lives in:



`scripts/validate\_scoring\_config.py`



\---



\## Important MVP Rule



The project should not produce a final total vacation score yet.



The project should not call any vacation candidate "undervalued" yet.



Reason:



Benchmarking and fair-value estimation have not been implemented.



Allowed during MVP:



\- Draft component scoring plans

\- Draft component scores for testing

\- Data-quality flags

\- Candidate readiness flags



Not allowed yet:



\- Final total score

\- Final recommendation tier

\- Final undervalued label



\---



\## Current 100-Point Framework



| Component | Points | Current Status |

|---|---:|---|

| Price undervaluation | 30 | Not ready |

| Flight quality/value | 15 | Draft |

| Lodging quality/value | 20 | Draft |

| Destination attractiveness | 10 | Draft |

| Attractions/activity value | 10 | Not ready |

| Safety/travel advisory risk | 10 | Draft |

| Practicality/friction | 5 | Draft |



Total:



`100 points`



\---



\# Component 1 — Price Undervaluation



Weight:



`30 points`



Status:



`not\_ready`



\## Purpose



Measure whether the actual estimated trip cost is meaningfully below fair value for comparable trips.



This is the heart of the project.



\## Required Inputs



\- `actual\_estimated\_trip\_cost\_usd`

\- `fair\_value\_estimate\_usd`

\- `estimated\_discount\_pct`

\- `benchmark\_method`



\## Planned Formula



```text

estimated\_discount\_pct =

(fair\_value\_estimate\_usd - actual\_estimated\_trip\_cost\_usd) / fair\_value\_estimate\_usd

