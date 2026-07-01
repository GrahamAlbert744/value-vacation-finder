\# Processed Candidate Schema Plan



\## Purpose



This document defines the planned structure for the processed `vacation\_candidates` dataset.



The goal is to convert manually structured candidate YAML files into a flatter, analysis-ready table that can later be scored, benchmarked, ranked, and reported.



This is a planning document only. It does not create the processed dataset yet.



\---



\## Dataset Name



Planned processed dataset:



`data/processed/vacation\_candidates/vacation\_candidates.csv`



Optional later format:



`data/processed/vacation\_candidates/vacation\_candidates.parquet`



\---



\## Unit of Analysis



Each row represents one vacation candidate.



A vacation candidate combines:



\- One origin

\- One destination

\- One date range

\- One traveler count

\- One flight option

\- One lodging option

\- One attractions/tours estimate

\- One travel advisory/risk result

\- One total estimated trip cost

\- One benchmark/fair-value estimate or placeholder

\- One scoring status or score



\---



\## Required Identity Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| trip\_id | string | yes | Unique vacation candidate ID |

| search\_run\_id | string | yes | Links candidate to manual search run |

| candidate\_status | string | yes | Example: mvp\_manual\_candidate |

| destination\_slug | string | yes | Lowercase destination key |

| created\_at | date/string | yes | Candidate creation date |



\---



\## Origin and Destination Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| origin\_city | string | yes | MVP default: Boston |

| origin\_airport | string | yes | MVP default: BOS |

| origin\_country | string | yes | MVP default: United States |

| destination\_city | string | yes | Example: Lisbon |

| destination\_country | string | yes | Example: Portugal |

| destination\_airport | string | yes | Example: LIS |

| destination\_region | string | no | Example: Europe |

| destination\_group | string | no | Example: EU capital |



\---



\## Date and Traveler Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| departure\_date | date/string | yes | Flight departure / hotel check-in |

| return\_date | date/string | yes | Flight return / hotel check-out |

| trip\_length\_days | integer | yes | Must be 7 to 21 |

| trip\_length\_valid | boolean | yes | Must be true for MVP |

| adults | integer | yes | MVP default: 2 |

| children | integer | yes | MVP default: 0 |

| traveler\_count | integer | yes | Adults + children |



\---



\## Flight Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| flight\_source | string | yes | Example: Skyscanner |

| flight\_route | string | yes | Example: BOS-LIS |

| flight\_airline | string | no | Main carrier |

| outbound\_stops | integer | yes | Number of outbound stops |

| return\_stops | integer | yes | Number of return stops |

| outbound\_duration\_minutes | integer | yes | Outbound flight duration |

| return\_duration\_minutes | integer | yes | Return flight duration |

| listed\_flight\_price\_usd | float | yes | Raw listed price |

| flight\_price\_interpretation | string | yes | Example: NEEDS\_VERIFICATION |

| assumed\_price\_basis\_for\_mvp | string | yes | Example: per\_person |

| estimated\_total\_flight\_cost\_usd | float | yes | Estimated total for travelers |

| flight\_quality\_assessment | string | no | Example: strong |



\---



\## Lodging Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| lodging\_source | string | yes | Example: Expedia |

| hotel\_name | string | yes | Selected lodging |

| hotel\_guest\_rating | float | no | Source rating |

| hotel\_review\_count | integer | no | Review count |

| hotel\_star\_rating | float | no | Star rating |

| hotel\_nightly\_price\_usd | float | yes | Average nightly price |

| hotel\_total\_price\_usd | float | yes | Total stay price |

| lodging\_quality\_assessment | string | no | Example: strong\_value\_candidate |

| lodging\_validation\_source | string | yes | Example: Expedia only |

| tripadvisor\_validation\_status | string | yes | Example: unavailable |

| hotel\_cancellation\_policy\_status | string | yes | Example: missing |

| hotel\_location\_quality\_status | string | yes | Example: needs\_manual\_validation |



\---



\## Attractions Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| attractions\_source | string | yes | Example: placeholder or Viator |

| viator\_validation\_status | string | yes | Example: unavailable |

| estimated\_attraction\_cost\_per\_person\_usd | float | yes | MVP placeholder allowed |

| estimated\_attraction\_cost\_total\_usd | float | yes | Total for travelers |

| activity\_budget\_method | string | yes | Example: conservative\_placeholder |



