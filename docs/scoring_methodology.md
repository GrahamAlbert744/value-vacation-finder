\# Scoring Methodology



\## Purpose



This document explains the draft scoring framework for Value Vacation Finder.



The scoring framework is designed to evaluate vacation candidates using a 100-point system.



Important rule:



A vacation candidate should not be called \*\*undervalued\*\* until fair-value benchmarking is implemented.



\---



\## Total Score



The planned total score is:



`100 points`



Current scoring categories:



| Category | Points | Current Status |

|---|---:|---|

| Price undervaluation | 30 | Not ready |

| Flight quality/value | 15 | Draft |

| Lodging quality/value | 20 | Draft |

| Destination attractiveness | 10 | Draft |

| Attractions/activity value | 10 | Not ready |

| Safety/travel advisory risk | 10 | Draft |

| Practicality/friction | 5 | Draft |



\---



\## Why Price Undervaluation Gets the Most Weight



The project is built around the idea of finding undervalued vacations.



That means the most important question is:



`Is this trip meaningfully cheaper than comparable trips of similar quality?`



However, this cannot be answered honestly until the project has a benchmark or fair-value estimate.



Until then:



\- No final undervaluation score.

\- No final total vacation score.

\- No final recommendation tier.

\- No claim that a vacation is undervalued.



\---



\## Category 1 — Price Undervaluation



Weight:



`30 points`



Purpose:



Compare actual estimated trip cost against fair-value trip cost.



Formula planned:



`estimated\_discount\_pct = (fair\_value\_estimate\_usd - actual\_estimated\_trip\_cost\_usd) / fair\_value\_estimate\_usd`



This category requires:



\- Actual estimated trip cost

\- Fair-value estimate

\- Benchmark method

\- Estimated discount percentage



Current status:



`not\_ready`



Reason:



Benchmarking has not been built yet.



\---



\## Category 2 — Flight Quality / Value



Weight:



`15 points`



Flight score should consider:



\- Price reasonableness

\- Stop count

\- Total travel duration

\- Basic economy or fare restrictions

\- Schedule practicality



Important caveat:



A cheap flight is not necessarily a good flight.



A flight may be cheap because it has bad timing, long layovers, restrictive fare rules, or inconvenient routing.



\---



\## Category 3 — Lodging Quality / Value



Weight:



`20 points`



Lodging score should consider:



\- Total hotel price

\- Nightly price

\- Guest rating

\- Review count

\- Location quality

\- Cancellation policy

\- Independent validation

\- Amenities and room quality



Important caveat:



A cheap hotel is not necessarily a good value.



A hotel may be cheap because it has weak reviews, bad location, poor cancellation policy, hidden fees, or poor room quality.



\---



\## Category 4 — Destination Attractiveness



Weight:



`10 points`



Destination score should consider:



\- Weather and seasonality

\- Food, culture, history, and nature

\- Ease of getting around

\- Fit with trip length

\- Personal interest or uniqueness



This is partly subjective, but the project should still document why a destination receives a high or low score.



\---



\## Category 5 — Attractions / Activity Value



Weight:



`10 points`



Activity score should consider:



\- Number of good activities

\- Review quality

\- Cost reasonableness

\- Date availability

\- Variety



Current status:



`not\_ready`



Reason:



The Lisbon MVP currently uses a placeholder activity budget because Viator validation was unavailable.



Placeholder activity budgets are acceptable for pipeline testing but should not receive final activity scores.



\---



\## Category 6 — Safety / Travel Advisory Risk



Weight:



`10 points`



Safety score should consider:



\- U.S. travel advisory level

\- Canadian travel advisory status

\- Regional conflict/security issues

\- Health, disaster, or civil unrest alerts

\- Overall destination risk



Draft scoring:



| Advisory Level | Score | Decision |

|---|---:|---|

| Level 1 | 10 | Continue |

| Level 2 | 7 | Continue with caution |

| Level 3 | 2 | Usually reject or manual review |

| Level 4 | 0 | Automatic reject |



Current limitation:



Canadian advisory checks are not yet implemented.



This matters because Graham is a Canadian citizen and Anjali is a U.S. citizen.



\---



\## Category 7 — Practicality / Friction



Weight:



`5 points`



Practicality score should consider:



\- Visa requirements

\- Passport validity requirements

\- Local transportation

\- Language/logistics

\- Travel insurance concerns



Current limitation:



Visa and passport requirement checks are not yet implemented.



\---



\## Hard Rejection Rules



A trip should be rejected if any of the following are true:



\- Level 4 travel advisory

\- Active conflict risk is high

\- Destination/date mismatch

\- Trip length is outside 7 to 21 days

\- Traveler count mismatch

\- Flight itinerary is unreasonable

\- Lodging quality is clearly poor

\- Entry requirements are infeasible

\- Total cost is not below benchmark once benchmarking exists



\---



\## Recommendation Tiers



Future recommendation tiers:



| Score | Tier |

|---:|---|

| 90–100 | Exceptional value |

| 80–89 | Strong candidate |

| 70–79 | Worth considering |

| 60–69 | Only if destination is personally exciting |

| Below 60 | Reject |



These tiers should not be used for final recommendations until benchmark logic exists.



\---



\## MVP Scoring Policy



During the MVP:



\- Draft component scores are allowed.

\- Final total scores are not allowed.

\- Final recommendation tiers are not allowed.

\- “Undervalued” labels are not allowed.



Reason:



Fair-value benchmarking has not been implemented.



\---



\## Next Phase



Next phase:



`Phase 6.2 — Create a scoring config validation script`



Goal:



Create a lightweight Python script that verifies:



\- Scoring weights sum to 100.

\- Required scoring categories exist.

\- Recommendation tiers exist.

\- MVP policy blocks final undervaluation labels before benchmarking.

