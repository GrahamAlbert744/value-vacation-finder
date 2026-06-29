\# Structured Vacation Candidate — Lisbon



\## Purpose



This document summarizes the first manually structured vacation candidate for the Value Vacation Finder project.



The actual interim candidate file is stored locally at:



`data/interim/manual\_candidates/lisbon\_candidate\_001.yaml`



Depending on `.gitignore`, the interim data file may not be committed to GitHub.



\---



\## Candidate ID



`trip\_20261005\_lisbon\_001`



\## Search Run ID



`run\_20260625\_lisbon\_20261005\_20261016`



\---



\## Candidate Summary



| Field | Value |

|---|---|

| Origin | Boston / BOS |

| Destination | Lisbon, Portugal / LIS |

| Departure date | 2026-10-05 |

| Return date | 2026-10-16 |

| Travelers | 2 adults |

| Candidate status | MVP manual candidate |

| Ready for final scoring | No |

| Ready for benchmarking | No |



\---



\## Flight Component



Source:



Skyscanner



Selected MVP flight assumption:



\- Airline: TAP Air Portugal

\- Route: BOS to LIS

\- Outbound stops: 0

\- Return stops: 0

\- Outbound duration: 395 minutes

\- Return duration: 465 minutes

\- Listed price: 737.97 USD

\- MVP assumption: price is per person

\- Estimated total flight cost for two adults: 1475.94 USD



Main caveat:



The listed Skyscanner price must be verified as per-person vs total before final scoring.



\---



\## Lodging Component



Source:



Expedia



Selected MVP lodging assumption:



\- Hotel: Hotel Gat Rossio

\- Guest rating: 9.0

\- Review count: 1001

\- Star rating: 2.0

\- Nightly price: 151.00 USD

\- Total price: 1819.00 USD



Reason selected:



Hotel Gat Rossio is the first MVP lodging candidate because it combines a relatively low total price with a strong Expedia guest rating and high review count.



Main caveats:



\- Tripadvisor validation unavailable

\- Cancellation policy missing

\- Location quality needs manual validation

\- Expedia is the only lodging source used so far



\---



\## Attractions Component



Source:



Placeholder



Viator validation was unavailable/blocked for this run.



MVP placeholder:



\- Estimated attraction cost per person: 200 USD

\- Estimated attraction cost for two adults: 400 USD



Main caveat:



Activity cost is not source-validated.



\---



\## Risk Component



Source:



Travel Advisory connector



Portugal result:



\- Advisory level: 1

\- Advisory label: Exercise Normal Precautions

\- Decision: Continue



Risk decision:



Portugal does not trigger a project-level safety rejection for this MVP candidate.



\---



\## Draft Cost Estimate



| Component | Estimated Cost USD |

|---|---:|

| Flights | 1475.94 |

| Lodging | 1819.00 |

| Attractions placeholder | 400.00 |

| Food/transport buffer | 600.00 |

| Total draft trip cost | 4294.94 |



\---



\## Data Quality Flags



This candidate must carry the following flags:



\- `flight\_price\_interpretation\_needs\_verification`

\- `tripadvisor\_validation\_unavailable`

\- `viator\_validation\_unavailable`

\- `activity\_budget\_placeholder\_used`

\- `hotel\_cancellation\_policy\_missing`

\- `hotel\_location\_quality\_missing`

\- `expedia\_inventory\_only`

\- `food\_transport\_buffer\_placeholder`

\- `fair\_value\_estimate\_missing`



\---



\## Candidate Decision



Decision:



`usable\_for\_mvp\_candidate\_building`



This candidate is good enough to test the project structure, but it is not good enough for a real booking decision or final recommendation.



It should not be called “undervalued” yet because benchmark/fair-value logic has not been built.



\---



\## Next Phase



Next phase:



`Phase 5.2 — Create a candidate schema validation checklist`



Goal:



Define what fields must exist before any candidate can move from manual/interim form into a future processed vacation candidate dataset.

