# Tripadvisor Hotel Quality Connector Prompt

Use after Expedia finds candidate hotels.

```text
Use the Tripadvisor connector to evaluate hotel quality for:

Destination:
[PASTE_DESTINATION_CITY], [PASTE_DESTINATION_COUNTRY]

Dates:
[YYYY-MM-DD] to [YYYY-MM-DD]

Travelers:
2 adults

Purpose:
Validate hotel quality and detect whether Expedia hotel options are cheap for a bad reason.

Please search for hotel quality signals and return a structured summary with:

1. Search run ID
2. Destination
3. Hotel name
4. Tripadvisor bubble rating
5. Review count
6. Location score or location comments
7. Cleanliness comments
8. Service comments
9. Value comments
10. Common complaints
11. Common positive themes
12. Whether this hotel appears safe and reasonable for a vacation
13. Hotel quality assessment:
    - Strong
    - Acceptable
    - Weak
    - Reject

Important:
Use Tripadvisor as a hotel quality and review source, not just a price source.
Flag hotels that are cheap because of poor location, cleanliness, noise, safety, or bad reviews.
```

Suggested raw output folder:

```text
data/raw/tripadvisor/
```

Suggested filename:

```text
search_run_id_tripadvisor_destination.md
```
