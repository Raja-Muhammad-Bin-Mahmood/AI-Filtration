import streamlit as st
import random
from streamlit_autorefresh import st_autorefresh

# Set up the page configuration
st.set_page_config(layout="wide")

# Styling with a more elegant Apple-like aesthetic
st.markdown("""
    <style>
    body {
        background-color: #f0f4f7;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stText {
        color: #3498db;
    }
    .stBox {
        background-color: #3498db;
        border-radius: 15px;
        padding: 20px;
        color: #ffffff;
        font-family: 'San Francisco', sans-serif;
    }
    .stGreenBox {
        background-color: #28a745;
        border-radius: 15px;
        padding: 20px;
        color: #ffffff;
        font-family: 'San Francisco', sans-serif;
    }
    .headerBox {
        font-size: 30px;
        color: #2c3e50;
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 3px solid #2c3e50;
    }
    .stButton>button {
        color: #fff;
        background-color: #3498db;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
    }
    .stButton>button:hover {
        background-color: #2980b9;
    }
    </style>
""", unsafe_allow_html=True)

# Header for the App
st.markdown('<div class="headerBox">Water Filtration Plants PD Khan Thill Sharif</div>', unsafe_allow_html=True)

# Column layout for three filters with different maintenance dates
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="stBox"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(400, 500)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Humidity: {random.uniform(30.0, 50.0):.2f}%")
    st.text(f"Filter Life: {random.randint(40, 60)}% remaining")
    st.text(f"Chemical Dosage: {random.randint(5, 15)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done on 2024-07-15. Next maintenance due in 20 days.</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stBox"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(350, 450)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Humidity: {random.uniform(30.0, 50.0):.2f}%")
    st.text(f"Filter Life: {random.randint(30, 50)}% remaining")
    st.text(f"Chemical Dosage: {random.randint(7, 12)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done on 2024-08-01. Next maintenance due in 30 days.</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stBox"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(380, 480)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Humidity: {random.uniform(30.0, 50.0):.2f}%")
    st.text(f"Filter Life: {random.randint(35, 55)}% remaining")
    st.text(f"Chemical Dosage: {random.randint(6, 14)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done on 2024-08-25. Next maintenance due in 40 days.</div></div>', unsafe_allow_html=True)

# Implementing auto-refresh using streamlit-autorefresh
st_autorefresh(interval=60000, limit=None, key="auto_refresh")  # Auto-refresh every 60 seconds
