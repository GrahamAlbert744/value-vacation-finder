\# Destination Filtering



The project contains a large destination universe in:



`config/destinations\_watchlist.yaml`



However, the MVP should not search the full universe at once. The file:



`config/destination\_filter.yaml`



controls which destinations are active for a given manual search run.



\## Why This Matters



The project needs to remain modular. A broad destination universe is useful for future search expansion, but early testing should use a small, controlled list.



\## MVP Filter



The MVP filter currently limits the search to a small set of destinations from Boston:



\- Lisbon

\- Porto

\- Barcelona

\- Rome

\- Athens

\- Montreal

\- Mexico City



\## Safety Filtering



The project should eventually check travel advisory data before treating a destination as eligible.



Current rule:



\- Level 1: eligible

\- Level 2: eligible with caution

\- Level 3: flag for manual review

\- Level 4: reject



\## Manual Run Rule



This project does not update automatically. It only runs when the user manually initiates a vacation search.

