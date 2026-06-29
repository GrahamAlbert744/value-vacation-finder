\# Candidate Schema Validation



\## Purpose



This document defines the minimum required fields and validation rules for a structured `vacation\_candidate`.



A vacation candidate should not move from manual/interim form into a processed dataset unless it passes basic schema validation.



The goal is to prevent the project from accidentally combining mismatched flights, hotels, dates, travelers, destinations, or source assumptions.



\---



\## Unit of Analysis



The unit of analysis is:



`vacation\_candidate`



A valid vacation candidate represents one possible vacation option from Boston for two adult travelers over a fixed date range.



Each candidate should combine:



\- One destination

\- One date range

\- One round-trip flight option

\- One lodging option

\- One attractions/tours estimate

\- One travel advisory/risk assessment

\- One total estimated trip cost

\- One benchmark/fair-value estimate or placeholder

\- One score or pre-scoring status



\---



\## Required Top-Level Sections



A candidate YAML file should include these top-level sections:



\- `candidate`

\- `origin`

\- `destination`

\- `dates`

\- `travelers`

\- `flight`

\- `lodging`

\- `attractions`

\- `risk`

\- `cost\_estimate`

\- `benchmark`

\- `data\_quality\_flags`

\- `candidate\_decision`



\---



\## Required Candidate Fields



| Section | Required Field | Rule |

|---|---|---|

| candidate | trip\_id | Must not be null |

| candidate | search\_run\_id | Must match the active search run |

| candidate | candidate\_status | Must not be null |

| candidate | destination\_slug | Must not be null |

| origin | city | Must be Boston for MVP |

| origin | airport\_code | Must be BOS for MVP |

| destination | city | Must match search run destination |

| destination | country | Must match search run country |

| destination | airport\_code | Must match destination airport |

| dates | departure\_date | Must match flight departure date |

| dates | return\_date | Must match flight return date |

| dates | trip\_length\_days | Must be between 7 and 21 |

| dates | trip\_length\_valid | Must be true |

| travelers | adults | Must equal 2 for MVP |

| travelers | children | Must equal 0 for MVP |

| travelers | traveler\_count | Must equal adults + children |

| flight | source | Must not be null |

| flight | route | Must include BOS and destination airport |

| flight | estimated\_total\_flight\_cost\_usd | Must be numeric or flagged |

| lodging | source | Must not be null |

| lodging | hotel\_name | Must not be null |

| lodging | total\_price\_usd | Must be numeric or flagged |

| attractions | estimated\_attraction\_cost\_total\_usd | Must be numeric or flagged |

| risk | advisory\_decision | Must not be reject |

| risk | risk\_flag | Must be false unless manually overridden |

| cost\_estimate | actual\_estimated\_trip\_cost\_usd | Must be numeric |

| benchmark | benchmark\_method | Must not be null |

| data\_quality\_flags | list | Must exist, even if empty |

| candidate\_decision | mvp\_candidate\_usable | Must be true or false |

| candidate\_decision | ready\_for\_scoring | Must be true or false |



\---



\## Search Run Matching Rules



A candidate must match the search run on:



\- Search run ID

\- Origin airport

\- Destination city

\- Destination country

\- Destination airport

\- Departure date

\- Return date

\- Traveler count



If any of these fields conflict, the candidate should be rejected or flagged for manual review.



\---



\## Date Validation Rules



A candidate passes date validation if:



\- Departure date is before return date.

\- Trip length is at least 7 days.

\- Trip length is no more than 21 days.

\- Flight dates match lodging dates.

\- Attractions/tours dates, if available, fall within the trip date range.



If activity data is unavailable, the candidate may continue with a placeholder flag.



\---



\## Flight Validation Rules



A candidate passes flight validation if:



\- Flight source is recorded.

\- Route matches origin and destination.

\- Departure and return dates match the search run.

\- Stops are recorded.

\- Durations are recorded.

\- Price is recorded or clearly flagged as uncertain.

