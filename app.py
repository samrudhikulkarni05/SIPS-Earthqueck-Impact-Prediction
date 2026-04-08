import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Page Configuration
st.set_page_config(
    page_title="SIPS - Seismic Intelligence & Prediction System",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Deep Ocean & Volcanic Theme
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: #f8fafc;
    }
    .stButton>button {
        background-color: #0891b2;
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #06b6d4;
        border: none;
    }
    .css-1d391kg {
        background-color: #1e293b;
    }
    .metric-card {
        background-color: #1e293b;
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid #334155;
    }
    .developer-text {
        font-size: 0.8rem;
        color: #94a3b8;
        margin-top: 2rem;
    }
    .creator-name {
        color: #22d3ee;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("SIPS")
st.sidebar.caption("Seismic Intelligence & Prediction System")

menu = ["Home", "Prediction Lab", "Live Map", "Data Insights", "Safety & Prep"]
choice = st.sidebar.selectbox("Navigation", menu)

st.sidebar.markdown("---")
st.sidebar.markdown('<div class="developer-text">Developed by <span class="creator-name">Samrudhi Kulkarni</span></div>', unsafe_allow_html=True)

# Mock Data Generation
def get_mock_alerts():
    return pd.DataFrame([
        {"Location": "Hokkaido, Japan", "Magnitude": 5.2, "Time": "12m ago", "Risk": "Medium"},
        {"Location": "Antofagasta, Chile", "Magnitude": 4.1, "Time": "45m ago", "Risk": "Low"},
        {"Location": "Lombok, Indonesia", "Magnitude": 6.4, "Time": "2h ago", "Risk": "High"},
        {"Location": "California, USA", "Magnitude": 3.8, "Time": "4h ago", "Risk": "Low"},
        {"Location": "Athens, Greece", "Magnitude": 4.5, "Time": "6h ago", "Risk": "Medium"},
        {"Location": "Sichuan, China", "Magnitude": 5.9, "Time": "8h ago", "Risk": "High"},
    ])

# --- HOME PAGE ---
if choice == "Home":
    st.title("Predicting the Unpredictable.")
    st.write("SIPS combines advanced machine learning with real-time tectonic data to provide accurate risk assessments and life-saving insights for a safer world.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Events", "1,284", "+12")
    with col2:
        st.metric("High Risk Zones", "42", "-2")
    with col3:
        st.metric("Active Sensors", "8,902", "Live")
    with col4:
        st.metric("Global Coverage", "98.4%", "Stable")

    st.markdown("---")
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("System Capabilities")
        c1, c2 = st.columns(2)
        with c1:
            st.info("**Real-time Monitoring**\n\nContinuous ingestion of global seismic data from USGS, EMSC, and private sensor networks.")
        with c2:
            st.warning("**ML Risk Assessment**\n\nProprietary algorithms trained on 50+ years of historical data to identify high-probability risk zones.")
            
        if st.button("View Documentation"):
            st.write("### System Documentation")
            st.write("**Overview**: SIPS is a comprehensive platform designed to monitor, analyze, and predict seismic events globally.")
            st.write("**Prediction Lab**: Allows users to simulate seismic scenarios based on magnitude and depth.")
            st.write("**Data Sources**: Integrates data from USGS, EMSC, and IoT sensor networks.")

    with col_right:
        st.subheader("Recent Alerts")
        alerts_df = get_mock_alerts()
        for index, row in alerts_df.head(3).iterrows():
            st.markdown(f"**{row['Location']}**")
            st.caption(f"Mag: {row['Magnitude']} | {row['Time']} | Risk: {row['Risk']}")
            st.markdown("---")
        
        if st.button("View All Alerts"):
            st.table(alerts_df)

# --- PREDICTION LAB ---
elif choice == "Prediction Lab":
    st.title("Prediction Lab")
    st.write("Simulate seismic scenarios to assess potential risks.")
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        mag = col1.slider("Magnitude (Mw)", 1.0, 10.0, 5.0)
        depth = col2.number_input("Depth (km)", 0, 700, 10)
        
        lat = col1.number_input("Latitude", -90.0, 90.0, 0.0)
        lon = col2.number_input("Longitude", -180.0, 180.0, 0.0)
        
        submitted = st.form_submit_button("Run Analysis")
        
        if submitted:
            risk_score = (mag * 0.7) - (depth * 0.01)
            if risk_score > 5:
                st.error(f"High Risk Detected! Score: {risk_score:.2f}")
            elif risk_score > 3:
                st.warning(f"Medium Risk Detected. Score: {risk_score:.2f}")
            else:
                st.success(f"Low Risk. Score: {risk_score:.2f}")

# --- LIVE MAP ---
elif choice == "Live Map":
    st.title("Live Seismic Map")
    # Simple mock map data
    map_data = pd.DataFrame(
        np.random.randn(100, 2) / [50, 50] + [35.6895, 139.6917],
        columns=['lat', 'lon']
    )
    st.map(map_data)
    st.caption("Displaying recent activity around major fault lines.")

# --- DATA INSIGHTS ---
elif choice == "Data Insights":
    st.title("Data Insights")
    
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Magnitude', 'Depth', 'Frequency']
    )
    
    st.subheader("Seismic Activity Trends")
    st.line_chart(chart_data)
    
    st.subheader("Magnitude Distribution")
    fig = px.histogram(chart_data, x="Magnitude", nbins=10, color_discrete_sequence=['#0891b2'])
    st.plotly_chart(fig, use_container_width=True)

# --- SAFETY & PREP ---
elif choice == "Safety & Prep":
    st.title("Safety & Preparedness")
    
    with st.expander("Before an Earthquake"):
        st.write("- Secure heavy items to walls.")
        st.write("- Create a family emergency plan.")
        st.write("- Prepare an emergency kit (water, food, first aid).")
        
    with st.expander("During an Earthquake"):
        st.write("- **DROP, COVER, and HOLD ON**.")
        st.write("- Stay away from glass, windows, and outside doors.")
        st.write("- If in bed, stay there and protect your head with a pillow.")
        
    with st.expander("After an Earthquake"):
        st.write("- Check yourself and others for injuries.")
        st.write("- Be prepared for aftershocks.")
        st.write("- Listen to local news for emergency information.")
