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

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'processed')

# Load data
df_risk = pd.read_csv(os.path.join(DATA_PATH, 'top_risk_events.csv'))
df_monthly = pd.read_csv(os.path.join(DATA_PATH, 'monthly_trend.csv'))
df_types = pd.read_csv(os.path.join(DATA_PATH, 'accident_types.csv'))

# Sidebar filters
st.sidebar.header("Filter Risk Events")

# Convert UlykkeDato to datetime
df_risk['UlykkeDato'] = pd.to_datetime(df_risk['UlykkeDato'], errors='coerce')

# Filter: Year Range
years = df_risk['UlykkeDato'].dropna().dt.year
min_year, max_year = int(years.min()), int(years.max())
year_range = st.sidebar.slider("Year Range", min_value=min_year, max_value=max_year,
                               value=(min_year, max_year))
df_filtered = df_risk[df_risk['UlykkeDato'].dt.year.between(*year_range)]

# Filter: Vessel Type
vessel_types = sorted(df_filtered['FartøyType'].dropna().unique())
selected_vessels = st.sidebar.multiselect("Vessel Types", vessel_types, default=vessel_types)
df_filtered = df_filtered[df_filtered['FartøyType'].isin(selected_vessels)]

# Filter: Damage Type
damage_types = sorted(df_filtered['Skadeomfang'].dropna().unique())
selected_damages = st.sidebar.multiselect("Damage Types", damage_types, default=damage_types)
df_filtered = df_filtered[df_filtered['Skadeomfang'].isin(selected_damages)]

# Tabs
tab1, tab2, tab3 = st.tabs(["Risk Events", "Monthly Trends", "ccident Types"])

# Tab 1
with tab1:
    st.subheader("Top Risk Events (Filtered)")
    st.dataframe(df_filtered.sort_values("risk_score", ascending=False).reset_index(drop=True),
                 use_container_width=True)

# Tab 2
with tab2:
    st.subheader("Incidents Over Time")
    st.line_chart(df_monthly.set_index('month'))

# Tab 3
with tab3:
    st.subheader("Most Frequent Types of Maritime Accidents")
    st.bar_chart(df_types.set_index('UlykkeType'))

# Footer
st.markdown("---")
st.markdown("[View on GitHub](https://github.com/ChristopherIanPeck/marine-cargo-risk-analyzer)")
