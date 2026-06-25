\# Search Run Protocol



\## Purpose



A search run is one manual vacation search for one destination and one date range.



The search run template is stored at:



`config/search\_run\_template.yaml`



Each search run should define:



\- Search run ID

\- Origin

\- Destination

\- Departure date

\- Return date

\- Traveler count

\- Source order

\- Raw output naming convention

\- Validation rules



\---



\## Search Run Rule



A search run must not mix:



\- Different destinations

\- Different countries

\- Different departure dates

\- Different return dates

\- Different traveler counts

\- Different currencies unless explicitly documented



\---



\## MVP Example



The starter template uses:



\- Origin: BOS

\- Destination: Lisbon, Portugal

\- Destination airport: LIS

\- Departure date: 2026-10-05

\- Return date: 2026-10-16

\- Travelers: 2 adults

\- Trip length: 11 days



\---



\## Connector Order



Use connectors in this order:



1\. Travel Advisory

2\. Skyscanner

3\. Expedia

4\. Tripadvisor

5\. Viator



Travel Advisory comes first because a destination should not proceed to pricing if it is unsafe or high risk.



\---



\## Raw Output Rule



Raw outputs should be saved locally under:



\- `data/raw/travel\_advisory/`

\- `data/raw/skyscanner/`

\- `data/raw/expedia/`

\- `data/raw/tripadvisor/`

\- `data/raw/viator/`



Raw connector outputs should not be committed to GitHub unless they are mock/sample data.



\---



\## Next Step



After creating the template, the next step is:



`Phase 2.2 — Create the first actual search run config`

