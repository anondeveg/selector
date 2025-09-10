# S3lect0r – SQL Injection Pentest Toolkit 

S3lect0r is a lightweight SQL injection reconnaissance and triage toolkit focused on rapid URL screening. It features a fast SQLI Scanner for pentest workflows, supported by utilities for list preparation (combo/URL cleaning, sorting, deduping) and basic parsing. The app is modular, cross-platform (Linux/Windows), and configurable via JSON.

## Highlights
- SQL Injection Scanner: quick triage of URL lists to surface likely SQL injection entry points with live stats (CPM, counts) and categorized hit files
- URL and list utilities: cleaner, reverser, sorter, shuffle, remove dupes, line counter, LQ→HQ
- Email/domain helpers: domain changer, email/password extractors, filter by domain, EP→UP, domain sorter
- Parsers: keywords from URLs, page types/formats from URLs, URL cleaner
- Externalized config for long lists (`data/config.json`)
- TEST_DATA fixtures for quick manual testing
- Optional GUI file picker; CLI prompt fallback on Linux

## Requirements
- Python 3.11+ recommended (tested with 3.13)
- pip, virtualenv

Key packages (see `requirements.txt`): beautifulsoup4, colorama, discord.py, download, matplotlib, my_fake_useragent, requests.

Note: `tkinter` is optional on Linux. If you want GUI file dialogs, install Tk (Arch: `sudo pacman -S tk`). Without it, the program falls back to CLI prompts for file paths.

## Setup
```bash
git clone https://github.com/anondeveg/selector
cd cd selector
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

## Run
## SQLI Scanner Overview
The SQL Injection Scanner rapidly triages large URL sets and highlights endpoints that are likely injectable based on response-body heuristics.

- Detection categories: MySQL, Microsoft SQL Server, PostgreSQL, Oracle, MariaDB, and generic SQL error strings
- Live metrics: CPM (checks per minute), running totals per engine, errors, and elapsed time
- Output: categorized hit files saved under `results/SQL_HITS/` with timestamps
- Config: tune filtering and parsing helpers via `data/config.json`

```bash
source .venv/bin/activate
python selector.py
```

## Configuration
data is externalized in `data/config.json`:
- `pagtypes`: default page parameter seeds for dork generation
- `bad_urls`: prefixes filtered out by the URL cleaner

Example:
```json
{
  "pagtypes": ["id=", "page=", "user_id="],
  "bad_urls": ["https://www.google.com", "https://www.bing.com/ck/a?!&&p="]
}
```


## Test Data
Sample inputs live under `TEST_DATA/`. When prompted for files, select the relevant one (e.g., `TEST_DATA/password_limit.txt`, `TEST_DATA/domain_changer.txt`, `TEST_DATA/remove_dupes.txt`).




## License
For authorized security testing and research only. You must have explicit permission from the system owner. Always comply with applicable laws and target site terms.
