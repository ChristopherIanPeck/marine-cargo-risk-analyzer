import sqlite3
import pandas as pd
import os

# Project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
db_path = os.path.join(BASE_DIR, 'data/processed/marine_risk.db')

# Connect to SQLite
conn = sqlite3.connect(db_path)

# --- Query 1: Most common types of accidents ---
q1 = """
SELECT 
    UlykkeType, 
    COUNT(*) AS count 
FROM incidents
GROUP BY UlykkeType
ORDER BY count DESC
"""
df1 = pd.read_sql(q1, conn)
print("\n Most Common Types of Accidents:")
print(df1)

# --- Query 2: Most affected ship types ---
q2 = """
SELECT 
    FartøyType, 
    COUNT(*) AS count
FROM incidents
GROUP BY FartøyType
ORDER BY count DESC
"""
df2 = pd.read_sql(q2, conn)
print("\nAccidents by Ship Type:")
print(df2)

# --- Query 3: High-fatality events ---
q3 = """
SELECT 
    UlykkeDato, 
    FartøyNavn, 
    AntallDød, 
    AntallSkadet, 
    Skadeomfang
FROM incidents
WHERE AntallDød > 0
ORDER BY AntallDød DESC
LIMIT 10
"""
df3 = pd.read_sql(q3, conn)
print("\n Deadliest Incidents:")
print(df3)

# --- Query 4: Monthly incident trend (if dates are consistent) ---
q4 = """
SELECT 
    strftime('%Y-%m', UlykkeDato) AS month,
    COUNT(*) AS count
FROM incidents
WHERE UlykkeDato IS NOT NULL
GROUP BY month
ORDER BY month
"""
df4 = pd.read_sql(q4, conn)
print("\n Monthly Incidents Over Time:")
print(df4)

# --- Query 5: Compute Risk Score for each incident ---
q5 = """
SELECT 
    UlykkeDato,
    FartøyNavn,
    FartøyType,
    AntallDød,
    AntallSkadet,
    Skadeomfang,
    
    -- Assign numeric damage score
    CASE Skadeomfang
        WHEN 'Fartøy sunket/total havari' THEN 100
        WHEN 'Fartøy totalskadet (ikke sunket)' THEN 80
        WHEN 'Vesentlige skader' THEN 60
        WHEN 'Mindre skader' THEN 30
        ELSE 0
    END AS skade_score,
    
    -- Final risk score formula
    (AntallDød * 100) + (AntallSkadet * 10) + 
    CASE Skadeomfang
        WHEN 'Fartøy sunket/total havari' THEN 100
        WHEN 'Fartøy totalskadet (ikke sunket)' THEN 80
        WHEN 'Vesentlige skader' THEN 60
        WHEN 'Mindre skader' THEN 30
        ELSE 0
    END AS risk_score

FROM incidents
WHERE AntallDød IS NOT NULL OR AntallSkadet IS NOT NULL OR Skadeomfang IS NOT NULL
ORDER BY risk_score DESC
LIMIT 20
"""
df5 = pd.read_sql(q5, conn)
print("\n Top Risk Events (by risk score):")
print(df5)


# --- Save to CSV for Power BI ---
output_dir = os.path.join(BASE_DIR, 'data/processed')
df1.to_csv(os.path.join(output_dir, 'accident_types.csv'), index=False)
df2.to_csv(os.path.join(output_dir, 'ship_types.csv'), index=False)
df3.to_csv(os.path.join(output_dir, 'deadliest_incidents.csv'), index=False)
df4.to_csv(os.path.join(output_dir, 'monthly_trend.csv'), index=False)
df5.to_csv(os.path.join(output_dir, 'top_risk_events.csv'), index=False)

conn.close()
print("\n Analysis complete. Results saved to /data/processed/")
