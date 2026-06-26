\# Raw Data Review Checklist



\## Purpose



This checklist is used after connector-assisted data collection and before any cleaning, scoring, or report generation.



The goal is to verify that all raw source outputs refer to the same vacation search run.



A valid search run must match on:



\- Same search run ID

\- Same origin

\- Same destination

\- Same country

\- Same departure date

\- Same return date

\- Same traveler count

\- Same currency where possible



\---



\## Search Run Under Review



Search run ID:



`run\_20260625\_lisbon\_20261005\_20261016`



Destination:



Lisbon, Portugal



Origin:



Boston / BOS



Dates:



\- Departure / check-in: 2026-10-05

\- Return / check-out: 2026-10-16



Trip length:



11 nights / 11-day date span depending on calculation convention



Travelers:



2 adults



Currency:



USD where available



\---



\## Source Status Summary



| Source | Expected Role | Status | Decision |

|---|---|---|---|

| Travel Advisory | Safety/risk check | Available | Continue |

| Skyscanner | Flight pricing | Available | Continue with price interpretation caveat |

| Expedia | Hotel pricing | Available | Continue |

| Tripadvisor | Hotel quality validation | Inconclusive / unavailable | Continue with missing validation flag |

| Viator | Attractions/tours | Blocked / unavailable | Continue with placeholder activity budget |



\---



\## Travel Advisory Review



Raw file expected:



`data/raw/travel\_advisory/run\_20260625\_lisbon\_20261005\_20261016\_travel\_advisory\_lisbon.md`



Checklist:



\- \[ ] Country is Portugal

\- \[ ] Destination is Lisbon, Portugal

\- \[ ] Advisory level is recorded

\- \[ ] Advisory decision is recorded

\- \[ ] Advisory does not require rejection

\- \[ ] Entry/exit notes are recorded if available



Current result:



\- Advisory level: 1

\- Advisory label: Exercise Normal Precautions

\- Decision: Continue



Review decision:



`pass`



\---



\## Skyscanner Flight Review



Raw file expected:



`data/raw/skyscanner/run\_20260625\_lisbon\_20261005\_20261016\_skyscanner\_lisbon.md`



Checklist:



\- \[ ] Origin is BOS

\- \[ ] Destination is LIS

\- \[ ] Departure date is 2026-10-05

\- \[ ] Return date is 2026-10-16

\- \[ ] Cabin is economy

\- \[ ] Currency is USD

\- \[ ] Flight options are operationally reasonable

\- \[ ] Stops are recorded

\- \[ ] Durations are recorded

\- \[ ] Price is recorded

\- \[ ] Price interpretation is clear



Current result:



\- Viable nonstop BOS-LIS flights found

\- Main carrier: TAP Air Portugal

\- Listed price: 737.97 USD

\- Price interpretation: NEEDS\_VERIFICATION



Review decision:



`conditional\_pass`



Reason:



Flight options are viable, but the project must verify whether listed prices are per person or total for two adults before final scoring.



\---



\## Expedia Hotel Review



Raw file expected:



`data/raw/expedia/run\_20260625\_lisbon\_20261005\_20261016\_expedia\_lisbon.md`



Checklist:



\- \[ ] Destination is Lisbon, Portugal

\- \[ ] Check-in date is 2026-10-05

\- \[ ] Check-out date is 2026-10-16

\- \[ ] Traveler count is 2 adults

\- \[ ] Room count is 1

\- \[ ] Currency is USD

\- \[ ] Hotel names are recorded

\- \[ ] Total prices are recorded

\- \[ ] Nightly prices are recorded

\- \[ ] Guest ratings are recorded

\- \[ ] Review counts are recorded if available

\- \[ ] Weak or low-review-count hotels are flagged



Current result:



Representative value candidates:



1\. Hotel Gat Rossio

2\. VIP Executive Suites do Marques Hotel

3\. HF Fenix Music

4\. VIP Executive Picoas Hotel

5\. Chiado 44



Review decision:



`pass`



Caveats:



\- Cancellation policies were not captured.

\- Location quality still needs validation.

\- Tripadvisor validation was unavailable.

\- Expedia inventory is only one lodging source.



\---



