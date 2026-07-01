# Combined Raw Data Review Prompt

Use after collecting all connector outputs for one destination.

```text
Review the raw connector outputs for one value-vacation-finder search run.

Search run ID:
[PASTE_SEARCH_RUN_ID]

Destination:
[PASTE_DESTINATION_CITY], [PASTE_DESTINATION_COUNTRY]

Date range:
[YYYY-MM-DD] to [YYYY-MM-DD]

Sources collected:
- Travel Advisory
- Skyscanner
- Expedia
- Tripadvisor
- Viator

Check whether all sources match on:

1. Same destination
2. Same country
3. Same date range
4. Same traveler count
5. Same currency where possible
6. No obvious source mismatch
7. No obvious safety rejection
8. No hotel quality red flags
9. No flight itinerary red flags

Return:

1. Pass/fail for each source
2. Any mismatch detected
3. Any missing fields
4. Whether this search run is ready for cleaning
5. What should be fixed before moving to cleaned data
```
