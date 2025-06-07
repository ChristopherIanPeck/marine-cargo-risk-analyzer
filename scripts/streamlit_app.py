import streamlit as st
import pandas as pd
import os

# Base path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed')

# Load data
df_risk = pd.read_csv(os.path.join(DATA_PATH, 'top_risk_events.csv'))
df_monthly = pd.read_csv(os.path.join(DATA_PATH, 'monthly_trend.csv'))
df_types = pd.read_csv(os.path.join(DATA_PATH, 'accident_types.csv'))

# Page title
st.title("Marine Cargo Risk Analyzer")

# Tab: Risk Score
st.header("op Risk Events")
st.dataframe(df_risk)

# Tab: Monthly Trend
st.header("Monthly Incidents Over Time")
st.line_chart(df_monthly.set_index('month'))

# Tab: Most Common Accident Types
st.header("Common Accident Types")
st.bar_chart(df_types.set_index('UlykkeType'))
