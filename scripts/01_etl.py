import pandas as pd
import sqlite3
import os

#File paths
xlsx_path = "data/raw/marine_incidents_raw.xlsx"
csv_path = "data/processed/marine_incidents_cleaned.csv"
db_path = "data/processed/marine_risk.db"

#Ensure output folder exists
os.makedirs("data/processed", exist_ok=True)

#Load Excel data
try:
    df = pd.read_excel(xlsx_path, sheet_name="Export")
except FileNotFoundError:
    print(f"ERROR: File not found: {xlsx_path}")
    exit(1)

print("Initial columns:", df.columns.tolist())

#Save cleaned CSV
df.to_csv(csv_path, index=False)
print(f"Cleaned CSV saved at: {csv_path}")

#Write to SQLite
conn = sqlite3.connect(db_path)
df.to_sql("incidents", conn, if_exists="replace", index=False)
conn.close()

print(f"SQLite DB created at: {db_path}")


