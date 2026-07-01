# Connector Failure Record Prompt

Use this when a connector is blocked, returns no results, or returns ambiguous results.

```text
A connector attempt failed or returned inconclusive results for value-vacation-finder.

Search run ID:
[PASTE_SEARCH_RUN_ID]

Connector/source:
[Travel Advisory / Skyscanner / Expedia / Tripadvisor / Viator]

Destination:
[PASTE_DESTINATION_CITY], [PASTE_DESTINATION_COUNTRY]

Date range:
[YYYY-MM-DD] to [YYYY-MM-DD]

Traveler count:
2 adults

What happened:
[DESCRIBE FAILURE]

Please create a structured raw-note summary with:

1. Source
2. Search run ID
3. Destination
4. Date range
5. Search intent
6. Result status
7. Why this is inconclusive
8. Whether this should reject the destination
9. Recommended project decision
10. Data quality flag to carry forward
11. Follow-up needed later

Important:
Do not invent missing data. Do not reject a vacation solely because one validation connector failed unless the failure itself reveals a safety, quality, or feasibility problem.
```
