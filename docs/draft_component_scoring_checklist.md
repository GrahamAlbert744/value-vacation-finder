\# Draft Component Scoring Checklist



\## Purpose



This checklist determines whether a vacation candidate has enough information to receive draft component scores.



This document does not implement scoring code.



It exists to prevent the project from scoring incomplete candidates as if they were fully validated.



\---



\## Important MVP Rule



The project should not produce:



\- Final total vacation score

\- Final recommendation tier

\- Final undervalued label



until benchmarking and fair-value estimation are built.



Draft component scores may be allowed for testing only if all caveats are preserved.



\---



\## Candidate Under Review



Current sample candidate:



`sample\_trip\_20261005\_lisbon\_001`



Current status:



\- MVP usable: true

\- Ready for scoring: false

\- Ready for benchmarking: false



Reason:



The candidate has enough structure for testing, but not enough validated data for final scoring.



\---



\# Overall Scoring Readiness Checklist



A candidate can move toward draft component scoring only if:



\- \[ ] Candidate schema validates

\- \[ ] Search run ID is present

\- \[ ] Origin is present

\- \[ ] Destination is present

\- \[ ] Date range is present

\- \[ ] Trip length is between 7 and 21 days

\- \[ ] Traveler count is present

\- \[ ] Flight section exists

\- \[ ] Lodging section exists

\- \[ ] Attractions section exists

\- \[ ] Risk section exists

\- \[ ] Cost estimate section exists

\- \[ ] Benchmark section exists

\- \[ ] Data quality flags are preserved

\- \[ ] Candidate decision fields exist



Current Lisbon sample status:



`partial\_pass`



Reason:



The candidate has the required structure, but several scoring inputs are placeholders or incomplete.



\---



\# Component 1 — Price Undervaluation



Weight:



`30 points`



Current status:



`not\_ready`



\## Required Inputs



\- \[ ] actual\_estimated\_trip\_cost\_usd

\- \[ ] fair\_value\_estimate\_usd

\- \[ ] estimated\_discount\_pct

\- \[ ] benchmark\_method

\- \[ ] undervalued\_flag



\## Readiness Rules



This component is ready only if:



\- \[ ] Fair-value estimate exists

\- \[ ] Benchmark method exists

\- \[ ] Estimated discount percentage exists

\- \[ ] Benchmark method is documented

\- \[ ] Benchmark method has been tested



\## Current Lisbon Sample Status



\- actual estimated trip cost exists

\- fair value estimate is missing

\- estimated discount percentage is missing

\- benchmark method is `not\_yet\_built`



Decision:



`not\_ready`



Required flag:



`fair\_value\_estimate\_missing`



Rule:



Do not calculate price undervaluation score yet.



\---



\# Component 2 — Flight Quality / Value



Weight:



`15 points`



Current status:



`draft\_possible\_with\_caveats`



\## Required Inputs



\- \[ ] flight\_source

\- \[ ] flight\_route

\- \[ ] flight\_airline

\- \[ ] outbound\_stops

\- \[ ] return\_stops

\- \[ ] outbound\_duration\_minutes

\- \[ ] return\_duration\_minutes

\- \[ ] listed\_flight\_price\_usd

\- \[ ] estimated\_total\_flight\_cost\_usd

\- \[ ] flight\_price\_interpretation

\- \[ ] assumed\_price\_basis\_for\_mvp



\## Readiness Rules



This component can receive a draft score if:



\- \[ ] Route matches search run

\- \[ ] Dates match search run

\- \[ ] Stop counts are recorded

\- \[ ] Durations are recorded

\- \[ ] Price is recorded

\- \[ ] Price uncertainty is flagged if unresolved



\## Current Lisbon Sample Status



\- Flight route exists

\- Airline exists

\- Stop counts exist

\- Duration fields exist

\- Price exists

\- Price basis needs verification



Decision:



`draft\_possible\_with\_caveat`



Required flag:



`flight\_price\_interpretation\_needs\_verification`



Rule:



A draft flight score may be created later, but it cannot be treated as final until price basis is verified.



\---



