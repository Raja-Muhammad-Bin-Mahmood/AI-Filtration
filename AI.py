import requests
import streamlit as st
import random
import time

# Set up the page
st.set_page_config(layout="wide")

# Styling with a water theme and bold text
st.markdown("""
    <style>
    body {background-color: #f0f4f7;}
    .stText {color: #0a74da; font-family: 'Arial', sans-serif;}
    .stBox {background-color: #0e4c92; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stGreenBox {background-color: #28a745; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stTitle {font-size: 2.5em; font-weight: bold; text-align: center; color: #0a74da;}
    .stBorder {border: 2px solid #0a74da; border-radius: 10px; padding: 10px; margin-bottom: 20px;}
    .bold-text {font-weight: bold; font-size: 1.2em;}
    </style>
""", unsafe_allow_html=True)

# Title with custom font
st.markdown('<h1 class="stTitle">Water Filtration Plants PD Khan Thill Sharif</h1>', unsafe_allow_html=True)

# Weather API setup
api_key = "ec5dff3620be8d025f51f648826a4ada"
latitude = 32.6970
longitude = 73.3252

# Function to fetch weather data from the API using latitude and longitude
def fetch_weather_data():
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={latitude},{longitude}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_data():
    # Fetch the weather data from API
    weather_data = fetch_weather_data()
    
    if weather_data and "current" in weather_data:
        temp_c = weather_data['current']['temperature']
        humidity = weather_data['current']['humidity']
        weather_desc = weather_data['current']['weather_descriptions'][0]
    else:
        temp_c = random.uniform(22.0, 25.0)
        humidity = random.randint(60, 80)
        weather_desc = "No data"

    # Column layout for three filters with the refreshed content
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="stBox stBorder"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Flow Rate: {random.randint(400, 500)} Liters/day</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Temperature: {temp_c} °C (Real-time)</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Humidity: {humidity}%</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Weather: {weather_desc}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Chemical Dosage: {random.randint(5, 15)} kg/day</p>', unsafe_allow_html=True)
        st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="stBox stBorder"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Flow Rate: {random.randint(350, 450)} Liters/day</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Temperature: {temp_c} °C (Real-time)</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Humidity: {humidity}%</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Weather: {weather_desc}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Chemical Dosage: {random.randint(7, 12)} kg/day</p>', unsafe_allow_html=True)
        st.markdown('<div class="stGreenBox">Maintenance done 25 days ago. Next maintenance due in 35 days.</div></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="stBox stBorder"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Flow Rate: {random.randint(380, 480)} Liters/day</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Temperature: {temp_c} °C (Real-time)</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Humidity: {humidity}%</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Weather: {weather_desc}</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="bold-text">Chemical Dosage: {random.randint(6, 14)} kg/day</p>', unsafe_allow_html=True)
        st.markdown('<div class="stGreenBox">Maintenance done 20 days ago. Next maintenance due in 30 days.</div></div>', unsafe_allow_html=True)

# Main loop to update data every 5 seconds
while True:
    display_data()
    time.sleep(5)  # Sleep for 5 seconds between updates
    # No need to rerun the entire script, just refreshing values dynamically
