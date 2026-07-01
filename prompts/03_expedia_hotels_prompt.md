# Expedia Hotels Connector Prompt

Use after the flight search.

```text
Use the Expedia connector to search for hotels.

Search context:

Destination:
[PASTE_DESTINATION_CITY], [PASTE_DESTINATION_COUNTRY]

Check-in date:
[YYYY-MM-DD]

Check-out date:
[YYYY-MM-DD]

Travelers:
2 adults

Rooms:
1

Currency:
USD

Hotel preferences:
- Good or better guest rating
- Reasonable central location
- Avoid poorly reviewed hotels
- Prefer free cancellation where available
- Prefer hotels, inns, or aparthotels over hostels
- Do not choose the cheapest property if it appears low quality

Please return a structured hotel summary with:

1. Search run ID
2. Destination city and country
3. Check-in date
4. Check-out date
5. Hotel name
6. Total price for full stay
7. Average nightly price
8. Guest rating
9. Star rating if available
10. Cancellation policy if available
11. Key amenities
12. Location notes
13. Booking/provider URL if available
14. Hotel value assessment:
    - Strong
    - Acceptable
    - Weak
    - Reject

Important:
The hotel dates must exactly match the flight dates.
Do not include hotels from nearby cities unless clearly flagged.
```

Suggested raw output folder:

```text
data/raw/expedia/
```

Suggested filename:

```text
search_run_id_expedia_destination.md
```
