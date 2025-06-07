import streamlit as st
import pandas as pd
import os

# Set page config
st.set_page_config(
    page_title="Marine Cargo Risk Analyzer",
    layout="wide",
)

# Title
st.title("Marine Cargo Risk Analyzer")

# Base data path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed')

# Load data
df_risk = pd.read_csv(os.path.join(DATA_PATH, 'top_risk_events.csv'))
df_monthly = pd.read_csv(os.path.join(DATA_PATH, 'monthly_trend.csv'))
df_types = pd.read_csv(os.path.join(DATA_PATH, 'accident_types.csv'))

# Tabs
tab1, tab2, tab3 = st.tabs(["Risk Events", "Monthly Trends", "Common Accident Types"])

# Tab 1: Risk Events
with tab1:
    st.subheader("Top Risk Events by Severity Score")
    st.dataframe(df_risk, use_container_width=True)

# Tab 2: Monthly Trends
with tab2:
    st.subheader("Incident Trends Over Time")
    st.line_chart(df_monthly.set_index('month'))

# Tab 3: Common Types
with tab3:
    st.subheader("Most Frequent Types of Maritime Accidents")
    st.bar_chart(df_types.set_index('UlykkeType'))

# Footer
st.markdown("---")
st.markdown("[View source on GitHub](https://github.com/ChristopherIanPeck/marine-cargo-risk-analyzer)")