\---



\## Risk and Advisory Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| risk\_source | string | yes | Example: Travel Advisory connector |

| advisory\_country | string | yes | Example: Portugal |

| us\_travel\_advisory\_level | integer/string | yes | Example: 1 |

| us\_travel\_advisory\_label | string | yes | Example: Exercise Normal Precautions |

| advisory\_decision | string | yes | Must not be reject |

| risk\_flag | boolean | yes | False if continuing |

| rejection\_reason | string/null | no | Null if not rejected |

| canada\_travel\_advisory\_status | string | no | Not yet implemented |

| visa\_entry\_status | string | no | Not yet implemented |

| passport\_requirement\_status | string | no | Not yet implemented |



\---



\## Cost Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| estimated\_total\_flight\_cost\_usd | float | yes | Total estimated flights |

| hotel\_total\_price\_usd | float | yes | Total lodging |

| estimated\_attraction\_cost\_total\_usd | float | yes | Total activities |

| estimated\_food\_transport\_buffer\_usd | float | yes | Placeholder allowed |

| actual\_estimated\_trip\_cost\_usd | float | yes | Sum of cost components |

| cost\_estimate\_status | string | yes | Example: draft |



Formula:



`actual\_estimated\_trip\_cost\_usd = estimated\_total\_flight\_cost\_usd + hotel\_total\_price\_usd + estimated\_attraction\_cost\_total\_usd + estimated\_food\_transport\_buffer\_usd`



\---



\## Benchmark Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| fair\_value\_estimate\_usd | float/null | no | Not built yet |

| estimated\_discount\_pct | float/null | no | Not built yet |

| benchmark\_method | string | yes | Example: not\_yet\_built |

| undervalued\_flag | boolean/null | no | Null until benchmark exists |



A candidate should not be called undervalued until these fields are implemented.



\---



\## Scoring Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| undervaluation\_score | float/null | no | Later scoring field |

| flight\_score | float/null | no | Later scoring field |

| lodging\_score | float/null | no | Later scoring field |

| destination\_score | float/null | no | Later scoring field |

| attractions\_score | float/null | no | Later scoring field |

| risk\_score | float/null | no | Later scoring field |

| practicality\_score | float/null | no | Later scoring field |

| total\_vacation\_score | float/null | no | Later scoring field |

| recommendation\_tier | string/null | no | Later reporting field |

| ready\_for\_scoring | boolean | yes | False until scoring is ready |

| ready\_for\_benchmarking | boolean | yes | False until benchmark is ready |



\---



\## Data Quality Fields



| Field | Type | Required | Notes |

|---|---|---:|---|

| data\_quality\_flags | list/string | yes | Store as pipe-separated string in CSV |

| has\_flight\_price\_uncertainty | boolean | yes | Derived from flags |

| has\_missing\_hotel\_validation | boolean | yes | Derived from flags |

| has\_placeholder\_activity\_budget | boolean | yes | Derived from flags |

| has\_missing\_benchmark | boolean | yes | Derived from flags |

| mvp\_candidate\_usable | boolean | yes | True/false |

| candidate\_summary | string | no | Short decision summary |



\---



\## Data Quality Flag Handling



In YAML, `data\_quality\_flags` can be a list.



In CSV, store it as a pipe-separated string.



Example:



`flight\_price\_interpretation\_needs\_verification|tripadvisor\_validation\_unavailable|fair\_value\_estimate\_missing`



Derived boolean fields should be created later for easier filtering.



\---



\## First Processed Row Source



The first processed row should be created from:



`data/interim/manual\_candidates/lisbon\_candidate\_001.yaml`



If the local interim candidate is unavailable, use the GitHub-safe sample candidate as a test input:



`references/sample\_candidates/sample\_lisbon\_candidate.yaml`



\---



\## Acceptance Criteria for Phase 5.6



This phase is complete when:



\- The processed schema is documented.

\- Required flat fields are defined.

\- Cost formula is documented.

\- Benchmark/scoring placeholders are clearly marked.

\- Data quality flags are preserved.

\- The next coding step is clear.



\---



\## Next Phase



Next phase:



`Phase 5.7 — Create a script to flatten candidate YAML into a processed-style row`



Goal:



Create a Python script that reads a candidate YAML file and outputs a flattened dictionary or CSV row using the schema described here.

