\# Known Limitations



\## Purpose



This document records known limitations of the Value Vacation Finder project.



The project is intentionally being built in stages. Early versions should be treated as a structured research workflow, not as a fully automated travel booking engine.



\---



\## Current Project Stage



Current stage:



`Phase 1 — Project configuration and documentation`



Completed so far:



\- Project scaffold

\- GitHub setup

\- Traveler profile

\- Destination universe

\- Destination filter config

\- Source configuration

\- Data dictionary skeleton

\- Manual workflow document

\- Connector prompt library



Not yet completed:



\- Live connector data collection

\- Raw data storage examples

\- Data cleaning modules

\- Matching logic

\- Benchmarking logic

\- Risk filtering code

\- Scoring code

\- Final shortlist reports



\---



\## Manual Workflow Limitation



The project does not update automatically.



Data is collected only when Graham manually initiates a vacation search.



This is intentional. Travel pricing changes quickly, and the project should not run in the background unless explicitly redesigned later.



\---



\## Connector Limitation



The project currently depends on manual connector-assisted research.



Sources include:



\- Travel Advisory

\- Skyscanner

\- Expedia

\- Tripadvisor

\- Viator



At this stage, connector outputs may need to be manually copied or summarized into raw markdown files.



The project does not yet have direct automated API ingestion.



\---



\## Destination Universe Limitation



The destination universe is intentionally broad.



It includes:



\- EU capitals

\- EU major cities

\- South and Central American capitals and large cities

\- ASEAN destinations

\- Japan

\- South Korea

\- Selected African destinations



However, the MVP should not search the full universe at once.



The MVP should use `config/destination\_filter.yaml` to restrict searches to a small, controlled set of destinations.



\---



\## Airport Code Limitation



Airport codes in `config/destinations\_watchlist.yaml` should be treated as starting assumptions.



They must be validated before live searches.



Some cities use nearby practical airports rather than city-center airports.



Examples:



\- Bratislava may use Vienna as an alternate airport.

\- Nicosia may use Larnaca.

\- Kyoto may use Osaka-area airports.

\- Pretoria may use Johannesburg.



\---



\## Safety and Advisory Limitation



Travel advisory information should be checked before pricing flights, hotels, or activities.



Current conservative rule:



\- Level 1: continue

\- Level 2: continue with caution

\- Level 3: manual review / usually reject

\- Level 4: reject



The MVP should not treat a low price as attractive if the destination is cheap because of conflict, instability, health risk, or serious safety concerns.



\---



\## Visa and Entry Limitation



The project records traveler context:



\- Graham is a U.S. resident and Canadian citizen.

\- Anjali is a U.S. citizen.



However, the project does not yet automatically validate visa, passport, vaccination, or entry requirements.



These must be manually reviewed before any real booking decision.



\---



\## Price Benchmark Limitation



The project has not yet built a robust fair-value model.



Early benchmark estimates may be simple and approximate.



The first MVP may use:



\- Comparable flight prices

\- Comparable hotel nightly prices

\- Estimated activity budgets

\- Simple manual judgment



Later versions may add stronger benchmark logic.



\---



\## Scoring Limitation



The scoring model is not yet implemented in Python.



The intended scoring structure is:



\- Price undervaluation: 30 points

\- Flight quality/value: 15 points

\- Accommodation quality/value: 20 points

\- Destination attractiveness: 10 points

\- Attractions/tours value: 10 points

\- Safety/risk: 10 points

\- Practicality/friction: 5 points



Until scoring code exists, scores should be treated as draft/manual estimates.



\---



\## Data Quality Limitation



Raw connector outputs may vary in format.



Potential issues include:



\- Missing prices

\- Different currencies

\- Different date formats

\- Incomplete hotel fees

\- Unclear cancellation policies

\- Inconsistent review scores

\- Nearby-city substitutions

\- Flights and hotels that do not match the same dates



Cleaning and validation code will be needed before the project can reliably compare destinations.



\---



\## Matching Limitation



The core matching problem is not yet solved.



A valid vacation candidate must match on:



\- Same destination

\- Same country

\- Same date range

\- Same traveler count

\- Same origin airport

\- Same currency where possible



The project should reject or flag mismatches rather than silently combining unrelated data.



\---



\## Booking Limitation



This project is for research and screening only.



It does not book travel.



Before booking, Graham should manually verify:



\- Current prices

\- Total fees

\- Cancellation policy

\- Visa and entry rules

\- Passport validity

\- Travel advisories

\- Health requirements

\- Hotel location and recent reviews

\- Flight baggage and fare restrictions



\---



\## MVP Limitation



The MVP goal is modest:



Compare a small destination watchlist from Boston for one date range and produce a ranked shortlist.



The MVP is successful if it can answer:



“Which of these few destinations looks like the best value for this specific date range, after considering price, safety, lodging quality, and activities?”



The MVP does not need to solve global vacation optimization immediately.

