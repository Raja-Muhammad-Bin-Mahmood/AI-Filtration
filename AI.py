import subprocess
import sys
import streamlit as st
import random
import requests  # To fetch weather data
from datetime import datetime

# Install pip if not already installed
def install_pip():
    try:
        subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
    except subprocess.CalledProcessError as e:
        st.error("Failed to install pip automatically. Please install pip manually.")
        return

# Install any required packages
def install_packages():
    required_packages = ['streamlit_autorefresh', 'requests']
    for package in required_packages:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            st.error(f"Failed to install package {package}. Please try installing it manually.")
            return

# Run the installation functions
install_pip()
install_packages()

# Import after installation (important to avoid issues)
try:
    from streamlit_autorefresh import st_autorefresh
except ModuleNotFoundError:
    st.error("streamlit_autorefresh is not installed. Please try installing it manually.")
    st.stop()

# Set up the page
st.set_page_config(layout="wide")

# Function to get weather data
def get_weather_data(api_key, location="Lahore"):
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    try:
        response = requests.get(url)
        data = response.json()
        if "error" in data:
            st.error(f"Error fetching weather data: {data['error']['info']}")
            return None
        return data
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")
        return None

# Get weather data from your API key
weather_data = get_weather_data("ec5dff3620be8d025f51f648826a4ada")

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

# Weather information (if fetched successfully)
if weather_data:
    location_name = weather_data['location']['name']
    temperature = weather_data['current']['temperature']
    humidity = weather_data['current']['humidity']
    wind_speed = weather_data['current']['wind_speed']
    st.markdown(f"### Weather Data for {location_name}:")
    st.markdown(f"- **Temperature**: {temperature} °C")
    st.markdown(f"- **Humidity**: {humidity}%")
    st.markdown(f"- **Wind Speed**: {wind_speed} km/h")

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
