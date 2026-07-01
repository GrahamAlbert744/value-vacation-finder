# Cleaning Module Design Prompt

Use this when starting Python cleaners.

```text
Help me create a Python cleaning module for value-vacation-finder.

Source:
[Skyscanner / Expedia / Tripadvisor / Viator / Travel Advisory]

Input:
Raw markdown or JSON saved in data/raw/[source]/

Output:
A standardized pandas DataFrame saved to data/interim/[cleaned_source]/

Requirements:
1. Create the file path.
2. Give me the code.
3. Explain the function briefly.
4. Include basic validation.
5. Do not overwrite raw data.
6. Tell me how to test it.
7. Tell me when to commit.
```
