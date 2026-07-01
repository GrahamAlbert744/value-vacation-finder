# Vacation Candidate Assembly Prompt

Use after cleaned flight, hotel, attraction, and advisory data exists.

```text
Help me build vacation candidates for value-vacation-finder.

A vacation candidate must include:

- One destination
- One date range
- One round-trip flight option
- One lodging option
- One attractions/tours estimate
- One travel advisory assessment
- One total estimated trip cost
- One fair value estimate placeholder
- One score placeholder

Rules:
- Destination must match across sources.
- Dates must match across flights and lodging.
- Trip length must be between 7 and 21 days.
- Risk status must not be reject.
- Do not silently drop mismatches; save rejected records with reasons.

Create modular Python code that can be expanded later.
```
