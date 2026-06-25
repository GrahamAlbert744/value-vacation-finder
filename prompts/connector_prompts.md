\# Connector Prompt Library



This file stores reusable prompts for manually collecting travel data for the Value Vacation Finder project.



The purpose of these prompts is to keep every connector search aligned around the same:



\- Origin

\- Destination

\- Departure date

\- Return date

\- Traveler count

\- Currency

\- Search run ID



The MVP source order is:



1\. Travel Advisory

2\. Skyscanner

3\. Expedia

4\. Tripadvisor

5\. Viator



\---



\# Shared Search Context Template



Use this block at the top of every connector prompt.



```text

Project: value-vacation-finder



Search run ID:

\[PASTE\_SEARCH\_RUN\_ID]



Origin:

Boston, Massachusetts, United States



Origin airport:

BOS



Destination:

\[PASTE\_DESTINATION\_CITY], \[PASTE\_DESTINATION\_COUNTRY]



Destination airport:

\[PASTE\_DESTINATION\_AIRPORT\_CODE]



Departure date:

\[YYYY-MM-DD]



Return date:

\[YYYY-MM-DD]



Traveler count:

2 adults



Traveler context:

\- Graham is a U.S. resident and Canadian citizen.

\- Anjali is a U.S. citizen.



Currency:

USD



Trip rule:

The trip must be at least 7 days and no more than 21 days.



Important:

Use this exact destination and exact date range. Do not substitute nearby destinations, different dates, different airports, or different traveler assumptions unless explicitly noted. 





Use the Travel Advisory connector to check the current safety and travel-risk status for:



Destination country:

\[PASTE\_COUNTRY]



Traveler context:

\- Graham is a U.S. resident and Canadian citizen.

\- Anjali is a U.S. citizen.

\- The trip is for leisure/vacation.

\- Travelers are two adults.



Please return a structured summary with:



1\. Country

2\. Current U.S. travel advisory level

3\. Plain-English advisory summary

4\. Main safety concerns

5\. Whether the destination appears eligible for continued vacation planning

6\. Any notes relevant to U.S. citizens

7\. Any notes relevant to Canadian citizens, if available

8\. Conservative decision:

&#x20;  - Continue

&#x20;  - Continue with caution

&#x20;  - Manual review

&#x20;  - Reject



Use this decision rule:

\- Level 1: Continue

\- Level 2: Continue with caution

\- Level 3: Manual review / usually reject

\- Level 4: Reject



Do not evaluate flights, hotels, or attractions yet.





Use the Skyscanner connector to search for round-trip flights.



Search context:



Origin:

BOS



Destination:

\[PASTE\_DESTINATION\_AIRPORT\_CODE]



Departure date:

\[YYYY-MM-DD]



Return date:

\[YYYY-MM-DD]



Travelers:

2 adults



Cabin:

Economy



Currency:

USD



Preferences:

\- Avoid basic economy if possible.

\- Prefer reasonable total travel time.

\- Prefer no more than one stop unless nonstop is unavailable or much more expensive.

\- Do not select a terrible itinerary just because it is cheapest.



Please return a structured flight summary with:



1\. Search run ID

2\. Origin airport

3\. Destination airport

4\. Departure date

5\. Return date

6\. Airline or main carrier

7\. Number of stops outbound

8\. Number of stops return

9\. Total flight duration outbound

10\. Total flight duration return

11\. Total price for two adults

12\. Price per person

13\. Fare caveats, including basic economy if visible

14\. Booking provider if available

15\. Notes on whether this is a reasonable flight option

16\. Flight value assessment:

&#x20;   - Strong

&#x20;   - Acceptable

&#x20;   - Weak

&#x20;   - Reject



Important:

Use only the destination airport and dates listed above. Do not switch cities or dates.





Use the Expedia connector to search for hotels.



Search context:



Destination:

\[PASTE\_DESTINATION\_CITY], \[PASTE\_DESTINATION\_COUNTRY]



Check-in date:

\[YYYY-MM-DD]



Check-out date:

\[YYYY-MM-DD]



Travelers:

2 adults



Rooms:

1



Currency:

USD



Hotel preferences:

\- Good or better guest rating

\- Reasonable central location

\- Avoid poorly reviewed hotels

\- Prefer free cancellation where available

\- Prefer hotels, inns, or aparthotels over hostels

\- Do not choose the cheapest property if it appears low quality



Please return a structured hotel summary with:



1\. Search run ID

2\. Destination city and country

3\. Check-in date

4\. Check-out date

5\. Hotel name

6\. Total price for full stay

7\. Average nightly price

8\. Guest rating

9\. Star rating if available

10\. Cancellation policy if available

11\. Key amenities

12\. Location notes

13\. Booking/provider URL if available

14\. Hotel value assessment:

&#x20;   - Strong

&#x20;   - Acceptable

&#x20;   - Weak

&#x20;   - Reject



Important:

The hotel dates must exactly match the flight dates.

Do not include hotels from nearby cities unless clearly flagged.





Use the Tripadvisor connector to evaluate hotel quality for:



Destination:

\[PASTE\_DESTINATION\_CITY], \[PASTE\_DESTINATION\_COUNTRY]



Dates:

\[YYYY-MM-DD] to \[YYYY-MM-DD]



Travelers:

2 adults



Purpose:

Validate hotel quality and detect whether Expedia hotel options are cheap for a bad reason.



Please search for hotel quality signals and return a structured summary with:



1\. Search run ID

2\. Destination

3\. Hotel name

4\. Tripadvisor bubble rating

5\. Review count

6\. Location score or location comments

7\. Cleanliness comments

8\. Service comments

9\. Value comments

10\. Common complaints

11\. Common positive themes

12\. Whether this hotel appears safe and reasonable for a vacation

13\. Hotel quality assessment:

&#x20;   - Strong

&#x20;   - Acceptable

&#x20;   - Weak

&#x20;   - Reject



Important:

Use Tripadvisor as a hotel quality and review source, not just a price source.

Flag hotels that are cheap because of poor location, cleanliness, noise, safety, or bad reviews.



Use the Viator connector to search for tours, attractions, and experiences.



Destination:

\[PASTE\_DESTINATION\_CITY], \[PASTE\_DESTINATION\_COUNTRY]



Available date range:

\[YYYY-MM-DD] to \[YYYY-MM-DD]



Travelers:

2 adults



Currency:

USD



Preferences:

\- Food tours

\- Historical tours

\- Cultural experiences

\- Day trips

\- Museums or major attractions

\- Highly rated experiences

\- Reasonable cost

\- Avoid extremely expensive luxury-only experiences for the MVP



Please return a structured attractions summary with:



1\. Search run ID

2\. Destination

3\. Date range

4\. Number of relevant experiences found

5\. Top 5 to 10 experiences

6\. Price per person for each experience if available

7\. Rating for each experience

8\. Review count for each experience

9\. Duration if available

10\. Category/type

11\. Estimated realistic activity budget for two adults

12\. Notes on whether the destination has strong vacation activity value

13\. Attractions/tours assessment:

&#x20;   - Strong

&#x20;   - Acceptable

&#x20;   - Weak

&#x20;   - Reject



Important:

Activities should be relevant to the same destination and fall within the trip date range.



Review the raw connector outputs for one value-vacation-finder search run.



Search run ID:

\[PASTE\_SEARCH\_RUN\_ID]



Destination:

\[PASTE\_DESTINATION\_CITY], \[PASTE\_DESTINATION\_COUNTRY]



Date range:

\[YYYY-MM-DD] to \[YYYY-MM-DD]



Sources collected:

\- Travel Advisory

\- Skyscanner

\- Expedia

\- Tripadvisor

\- Viator



Check whether all sources match on:



1\. Same destination

2\. Same country

3\. Same date range

4\. Same traveler count

5\. Same currency where possible

6\. No obvious source mismatch

7\. No obvious safety rejection

8\. No hotel quality red flags

9\. No flight itinerary red flags



Return:



1\. Pass/fail for each source

2\. Any mismatch detected

3\. Any missing fields

4\. Whether this search run is ready for cleaning

5\. What should be fixed before moving to cleaned data



Extract structured data from the raw connector output below for the value-vacation-finder project.



Use the project data dictionary fields where possible.



Return the result as a clean table with these sections:



1\. Destination fields

2\. Date fields

3\. Flight fields

4\. Lodging fields

5\. Attractions fields

6\. Risk/advisory fields

7\. Notes and missing values



Rules:

\- Do not invent missing data.

\- Use null for missing fields.

\- Preserve source names.

\- Preserve original currency if listed.

\- Flag uncertain values.

\- Keep the same search\_run\_id.



Help me create a Python cleaning module for value-vacation-finder.



Source:

\[Skyscanner / Expedia / Tripadvisor / Viator / Travel Advisory]



Input:

Raw markdown or JSON saved in data/raw/\[source]/



Output:

A standardized pandas DataFrame saved to data/interim/\[cleaned\_source]/



Requirements:

1\. Create the file path.

2\. Give me the code.

3\. Explain the function briefly.

4\. Include basic validation.

5\. Do not overwrite raw data.

6\. Tell me how to test it.

7\. Tell me when to commit.



Help me build vacation candidates for value-vacation-finder.



A vacation candidate must include:



\- One destination

\- One date range

\- One round-trip flight option

\- One lodging option

\- One attractions/tours estimate

\- One travel advisory assessment

\- One total estimated trip cost

\- One fair value estimate placeholder

\- One score placeholder



Rules:

\- Destination must match across sources.

\- Dates must match across flights and lodging.

\- Trip length must be between 7 and 21 days.

\- Risk status must not be reject.

\- Do not silently drop mismatches; save rejected records with reasons.



Create modular Python code that can be expanded later.



Help me score vacation candidates in value-vacation-finder.



Use the scoring weights from config/scoring\_weights.yaml:



\- Price undervaluation: 30

\- Flight quality/value: 15

\- Accommodation quality/value: 20

\- Destination attractiveness: 10

\- Attractions/tours value: 10

\- Safety/risk: 10

\- Practicality/friction: 5



Return:

1\. A scoring function

2\. A recommendation tier function

3\. A ranked output table

4\. A clear explanation of each score

5\. Simple MVP logic first, not advanced machine learning



Help me create a final ranked vacation shortlist report for value-vacation-finder.



The report should include:



\- Search run ID

\- Destination

\- Dates

\- Trip length

\- Flight summary

\- Hotel summary

\- Attractions summary

\- Advisory/risk summary

\- Total estimated cost

\- Estimated fair value

\- Estimated discount percentage

\- Total score

\- Recommendation tier

\- Main caveats

\- Final decision



Create both:

1\. CSV summary

2\. Markdown report



Save outputs under reports/.

