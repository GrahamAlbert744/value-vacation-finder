# Data Extraction from Raw Notes Prompt

Use this when converting raw connector notes into a structured table.

```text
Extract structured data from the raw connector output below for the value-vacation-finder project.

Use the project data dictionary fields where possible.

Return the result as a clean table with these sections:

1. Destination fields
2. Date fields
3. Flight fields
4. Lodging fields
5. Attractions fields
6. Risk/advisory fields
7. Notes and missing values

Rules:
- Do not invent missing data.
- Use null for missing fields.
- Preserve source names.
- Preserve original currency if listed.
- Flag uncertain values.
- Keep the same search_run_id.
```
