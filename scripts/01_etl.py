import pandas as pd
import sqlite3
import os

#File paths

xlsx_path = 'data/raw/marine_incidents_raw.xlsx'
csv_path = 'data/processed/marine_incidents_cleaned.csv'
db_path = 'data/processed/marine_risk.db'

df = pd.read_excel(xlsx_path, sheet_name='Export')

print ('Initial Columns:', df.columns.tolist())

df.to_csv(csv_path, index=False)


conn = sqlite3.connect(db_path)
df.to_sql('incidents', conn, if_exists='replace', index=False)
conn.close()

print (f'SQLite DB created at {db_path}')

