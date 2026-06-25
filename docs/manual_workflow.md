\# Manual Workflow



\## Purpose



This document describes the manual workflow for collecting vacation data for the Value Vacation Finder project.



The project does not update automatically. Data is only collected when Graham manually initiates a vacation search.



The goal is to avoid mixing destinations, date ranges, traveler counts, or source assumptions across connectors.



\---



\## Core Rule



Every search run must use the same:



\- Origin

\- Destination

\- Departure date

\- Return date

\- Traveler count

\- Currency

\- Search run ID



For the MVP:



\- Origin: Boston / BOS

\- Travelers: 2 adults

\- Currency: USD

\- Trip length: 7 to 21 days



\---



\## Search Run Naming Convention



Each manual run should receive a unique `search\_run\_id`.



Format:



`run\_YYYYMMDD\_destination\_startdate\_enddate`



Example:



`run\_20260624\_lisbon\_20261005\_20261016`



This ID should appear in filenames, notes, and processed outputs.



\---



\## Manual Collection Order



The MVP should collect data in this order:



1\. Travel Advisory

2\. Skyscanner

3\. Expedia

4\. Tripadvisor

5\. Viator



Travel Advisory comes first because unsafe or high-risk destinations should be rejected before spending time on flights, hotels, and activities.



\---



\## Step 1: Travel Advisory Check



Purpose:



Check whether the destination is safe enough to continue.



Record:



\- Country

\- Advisory level

\- Advisory summary

\- Main risks

\- Safety notes

\- Whether destination should continue to pricing search



Decision rule:



\- Level 1: continue

\- Level 2: continue with caution

\- Level 3: flag for manual review

\- Level 4: reject



Raw output folder:



`data/raw/travel\_advisory/`



\---



\## Step 2: Skyscanner Flight Search



Purpose:



Find flight options from BOS to the destination for the exact date range.



Record:



\- Origin airport

\- Destination airport

\- Departure date

\- Return date

\- Airline

\- Stops

\- Duration

\- Price

\- Fare type if available

\- Booking provider if available



Raw output folder:



`data/raw/skyscanner/`



Rules:



\- Use the same departure and return dates as the search run.

\- Use the same destination airport listed in the destination config.

\- Prefer reasonable flights, not just the cheapest flight.

\- Avoid basic economy where possible.



\---



\## Step 3: Expedia Hotel Search



Purpose:



Find lodging prices for the same destination and same date range.



Record:



\- Hotel name

\- Destination city

\- Check-in date

\- Check-out date

\- Total price

\- Nightly price

\- Guest rating

\- Star rating

\- Amenities

\- Cancellation policy

\- Booking URL if available



Raw output folder:



`data/raw/expedia/`



Rules:



\- Check-in date must match the flight departure date.

\- Check-out date must match the flight return date.

\- Traveler count must be 2 adults.

\- Use USD where possible.

\- Do not mix hotels from nearby cities unless intentionally documented.



\---



\## Step 4: Tripadvisor Hotel Quality Search



Purpose:



Validate hotel quality and detect options that are cheap for a bad reason.



Record:



\- Hotel name

\- Bubble rating

\- Review count

\- Location quality

\- Cleanliness

\- Service

\- Value

\- Traveler ranking

\- Review notes



Raw output folder:



`data/raw/tripadvisor/`



Rules:



\- Match hotels to the same destination.

\- Use Tripadvisor mainly as a quality and review source.

\- Do not treat a cheap hotel as a good value if reviews are poor.



\---



\## Step 5: Viator Attractions and Tours Search



Purpose:



Estimate the richness and cost of destination activities.



Record:



\- Experience names

\- Categories

\- Available dates

\- Prices

\- Ratings

\- Review counts

\- Durations

\- Booking URLs if available



Raw output folder:



`data/raw/viator/`



Rules:



\- Search the same destination.

\- Use dates within the trip date range.

\- Prioritize highly rated tours and attractions.

\- Estimate realistic activity cost for two adults.



\---



\## File Naming Convention



Use this pattern for raw saved outputs:



`search\_run\_id\_source\_destination\_startdate\_enddate.md`



Examples:



`run\_20260624\_lisbon\_20261005\_20261016\_travel\_advisory\_lisbon.md`



`run\_20260624\_lisbon\_20261005\_20261016\_skyscanner\_lisbon.md`



`run\_20260624\_lisbon\_20261005\_20261016\_expedia\_lisbon.md`



`run\_20260624\_lisbon\_20261005\_20261016\_tripadvisor\_lisbon.md`



`run\_20260624\_lisbon\_20261005\_20261016\_viator\_lisbon.md`



\---



\## Raw Data Rule



Raw data should be treated as original source evidence.



Do not overwrite raw files.



If a search is repeated, create a new file with a new timestamp or new search run ID.



\---



\## GitHub Rule



Do not commit private raw travel data, API keys, or anything that contains sensitive personal details.



Safe to commit:



\- Config files

\- Documentation

\- Source code

\- Mock/sample data

\- Data dictionaries

\- Scoring methodology



Do not commit:



\- `.env`

\- API keys

\- Raw connector outputs with personal travel details

\- Booking links tied to private session data

\- Payment or account information



\---



\## MVP Manual Workflow



For the first MVP test, use one destination and one date range.



Example:



\- Destination: Lisbon, Portugal

\- Origin: BOS

\- Departure date: 2026-10-05

\- Return date: 2026-10-16

\- Travelers: 2 adults



Run order:



1\. Check Portugal travel advisory.

2\. Pull or record BOS to LIS flight options.

3\. Pull or record Lisbon hotel options.

4\. Pull or record Lisbon hotel review/quality signals.

5\. Pull or record Lisbon tours and attractions.

6\. Build one or more vacation candidates.

7\. Score candidates.

8\. Generate a ranked shortlist.



\---



\## Completion Criteria



This workflow is complete when the project has a documented, repeatable process for collecting data from all core sources without mixing destinations, dates, or traveler assumptions.

