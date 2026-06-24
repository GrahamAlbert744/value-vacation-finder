\# Source Configuration Notes



The file `config/source\_config.yaml` defines which data source is responsible for each part of the Value Vacation Finder project.



\## Source Roles



\- Skyscanner: primary flight source

\- Expedia: primary hotel-pricing source and secondary flight/package benchmark

\- Tripadvisor: hotel quality, reviews, and value signals

\- Viator: tours, attractions, and experience pricing

\- Travel Advisory: safety and destination-risk screening

\- Benchmark prices: future placeholder for fair-value estimation



\## Why This File Exists



This project combines multiple sources. Without a source configuration file, it would be easy to confuse which source is authoritative for each field.



The source configuration helps keep the project modular. Later, we can add or replace sources without rewriting the whole project.



\## MVP Source Order



The MVP should collect data in this order:



1\. Travel Advisory

2\. Skyscanner

3\. Expedia

4\. Tripadvisor

5\. Viator



Travel Advisory comes first because we do not want to waste time pricing trips to destinations that would later be rejected for safety reasons.



\## Manual Collection Rule



This project does not update automatically. Data should only be collected when the user manually initiates a vacation search.

