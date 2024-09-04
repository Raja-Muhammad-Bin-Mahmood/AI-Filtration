# Install the required packages
import subprocess
import sys

def install_packages():
    packages = ['streamlit-autorefresh', 'streamlit']
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_packages()

# Import the required modules
from streamlit_autorefresh import st_autorefresh
import streamlit as st
import random

# Set up the page
st.set_page_config(layout="wide")

# Styling with a water theme
st.markdown("""
    <style>
    body {background-color: #f0f4f7;}
    .stText {color: #4da6ff; font-family: 'Helvetica Neue', sans-serif;}
    .stBox {
        background-color: #0073e6;
        border-radius: 15px;
        padding: 20px;
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stGreenBox {
        background-color: #28a745;
        border-radius: 15px;
        padding: 20px;
        color: #ffffff;
        font-family: 'Helvetica Neue', sans-serif;
    }
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #0059b3;
        text-align: center;
        border-bottom: 2px solid #0059b3;
        padding-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Display the title
st.markdown('<h1>Water Filtration Plants PD Khan Thill Sharif</h1>', unsafe_allow_html=True)

# Column layout for three filters
col1, col2, col3 = st.columns(3)

# Osmosis Reactor
with col1:
    st.markdown('<div class="stBox"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(400, 500)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(5, 15)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

# AquaGuard Filter
with col2:
    st.markdown('<div class="stBox"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(350, 450)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(7, 12)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 15 days ago. Next maintenance due in 59 days.</div></div>', unsafe_allow_html=True)

# HydroFlow Unit
with col3:
    st.markdown('<div class="stBox"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(380, 480)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(6, 14)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 5 days ago. Next maintenance due in 75 days.</div></div>', unsafe_allow_html=True)

# Auto-refresh every 10 seconds
count = st_autorefresh(interval=10 * 1000, key="filt_autorefresh")

# Implementing a refresh using Streamlit's rerun method
if st.button("Refresh Data"):
    st.experimental_rerun()
