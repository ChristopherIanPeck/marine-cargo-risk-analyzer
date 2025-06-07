import pandas as pd
import sqlite3
import os

# --- Base directory ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# --- Paths to root ---
xlsx_path = os.path.join(BASE_DIR, 'data/raw/marine_incidents_raw.xlsx')
csv_path = os.path.join(BASE_DIR, 'data/processed/marine_incidents_cleaned.csv')
db_path = os.path.join(BASE_DIR, 'data/processed/marine_risk.db')

os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# --- Load and transform ---
if not os.path.exists(xlsx_path):
    raise FileNotFoundError(f"Excel file not found at: {xlsx_path}")

df = pd.read_excel(xlsx_path, sheet_name="Export")
print("Columns:", df.columns.tolist())

# Cleaned CSV
df.to_csv(csv_path, index=False)
print(f"Cleaned CSV saved at: {csv_path}")

# Load into SQLite
conn = sqlite3.connect(db_path)
df.to_sql("incidents", conn, if_exists="replace", index=False)
conn.close()
print(f"SQLite DB created at: {db_path}")


