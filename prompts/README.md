# Value Vacation Finder Prompt Library

Copy this entire `prompts/` folder into the root of your local `value-vacation-finder` project.

Recommended destination:

```text
C:\Users\graha\Documents\Data_Projects\value-vacation-finder\prompts\
```

These prompts are reusable project prompts for connector-assisted data collection, raw-data review, candidate creation, validation, scoring, and reporting.

## How to use

1. Open the relevant `.md` prompt file.
2. Copy the prompt text.
3. Replace bracketed placeholders such as `[PASTE_SEARCH_RUN_ID]`, `[YYYY-MM-DD]`, or `[PASTE_DESTINATION_CITY]`.
4. Paste into ChatGPT or the relevant connector workflow.
5. Save resulting notes under the appropriate `data/raw/`, `data/interim/`, `docs/`, or `reports/` location.

## GitHub safety

These prompt files are safe to commit.

Do not commit:

- `.env`
- API keys
- booking links tied to private sessions
- raw connector outputs with private details
- payment or account information