\# Component 3 — Lodging Quality / Value



Weight:



`20 points`



Current status:



`draft\_possible\_with\_caveats`



\## Required Inputs



\- \[ ] lodging\_source

\- \[ ] hotel\_name

\- \[ ] hotel\_total\_price\_usd

\- \[ ] hotel\_nightly\_price\_usd

\- \[ ] hotel\_guest\_rating

\- \[ ] hotel\_review\_count

\- \[ ] lodging\_validation\_source

\- \[ ] tripadvisor\_validation\_status

\- \[ ] hotel\_cancellation\_policy\_status

\- \[ ] hotel\_location\_quality\_status



\## Readiness Rules



This component can receive a draft score if:



\- \[ ] Hotel name exists

\- \[ ] Hotel price exists

\- \[ ] Guest rating exists

\- \[ ] Review count exists

\- \[ ] Missing validation is clearly flagged

\- \[ ] Cancellation-policy status is clearly flagged

\- \[ ] Location-quality status is clearly flagged



\## Current Lisbon Sample Status



\- Expedia lodging data exists

\- Hotel name exists

\- Guest rating exists

\- Review count exists

\- Tripadvisor validation unavailable

\- Cancellation policy missing

\- Location quality missing



Decision:



`draft\_possible\_with\_caveats`



Required flags:



\- `tripadvisor\_validation\_unavailable`

\- `hotel\_cancellation\_policy\_missing`

\- `hotel\_location\_quality\_missing`

\- `expedia\_inventory\_only`



Rule:



A draft lodging score may be created later, but missing validation must reduce confidence.



\---



\# Component 4 — Destination Attractiveness



Weight:



`10 points`



Current status:



`draft\_possible`



\## Required Inputs



\- \[ ] destination\_city

\- \[ ] destination\_country

\- \[ ] destination\_region

\- \[ ] departure\_date

\- \[ ] return\_date

\- \[ ] trip\_length\_days



\## Readiness Rules



This component can receive a draft score if:



\- \[ ] Destination is known

\- \[ ] Date range is known

\- \[ ] Trip length is valid

\- \[ ] Seasonality can be assessed

\- \[ ] Destination fit can be documented



\## Current Lisbon Sample Status



\- Destination exists

\- Country exists

\- Region exists

\- Dates exist

\- Trip length is valid



Decision:



`draft\_possible`



Rule:



A draft destination attractiveness score can be created later, but it should remain partly subjective and documented.



\---



\# Component 5 — Attractions / Activity Value



Weight:



`10 points`



Current status:



`not\_ready`



\## Required Inputs



\- \[ ] attractions\_source

\- \[ ] estimated\_attraction\_cost\_total\_usd

\- \[ ] viator\_validation\_status

\- \[ ] activity\_budget\_method

\- \[ ] activity names

\- \[ ] activity prices

\- \[ ] activity ratings

\- \[ ] activity review counts

\- \[ ] activity date availability



\## Readiness Rules



This component is ready only if:



\- \[ ] At least some real activity options exist

\- \[ ] Prices are source-based

\- \[ ] Ratings are source-based

\- \[ ] Review counts are source-based

\- \[ ] Activities are available during the trip dates



\## Current Lisbon Sample Status



\- Attractions source is placeholder

\- Viator validation unavailable

\- Activity budget is placeholder-based

\- Real activities are not listed



Decision:



`not\_ready`



Required flags:



\- `viator\_validation\_unavailable`

\- `activity\_budget\_placeholder\_used`



Rule:



Do not calculate final activity score yet.



\---



\# Component 6 — Safety / Travel Advisory Risk



Weight:



`10 points`



Current status:



`draft\_possible\_with\_caveat`



\## Required Inputs



\- \[ ] risk\_source

\- \[ ] advisory\_country

\- \[ ] us\_travel\_advisory\_level

\- \[ ] us\_travel\_advisory\_label

\- \[ ] advisory\_decision

\- \[ ] risk\_flag

\- \[ ] rejection\_reason

\- \[ ] canada\_travel\_advisory\_level

\- \[ ] canada\_travel\_advisory\_label



