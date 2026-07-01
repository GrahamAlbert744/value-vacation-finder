# Travel Advisory Connector Prompt

Use this first before searching flights or hotels.

```text
Use the Travel Advisory connector to check the current safety and travel-risk status for:

Destination country:
[PASTE_COUNTRY]

Traveler context:
- Graham is a U.S. resident and Canadian citizen.
- Anjali is a U.S. citizen.
- The trip is for leisure/vacation.
- Travelers are two adults.

Please return a structured summary with:

1. Country
2. Current U.S. travel advisory level
3. Plain-English advisory summary
4. Main safety concerns
5. Whether the destination appears eligible for continued vacation planning
6. Any notes relevant to U.S. citizens
7. Any notes relevant to Canadian citizens, if available
8. Conservative decision:
   - Continue
   - Continue with caution
   - Manual review
   - Reject

Use this decision rule:
- Level 1: Continue
- Level 2: Continue with caution
- Level 3: Manual review / usually reject
- Level 4: Reject

Do not evaluate flights, hotels, or attractions yet.
```

Suggested raw output folder:

```text
data/raw/travel_advisory/
```

Suggested filename:

```text
search_run_id_travel_advisory_destination.md
```