\## Tripadvisor Hotel Quality Review



Raw file expected:



`data/raw/tripadvisor/run\_20260625\_lisbon\_20261005\_20261016\_tripadvisor\_lisbon.md`



Checklist:



\- \[ ] Destination is Lisbon, Portugal

\- \[ ] Dates match the search run

\- \[ ] Traveler count is 2 adults

\- \[ ] Expedia hotel candidates were submitted

\- \[ ] Matched Tripadvisor hotels were returned

\- \[ ] Review/rating quality is recorded

\- \[ ] Common complaints are recorded

\- \[ ] Location concerns are recorded

\- \[ ] Cleanliness/service/value signals are recorded



Current result:



\- Explicit hotel-name comparison returned no matched hotels.

\- Broader Tripadvisor search was blocked by tool safety checks.

\- Validation status: unavailable / inconclusive



Review decision:



`missing\_validation\_continue`



Reason:



Do not reject Expedia hotels solely because Tripadvisor validation failed. Continue with Expedia-only lodging data, but mark hotel quality validation as incomplete.



\---



\## Viator Attractions and Tours Review



Raw file expected:



`data/raw/viator/run\_20260625\_lisbon\_20261005\_20261016\_viator\_lisbon.md`



Checklist:



\- \[ ] Destination is Lisbon, Portugal

\- \[ ] Date range is 2026-10-05 to 2026-10-16

\- \[ ] Traveler count is 2 adults

\- \[ ] Experience names are recorded

\- \[ ] Prices are recorded

\- \[ ] Ratings are recorded

\- \[ ] Review counts are recorded

\- \[ ] Representative activity budget is recorded



Current result:



\- Viator connector search was blocked by tool safety checks.

\- Structured activity results unavailable.

\- Placeholder activity budget used.



Placeholder:



\- Estimated attraction cost per person: 200 USD

\- Estimated attraction cost for two adults: 400 USD



Review decision:



`placeholder\_continue`



Reason:



Proceed with placeholder activity budget for MVP, but do not treat activity data as fully validated.



\---



\## Cross-Source Matching Review



Checklist:



\- \[ ] Same search run ID across all sources

\- \[ ] Same destination city

\- \[ ] Same country

\- \[ ] Same origin airport

\- \[ ] Same departure/check-in date

\- \[ ] Same return/check-out date

\- \[ ] Same traveler count

\- \[ ] Same currency where available

\- \[ ] No source uses a nearby city without being flagged

\- \[ ] No source introduces a conflicting date range

\- \[ ] No source introduces a conflicting traveler count



Current review:



| Field | Expected | Status |

|---|---|---|

| Search run ID | run\_20260625\_lisbon\_20261005\_20261016 | Pass |

| Origin | BOS | Pass |

| Destination | Lisbon, Portugal | Pass |

| Destination airport | LIS | Pass |

| Start date | 2026-10-05 | Pass |

| End date | 2026-10-16 | Pass |

| Travelers | 2 adults | Pass |

| Currency | USD where available | Pass / partial |

| Safety status | Continue | Pass |

| Hotel validation | Expedia only | Caveat |

| Attractions validation | Placeholder only | Caveat |



\---



\## Raw Data Quality Flags



Current flags:



\- `flight\_price\_interpretation\_needs\_verification`

\- `tripadvisor\_validation\_unavailable`

\- `viator\_validation\_unavailable`

\- `activity\_budget\_placeholder\_used`

\- `hotel\_cancellation\_policy\_missing`

\- `hotel\_location\_quality\_missing`

\- `expedia\_inventory\_only`



\---



\## Phase 4.1 Decision



The Lisbon search run is acceptable for MVP continuation, but only with caveats.



Decision:



`continue\_to\_structured\_review\_summary`



The project may proceed to a structured raw data review summary, but final scoring must clearly flag:



\- Flight price uncertainty

\- Missing Tripadvisor validation

\- Placeholder Viator activity budget

\- Expedia-only lodging data

\- Missing cancellation-policy detail



\---



\## Next Step



Next phase:



`Phase 4.2 — Create structured raw data review summary for Lisbon`



This will convert the raw review into a simple project-facing summary that can later feed the cleaning and scoring modules.

