# Skyscanner Flights Connector Prompt

Use after the Travel Advisory check passes.

```text
Use the Skyscanner connector to search for round-trip flights.

Search context:

Origin:
BOS

Destination:
[PASTE_DESTINATION_AIRPORT_CODE]

Departure date:
[YYYY-MM-DD]

Return date:
[YYYY-MM-DD]

Travelers:
2 adults

Cabin:
Economy

Currency:
USD

Preferences:
- Avoid basic economy if possible.
- Prefer reasonable total travel time.
- Prefer no more than one stop unless nonstop is unavailable or much more expensive.
- Do not select a terrible itinerary just because it is cheapest.

Please return a structured flight summary with:

1. Search run ID
2. Origin airport
3. Destination airport
4. Departure date
5. Return date
6. Airline or main carrier
7. Number of stops outbound
8. Number of stops return
9. Total flight duration outbound
10. Total flight duration return
11. Total price for two adults
12. Price per person
13. Fare caveats, including basic economy if visible
14. Booking provider if available
15. Notes on whether this is a reasonable flight option
16. Flight value assessment:
    - Strong
    - Acceptable
    - Weak
    - Reject

Important:
Use only the destination airport and dates listed above. Do not switch cities or dates.
```

Suggested raw output folder:

```text
data/raw/skyscanner/
```

Suggested filename:

```text
search_run_id_skyscanner_destination.md
```