\## Readiness Rules



This component can receive a draft score if:



\- \[ ] U.S. advisory status exists

\- \[ ] Advisory decision exists

\- \[ ] Risk flag exists

\- \[ ] No hard rejection is triggered



This component is not fully ready until:



\- \[ ] Canadian advisory status is added

\- \[ ] Regional conflict/security context is checked

\- \[ ] Entry/exit risks are checked for both travelers



\## Current Lisbon Sample Status



\- U.S. advisory exists

\- Advisory level is 1

\- Advisory decision is continue

\- Risk flag is false

\- Canadian advisory not yet implemented



Decision:



`draft\_possible\_with\_caveat`



Rule:



A draft safety score may be created later, but full risk scoring should eventually include both U.S. and Canadian advisory checks.



\---



\# Component 7 — Practicality / Friction



Weight:



`5 points`



Current status:



`not\_ready`



\## Required Inputs



\- \[ ] visa\_entry\_status

\- \[ ] passport\_requirement\_status

\- \[ ] traveler\_citizenship\_context

\- \[ ] language\_or\_logistics\_notes

\- \[ ] visa\_required\_graham

\- \[ ] visa\_required\_anjali

\- \[ ] passport\_validity\_requirement

\- \[ ] airport transfer or local transit note



\## Readiness Rules



This component is ready only if:



\- \[ ] Entry requirements are checked for Canadian passport holder

\- \[ ] Entry requirements are checked for U.S. passport holder

\- \[ ] Passport validity requirements are recorded

\- \[ ] Major logistics issues are recorded



\## Current Lisbon Sample Status



\- Traveler citizenship context exists

\- Entry requirement fields are not fully structured

\- Passport validity requirement is missing

\- Local logistics are not yet documented



Decision:



`not\_ready`



Rule:



Do not calculate final practicality score yet.



\---



\# Current Component Readiness Summary



| Component | Points | Current Status | Decision |

|---|---:|---|---|

| Price undervaluation | 30 | Not ready | Do not score |

| Flight quality/value | 15 | Draft possible with caveat | Can draft later |

| Lodging quality/value | 20 | Draft possible with caveats | Can draft later |

| Destination attractiveness | 10 | Draft possible | Can draft later |

| Attractions/activity value | 10 | Not ready | Do not score |

| Safety/travel advisory risk | 10 | Draft possible with caveat | Can draft later |

| Practicality/friction | 5 | Not ready | Do not score |



\---



\# Current Lisbon Sample Decision



Current decision:



`not\_ready\_for\_total\_score`



Reason:



The candidate is missing:



\- Benchmark/fair-value estimate

\- Final flight price verification

\- Tripadvisor hotel validation

\- Viator activity validation

\- Structured practicality and entry requirement fields

\- Canadian advisory/entry requirement checks



However, the candidate is useful for:



\- Schema validation

\- Candidate flattening

\- Processed-row generation

\- Draft scoring design

\- Future scoring-code tests



\---



\# Required Flags Before Any Draft Score



The following flags must remain attached to the Lisbon sample candidate:



\- `flight\_price\_interpretation\_needs\_verification`

\- `tripadvisor\_validation\_unavailable`

\- `viator\_validation\_unavailable`

\- `activity\_budget\_placeholder\_used`

\- `hotel\_cancellation\_policy\_missing`

\- `hotel\_location\_quality\_missing`

\- `expedia\_inventory\_only`

\- `food\_transport\_buffer\_placeholder`

\- `fair\_value\_estimate\_missing`

\- `sample\_record\_not\_for\_booking`



\---



\# Rule for Future Scoring Code



Future scoring code must not silently ignore missing data.



If a scoring input is missing, the code should either:



1\. Refuse to score that component, or

2\. Return a draft score with an explicit caveat.



Missing data should never be treated as zero-risk or fully valid.



\---



\# Next Phase



Next phase:



`Phase 6.5 — Create a scoring readiness check script`



Goal:



Create a lightweight Python script that reads the sample processed candidate CSV and reports which scoring components are ready, draft-ready, or not ready.

