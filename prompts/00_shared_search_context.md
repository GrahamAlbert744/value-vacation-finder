# Shared Search Context Prompt

Use this block at the top of every connector prompt.

```text
Project: value-vacation-finder

Search run ID:
[PASTE_SEARCH_RUN_ID]

Origin:
Boston, Massachusetts, United States

Origin airport:
BOS

Destination:
[PASTE_DESTINATION_CITY], [PASTE_DESTINATION_COUNTRY]

Destination airport:
[PASTE_DESTINATION_AIRPORT_CODE]

Departure date:
[YYYY-MM-DD]

Return date:
[YYYY-MM-DD]

Traveler count:
2 adults

Traveler context:
- Graham is a U.S. resident and Canadian citizen.
- Anjali is a U.S. citizen.

Currency:
USD

Trip rule:
The trip must be at least 7 days and no more than 21 days.

Important:
Use this exact destination and exact date range. Do not substitute nearby destinations, different dates, different airports, or different traveler assumptions unless explicitly noted.
```
