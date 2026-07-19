sme-market-research/
│
├── data/
│   ├── raw/                  # original downloaded files, never modified
│   └── processed/            # cleaned CSVs you export for inspection
│
├── db/
│   └── sme_research.db       #SQLite database
│
├── scripts/
│   ├── ingest_eurostat_sme.py
│   ├── clean_sme.py
│   ├── analyze_sme.py
│   └── csrd_crosswalk.py
│
├── notebooks/
│   └── exploration.ipynb     # scratch space only, not final code
│
├── notes/
│   └── data_observations.md  # what has been noticed about raw data before coding
│
├── requirements.txt
└── README.md
