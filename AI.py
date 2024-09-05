import subprocess
import sys
import streamlit as st
import random
import requests
from streamlit_autorefresh import st_autorefresh

# Function to check and install pip if not installed
def install_pip():
    try:
        __import__('pip')
    except ImportError:
        # Install pip if not present
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])

# Function to install required packages
def install_packages():
    required_packages = ['streamlit_autorefresh', 'requests']
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install pip if not present
install_pip()

# Install required packages
install_packages()

# Set up the page
st.set_page_config(layout="wide")

# Weather API configuration
API_KEY = 'ec5dff3620be8d025f51f648826a4ada'  # Replace with your API key
LOCATION = 'Thill Sharif, Pakistan'

# Function to fetch weather data from the API
def get_weather_data(api_key, location):
    """Fetches weather data from the API for the given location."""
    base_url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            return {
                "temperature": data["current"]["temperature"],
                "humidity": data["current"]["humidity"],
                "wind_speed": data["current"]["wind_speed"],
                "precipitation": data["current"]["precip"]
            }
        else:
            st.error("Error retrieving weather data")
            return None
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
        return None

# Fetch weather data
weather_data = get_weather_data(API_KEY, LOCATION)

# Styling with a water theme
st.markdown("""
    <style>
    body {background-color: #f0f4f7;}
    .stText {color: #0a74da; font-family: 'Arial', sans-serif;}
    .stBox {background-color: #0e4c92; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stGreenBox {background-color: #28a745; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stTitle {font-size: 2.5em; font-weight: bold; text-align: center; color: #0a74da;}
    .stBorder {border: 2px solid #0a74da; border-radius: 10px; padding: 10px; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# Title with custom font
st.markdown('<h1 class="stTitle">Water Filtration Plants PD Khan Thill Sharif</h1>', unsafe_allow_html=True)

# Display Weather Information
if weather_data:
    st.markdown(f"### Current Weather in {LOCATION}")
    st.text(f"Temperature: {weather_data['temperature']} °C")
    st.text(f"Humidity: {weather_data['humidity']}%")
    st.text(f"Wind Speed: {weather_data['wind_speed']} km/h")
    st.text(f"Precipitation: {weather_data['precipitation']} mm")

# Column layout for three filters with the refreshed content
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="stBox stBorder"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(400, 500)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(5, 15)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stBox stBorder"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(350, 450)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(7, 12)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 25 days ago. Next maintenance due in 35 days.</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stBox stBorder"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(380, 480)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(6, 14)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 20 days ago. Next maintenance due in 30 days.</div></div>', unsafe_allow_html=True)

# Implementing a refresh using Streamlit's rerun method
st_autorefresh(interval=60000)  # Auto-refresh every 60 seconds
