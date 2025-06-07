# marine-cargo-risk-analyzer
project_structure = """
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
"""

# Generate README.md content
readme_content = f"""
# Marine Cargo Risk Analyzer

This project analyzes real-world maritime accident data from the Norwegian Maritime Authority to identify high-risk events and visualize trends from 1981–2024.

 **Live App:** [Streamlit Dashboard](https://marine-cargo-risk-analyzer.streamlit.app)

---

## Features

- Risk scoring for historical maritime incidents
- Top incidents by severity, casualties, and damage
- Visual analysis of accident types and ship categories
- Monthly trends across 40+ years
- Interactive dashboard built with Streamlit

---

## Project Structure

{project_structure}

---

## ow to Run Locally

```bash
# Clone the repository
git clone https://github.com/ChristopherIanPeck/marine-cargo-risk-analyzer.git
cd marine-cargo-risk-analyzer

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the ETL script
python scripts/01_etl.py

# Run the analysis script
python scripts/02_analysis.py

# Launch the Streamlit app
streamlit run scripts/streamlit_app.py
