import streamlit as st
import pandas as pd

# Load data
df_risk = pd.read_csv("data/processed/top_risk_events.csv")
df_monthly = pd.read_csv("data/processed/monthly_trend.csv")
df_types = pd.read_csv("data/processed/accident_types.csv")

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
