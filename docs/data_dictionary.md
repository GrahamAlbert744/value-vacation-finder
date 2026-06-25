\# Data Dictionary



\## Unit of Analysis



The final unit of analysis is a `vacation\_candidate`.



A `vacation\_candidate` represents one possible vacation option from Boston for two adult travelers over a fixed date range.



Each candidate should combine:



\- One destination

\- One date range

\- One round-trip flight option

\- One lodging option

\- One set of attractions or tours

\- One travel advisory / risk assessment

\- One total estimated trip cost

\- One fair value estimate

\- One final vacation score



\---



\## Core Identifiers



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| trip\_id | string | Unique ID for a candidate trip | trip\_20261005\_lisbon\_001 | Generated |

| search\_run\_id | string | Unique ID for a manual search run | run\_2026\_06\_24\_001 | Generated |

| created\_at | datetime | Timestamp when the record was created | 2026-06-24 14:30:00 | Generated |

| search\_mode | string | Type of search used | mvp\_watchlist | config/destination\_filter.yaml |



\---



\## Destination Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| origin\_city | string | Origin city | Boston | config/traveler\_profile.yaml |

| origin\_airport | string | Origin airport code | BOS | config/traveler\_profile.yaml |

| destination\_city | string | Destination city | Lisbon | config/destinations\_watchlist.yaml |

| destination\_country | string | Destination country | Portugal | config/destinations\_watchlist.yaml |

| destination\_region | string | Destination region | Europe | config/destinations\_watchlist.yaml |

| destination\_airport | string | Primary destination airport code | LIS | config/destinations\_watchlist.yaml |

| destination\_group | string | Destination category | EU capital | config/destinations\_watchlist.yaml |



\---



\## Traveler Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| traveler\_count | integer | Number of adult travelers | 2 | config/traveler\_profile.yaml |

| children\_count | integer | Number of child travelers | 0 | config/traveler\_profile.yaml |

| graham\_citizenship | string | Graham's citizenship | Canada | config/traveler\_profile.yaml |

| graham\_residency | string | Graham's residency | USA | config/traveler\_profile.yaml |

| anjali\_citizenship | string | Anjali's citizenship | USA | config/traveler\_profile.yaml |



\---



\## Date Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| departure\_date | date | Flight departure / hotel check-in date | 2026-10-05 | User input |

| return\_date | date | Flight return / hotel check-out date | 2026-10-16 | User input |

| trip\_length\_days | integer | Number of days between departure and return | 11 | Generated |

| trip\_length\_valid | boolean | Whether trip length is between 7 and 21 days | true | Generated |



\---



\## Flight Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| flight\_source | string | Source used for flight data | Skyscanner | Skyscanner |

| flight\_price\_total | float | Total round-trip flight price for all travelers | 1400.00 | Skyscanner |

| flight\_price\_per\_person | float | Round-trip flight price per traveler | 700.00 | Skyscanner |

| flight\_currency | string | Flight price currency | USD | Skyscanner |

| flight\_airline | string | Main airline or carrier | TAP Air Portugal | Skyscanner |

| flight\_stops\_outbound | integer | Number of outbound stops | 0 | Skyscanner |

| flight\_stops\_return | integer | Number of return stops | 1 | Skyscanner |

| flight\_duration\_outbound\_minutes | integer | Outbound duration in minutes | 390 | Skyscanner |

| flight\_duration\_return\_minutes | integer | Return duration in minutes | 480 | Skyscanner |

| flight\_basic\_economy\_flag | boolean | Whether fare appears to be basic economy | false | Skyscanner / Expedia |

| flight\_booking\_provider | string | Booking provider if available | Expedia | Skyscanner / Expedia |

| flight\_url | string | Booking or source URL | example\_url | Skyscanner / Expedia |



\---



\## Lodging Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| hotel\_source | string | Source used for hotel price | Expedia | Expedia |

| hotel\_quality\_source | string | Source used for hotel reviews | Tripadvisor | Tripadvisor |

| hotel\_name | string | Lodging name | Hotel Lisboa Plaza | Expedia / Tripadvisor |

| hotel\_total\_price | float | Total lodging price for full stay | 1850.00 | Expedia |

| hotel\_nightly\_price | float | Average nightly lodging price | 168.18 | Expedia |

| hotel\_currency | string | Lodging price currency | USD | Expedia |

| hotel\_review\_score | float | Review or guest score | 4.4 | Tripadvisor / Expedia |

