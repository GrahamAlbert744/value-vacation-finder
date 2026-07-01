# Viator Attractions and Tours Connector Prompt

Use after lodging quality is acceptable.

```text
Use the Viator connector to search for tours, attractions, and experiences.

Destination:
[PASTE_DESTINATION_CITY], [PASTE_DESTINATION_COUNTRY]

Available date range:
[YYYY-MM-DD] to [YYYY-MM-DD]

Travelers:
2 adults

Currency:
USD

Preferences:
- Food tours
- Historical tours
- Cultural experiences
- Day trips
- Museums or major attractions
- Highly rated experiences
- Reasonable cost
- Avoid extremely expensive luxury-only experiences for the MVP

Please return a structured attractions summary with:

1. Search run ID
2. Destination
3. Date range
4. Number of relevant experiences found
5. Top 5 to 10 experiences
6. Price per person for each experience if available
7. Rating for each experience
8. Review count for each experience
9. Duration if available
10. Category/type
11. Estimated realistic activity budget for two adults
12. Notes on whether the destination has strong vacation activity value
13. Attractions/tours assessment:
    - Strong
    - Acceptable
    - Weak
    - Reject

Important:
Activities should be relevant to the same destination and fall within the trip date range.
```

Suggested raw output folder:

```text
data/raw/viator/
```

Suggested filename:

```text
search_run_id_viator_destination.md
```
