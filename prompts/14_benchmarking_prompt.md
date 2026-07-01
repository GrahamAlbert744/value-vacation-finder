# Benchmarking Methodology Prompt

Use this when beginning fair-value / undervaluation logic.

```text
Help me design a simple MVP benchmarking method for value-vacation-finder.

Goal:
Estimate whether a vacation candidate appears under-valued by comparing actual estimated trip cost to a fair-value estimate for comparable trips.

Inputs:
- Flight cost
- Hotel cost
- Activity budget
- Food/transport buffer
- Destination
- Date range
- Trip length
- Hotel quality/rating
- Flight quality/stops/duration
- Safety/advisory status

Please return:

1. A simple fair-value methodology suitable for MVP.
2. Which fields are needed.
3. Which fields are currently missing.
4. How to treat placeholders.
5. A conservative discount percentage formula.
6. Rules for when we are allowed to call a vacation undervalued.
7. A Python function outline.
8. Tests to run.
9. When to commit.

Important:
Do not overbuild. Do not use machine learning yet. Make the first benchmark transparent and conservative.
```