\- The itinerary is operationally reasonable.



For MVP, flight price uncertainty is allowed only if the candidate includes:



`flight\_price\_interpretation\_needs\_verification`



\---



\## Lodging Validation Rules



A candidate passes lodging validation if:



\- Lodging source is recorded.

\- Hotel name is recorded.

\- Hotel destination matches the search run.

\- Check-in/check-out dates match the search run.

\- Total price is recorded.

\- Guest rating is recorded if available.

\- Review count is recorded if available.

\- Low-review-count risk is flagged.

\- Missing cancellation policy is flagged.

\- Missing independent review validation is flagged.



For MVP, Expedia-only lodging is allowed only if the candidate includes:



`expedia\_inventory\_only`



and, if applicable:



`tripadvisor\_validation\_unavailable`



\---



\## Attractions Validation Rules



A candidate passes attractions validation if:



\- Attractions source is recorded.

\- Estimated attractions cost is recorded.

\- Activity dates fall within the trip range if dates are available.

\- Ratings/reviews are recorded if source data is available.



For MVP, placeholder activity cost is allowed only if the candidate includes:



\- `viator\_validation\_unavailable`

\- `activity\_budget\_placeholder\_used`



\---



\## Risk Validation Rules



A candidate passes risk validation if:



\- Travel advisory source is recorded.

\- Advisory level is recorded if available.

\- Advisory decision is not reject.

\- Risk flag is false or manually overridden with justification.

\- Rejection reason is null if the candidate continues.



Automatic rejection rules:



\- Level 4 advisory

\- Active conflict risk near destination

\- Entry requirements appear infeasible

\- Destination mismatch

\- Dates mismatch

\- Hotel quality clearly poor

\- Flight itinerary clearly unreasonable



\---



\## Cost Validation Rules



A candidate passes cost validation if:



\- Flight cost is recorded or flagged.

\- Lodging cost is recorded or flagged.

\- Attractions cost is recorded or flagged.

\- Food/transport buffer is recorded or flagged.

\- Total estimated trip cost is calculated.



Formula:



`actual\_estimated\_trip\_cost\_usd = estimated\_total\_flight\_cost\_usd + hotel\_total\_price\_usd + estimated\_attraction\_cost\_total\_usd + estimated\_food\_transport\_buffer\_usd`



For MVP, placeholder costs are allowed only if flagged.



\---



\## Benchmark Validation Rules



A candidate is not ready for undervaluation scoring until benchmark fields exist.



Required benchmark fields for later scoring:



\- `fair\_value\_estimate\_usd`

\- `estimated\_discount\_pct`

\- `benchmark\_method`

\- `undervalued\_flag`



Until benchmarking is built, candidates should include:



`fair\_value\_estimate\_missing`



and should not be called undervalued.



\---



\## Candidate Decision Rules



A candidate can be marked:



`mvp\_candidate\_usable: true`



if:



\- It matches the search run.

\- It has a viable flight.

\- It has a viable lodging option.

\- It does not fail safety/risk screening.

\- Its missing data is clearly flagged.



A candidate should be marked:



`ready\_for\_scoring: false`



if:



\- Flight price basis is uncertain.

\- Benchmarking is missing.

\- Hotel validation is incomplete.

\- Attractions/tours data uses placeholders.



\---



\## Current Lisbon Candidate Status



Candidate:



`trip\_20261005\_lisbon\_001`



Current status:



`mvp\_candidate\_usable: true`



Not ready for final scoring because:



\- Flight price interpretation needs verification.

\- Tripadvisor validation is unavailable.

\- Viator validation is unavailable.

\- Activity budget is placeholder-based.

\- Fair value estimate is missing.

\- Benchmark method is not yet built.



Decision:



`valid\_interim\_candidate\_with\_caveats`



\---



\## Next Phase



Next phase:



`Phase 5.3 — Create a simple candidate validation script`



Goal:



Create a Python script that loads the Lisbon candidate YAML and checks that required sections and fields exist.

