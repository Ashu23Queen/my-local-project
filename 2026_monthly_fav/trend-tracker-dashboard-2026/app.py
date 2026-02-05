import streamlit as st
import plotly.express as px
from data_engine import get_trend_data

# Page Config
st.set_page_config(page_title="2026 Trend Tracker", layout="wide")
st.title("🚀 2026 Trend-Tracker Dashboard")

# Sidebar for Inputs
st.sidebar.header("Settings")
keywords = st.sidebar.text_input("Enter keywords (comma separated)", "AI, Robotics, Quantum Computing")
kw_list = [x.strip() for x in keywords.split(",")]

# Fetch Data
if st.button("Sync Live Trends"):
    df = get_trend_data(kw_list)
    
    # Logic for Layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Interest Over Time")
        fig = px.line(df, labels={"value": "Interest", "date": "Timeline"})
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.subheader("Trend Breakdown")
        latest_stats = df.iloc[-1]
        st.write(latest_stats)

def explain_trend(keyword, score):
    # This is a placeholder for an API call to OpenAI/Gemini
    return f"The term '{keyword}' is spiking with a score of {score} due to recent breakthroughs in industry-led adoption."

# Call this in the UI
st.info(explain_trend(kw_list[0], 85))