| hotel\_review\_count | integer | Number of reviews | 1250 | Tripadvisor |

| hotel\_star\_rating | float | Hotel star rating if available | 4.0 | Expedia / Tripadvisor |

| hotel\_location\_score | float | Location quality score if available | 4.6 | Tripadvisor |

| hotel\_cancellation\_policy | string | Cancellation rule | Free cancellation | Expedia |

| hotel\_amenities | string | Key amenities | WiFi, breakfast, AC | Expedia / Tripadvisor |

| hotel\_url | string | Booking or source URL | example\_url | Expedia / Tripadvisor |



\---



\## Attractions and Tours Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| attractions\_source | string | Source used for attractions | Viator | Viator |

| top\_attractions\_count | integer | Number of relevant attractions/tours found | 12 | Viator |

| estimated\_attraction\_cost\_total | float | Estimated total activity/tour cost for two travelers | 400.00 | Viator |

| estimated\_attraction\_cost\_per\_person | float | Estimated activity/tour cost per person | 200.00 | Viator |

| top\_experience\_names | string | Names of selected representative experiences | Food tour; Sintra day trip | Viator |

| average\_experience\_rating | float | Average rating of top experiences | 4.7 | Viator |

| average\_experience\_review\_count | integer | Average review count of top experiences | 800 | Viator |

| attractions\_notes | string | Notes on destination activity quality | Strong food and history tours | Viator / manual review |



\---



\## Risk and Advisory Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| advisory\_source | string | Source used for travel advisory | Travel Advisory | Travel Advisory |

| us\_travel\_advisory\_level | integer | U.S. advisory level if available | 1 | Travel Advisory |

| advisory\_summary | string | Short advisory summary | Exercise normal precautions | Travel Advisory |

| key\_risks | string | Main risks listed | Pickpocketing, demonstrations | Travel Advisory |

| graham\_entry\_flag | string | Entry concern for Canadian citizen | No visa required | Manual / future source |

| anjali\_entry\_flag | string | Entry concern for U.S. citizen | No visa required | Manual / future source |

| risk\_flag | boolean | Whether material risk exists | false | Generated |

| rejection\_reason | string | Reason if rejected | Level 4 advisory | Generated |



\---



\## Cost and Benchmark Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| actual\_estimated\_trip\_cost | float | Flight + lodging + activities + buffer | 4050.00 | Generated |

| estimated\_food\_transport\_buffer | float | Basic estimated non-flight/lodging/activity buffer | 400.00 | Generated |

| fair\_value\_estimate | float | Estimated fair comparable trip value | 5200.00 | Benchmark logic |

| estimated\_discount\_pct | float | Estimated discount from fair value | 0.221 | Generated |

| undervalued\_flag | boolean | Whether candidate appears undervalued | true | Generated |

| benchmark\_method | string | Method used to estimate fair value | simple\_comps\_v1 | Benchmark logic |



\---



\## Score Fields



| Field | Type | Description | Example | Source |

|---|---|---|---|---|

| undervaluation\_score | float | Score for price undervaluation | 25 | Generated |

| flight\_score | float | Score for flight quality/value | 13 | Generated |

| hotel\_score | float | Score for lodging quality/value | 17 | Generated |

| attraction\_score | float | Score for attractions/tours | 8 | Generated |

| destination\_score | float | Score for destination attractiveness | 9 | Generated |

| risk\_score | float | Score for safety/risk | 9 | Generated |

| practicality\_score | float | Score for logistics/friction | 4 | Generated |

| total\_vacation\_score | float | Total score out of 100 | 85 | Generated |

| recommendation\_tier | string | Final recommendation label | Strong candidate | Generated |



\---



\## Recommendation Tiers



| Score Range | Tier |

|---|---|

| 90–100 | Exceptional value |

| 80–89 | Strong candidate |

| 70–79 | Worth considering |

| 60–69 | Marginal |

| Below 60 | Reject |



\---



\## Hard Rejection Rules



A vacation candidate should be rejected or manually reviewed if:



\- Travel advisory is Level 4.

\- Travel advisory is Level 3 unless manually overridden.

\- Trip length is below 7 days or above 21 days.

\- Flight, lodging, and attractions do not match the same destination.

\- Flight and hotel dates do not match the same date range.

\- Hotel review quality is poor.

\- The itinerary is unusually inconvenient.

\- Entry requirements appear infeasible for either traveler.

\- The trip is cheap primarily because of safety, conflict, or quality problems.

