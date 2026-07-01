# Workflow Audit Prompt

Use this when you want ChatGPT to audit project progress before moving forward.

```text
Audit the current value-vacation-finder workflow.

Check whether I have missed any steps, prompts, code files, documentation files, connector uses, tests, commits, or GitHub-safe sample artifacts.

Current intended workflow:

1. Phase 0 — project scaffold and GitHub setup
2. Phase 1 — configuration and documentation
3. Phase 2 — search run setup
4. Phase 3 — connector-assisted data collection
5. Phase 4 — raw data review
6. Phase 5 — structured candidate creation and validation
7. Phase 6 — processed candidate generation
8. Phase 7 — benchmarking
9. Phase 8 — scoring
10. Phase 9 — reporting

Please return:

1. What is complete
2. What is missing
3. What is blocked
4. What should not be done yet
5. Whether any connector should be used now
6. The next exact phase
7. The exact file to create or edit next
8. The commands to test and commit
```
