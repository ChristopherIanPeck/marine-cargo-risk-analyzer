# Marine Cargo Risk Analyzer

This project analyzes real-world maritime accident data from the **Norwegian Maritime Authority** to identify high-risk events, trends, and vessel types involved in marine incidents from **1981–2024**.

**Live App**: [Streamlit Dashboard](https://marine-cargo-risk-analyzer.streamlit.app)

---

## Features

- **Risk Scoring** for each incident (fatalities, injuries, damage)
- Top incidents by severity and casualties
- Accident breakdown by ship type and accident category
- Monthly trend analysis across 40+ years
- Interactive, filterable dashboard built with **Streamlit**

---

## roject Structure

```text
/marine-cargo-risk-analyzer
├── data
│   ├── raw                      # Original Excel data from the Norwegian Maritime Authority
│   └── processed                # Cleaned CSVs and SQLite DB used in the app
├── scripts
│   ├── 01_etl.py               # Extract and transform the data
│   ├── 02_analysis.py          # Perform SQL analysis and save key outputs
│   └── streamlit_app.py        # Interactive dashboard app
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview and instructions
