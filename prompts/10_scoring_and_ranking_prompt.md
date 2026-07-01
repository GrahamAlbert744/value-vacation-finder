# Scoring and Ranking Prompt

Use this when candidate records exist.

```text
Help me score vacation candidates in value-vacation-finder.

Use the scoring weights from config/scoring_weights.yaml:

- Price undervaluation: 30
- Flight quality/value: 15
- Accommodation quality/value: 20
- Destination attractiveness: 10
- Attractions/tours value: 10
- Safety/risk: 10
- Practicality/friction: 5

Return:
1. A scoring function
2. A recommendation tier function
3. A ranked output table
4. A clear explanation of each score
5. Simple MVP logic first, not advanced machine learning
```
