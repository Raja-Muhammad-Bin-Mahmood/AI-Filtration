import streamlit as st
import requests
import time
import subprocess
import sys

# Function to install required packages
def install_packages():
    packages = ["streamlit_autorefresh", "requests"]
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install required packages
install_packages()

from streamlit_autorefresh import st_autorefresh

# Set up the page
st.set_page_config(layout="wide", page_title="Water Filtration Plants PD Khan Thill Sharif")

# Styling with a water theme
st.markdown("""
    <style>
    body {background-color: #f0f4f7;}
    .stText {color: #0a74da; font-family: 'Helvetica Neue', sans-serif;}
    .stBox {background-color: #e0f7fa; border-radius: 15px; padding: 20px; color: #004d40;}
    .stGreenBox {background-color: #00796b; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stTitle {color: #0288d1; font-family: 'Helvetica Neue', sans-serif; text-align: center;}
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='stTitle'>Water Filtration Plants PD Khan Thill Sharif</h1>", unsafe_allow_html=True)

# Auto-refresh every 60 seconds
count = st_autorefresh(interval=60000, limit=100, key="refresh_counter")

# Function to fetch weather data using the Weather API
def get_weather_data(api_key, location="Jhelum,PK"):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    response = requests.get(url)
    return response.json()

# Replace with your Weather API key
api_key = "ec5dff3620be8d025f51f648826a4ada"

# Fetch weather data
weather_data = get_weather_data(api_key)

# Extract temperature (simulated for demo)
temperature = weather_data['current']['temperature']

# Column layout for three filters
col1, col2, col3 = st.columns(3)

# Function to display filtration unit data
def display_unit(name, flow_rate_range, chem_dosage_range, maintenance_days):
    st.markdown(f'<div class="stBox"><h3>{name}</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(*flow_rate_range)} Liters/day")
    st.text(f"Temperature: {temperature:.2f} °C")  # Using API data
    st.text(f"Chemical Dosage: {random.randint(*chem_dosage_range)} kg/day")
    st.markdown(f'<div class="stGreenBox">Maintenance done {maintenance_days[0]} days ago. Next maintenance due in {maintenance_days[1]} days.</div></div>', unsafe_allow_html=True)

with col1:
    display_unit("Osmosis Reactor", (400, 500), (5, 15), (29, 45))

with col2:
    display_unit("AquaGuard Filter", (350, 450), (7, 12), (15, 30))

with col3:
    display_unit("HydroFlow Unit", (380, 480), (6, 14), (10, 20))

# Implementing a refresh using Streamlit's rerun method (auto-refresh handles updates)
if st.button("Manual Refresh"):
    st.experimental_rerun()
