import subprocess
import sys
import streamlit as st
import requests
import datetime
import time
import numpy as np
import random

# Function to install required packages
def install_packages():
    required_packages = [
        'streamlit',
        'requests',
        'numpy'
    ]
    for package in required_packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Install packages
install_packages()

# OpenWeatherMap API configuration
api_key = "ec5dff3620be8d025f51f648826a4ada"
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Define the predictive model
def predict_water_usage(temp):
    if temp < 25:
        return 1000
    elif temp < 30:
        return 1500
    elif temp < 35:
        return 2000
    elif temp < 40:
        return 2500
    else:
        return 3000

# Define filtration adjustment
def adjust_filtration(usage):
    base_capacity = 1000
    adjustment = (usage - base_capacity) / 1000
    return adjustment

# Define resource management
def resource_management(adjustment):
    chemicals_used = 100 + adjustment * 10
    energy_used = 50 + adjustment * 5
    return chemicals_used, energy_used

# Streamlit app
st.set_page_config(page_title="Water Filtration Dashboard", page_icon=":droplet:", layout="wide")

st.title("Water Filtration Dashboard")

# Background animation CSS
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #000000, #003300);
            color: #00ff00;
            overflow: hidden;
        }
        .stTitle {
            color: #00ff00;
            font-size: 2.5em;
        }
        .stButton {
            color: #000000;
            background-color: #00ff00;
        }
        .animated-background {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://www.example.com/your-wallpaper.jpg'); /* Replace with your wallpaper URL */
            background-size: cover;
            animation: moveBackground 30s linear infinite;
            z-index: -1;
        }
        @keyframes moveBackground {
            0% { background-position: 0% 0%; }
            100% { background-position: 100% 100%; }
        }
        .stMarkdown {
            font-family: 'Arial', sans-serif;
        }
        .stDataFrame {
            border: 2px solid #00ff00;
            border-radius: 8px;
            padding: 10px;
            background-color: rgba(0, 0, 0, 0.5);
        }
    </style>
    <div class="animated-background"></div>
""", unsafe_allow_html=True)

# Function to update and display data
def update_data():
    while True:
        try:
            # Fetch weather data
            response = requests.get(url)
            data = response.json()

            # Extract data
            if 'main' in data:
                current_temp = data['main']['temp'] + random.uniform(-0.5, 0.5)
                feels_like = data['main']['feels_like'] + random.uniform(-0.5, 0.5)
                min_temp = data['main']['temp_min'] + random.uniform(-0.5, 0.5)
                max_temp = data['main']['temp_max'] + random.uniform(-0.5, 0.5)
                humidity = data['main']['humidity'] + random.uniform(-1, 1)
                
                # Predict water usage
                predicted_usage = predict_water_usage(current_temp)
                
                # Adjust filtration
                filtration_adjustment = adjust_filtration(predicted_usage)
                
                # Resource management
                chemicals, energy = resource_management(filtration_adjustment)

                # Get current date and time
                now = datetime.datetime.now()
                current_date = now.strftime("%Y-%m-%d")
                current_time = now.strftime("%H:%M:%S")

                # Display data
                st.markdown(f"### Current Date: {current_date}")
                st.markdown(f"### Current Time: {current_time}")
                st.markdown(f"**Temperature:** {current_temp:.1f}°C")
                st.markdown(f"**Feels Like:** {feels_like:.1f}°C")
                st.markdown(f"**Minimum Temperature:** {min_temp:.1f}°C")
                st.markdown(f"**Maximum Temperature:** {max_temp:.1f}°C")
                st.markdown(f"**Humidity:** {humidity:.1f}%")
                st.markdown(f"**Predicted Water Usage:** {predicted_usage:.2f} liters")
                st.markdown(f"**Filtration Adjustment Needed:** {filtration_adjustment:.2f}")
                st.markdown(f"**Chemicals Needed:** {chemicals:.2f} units")
                st.markdown(f"**Energy Needed:** {energy:.2f} kWh")

                # Maintenance prediction
                days_since_last_maintenance = (now - datetime.datetime(2024, 1, 1)).days
                maintenance_due = days_since_last_maintenance > 30

                if maintenance_due:
                    st.warning("Maintenance is due for the filtration system.")
                else:
                    st.success("No maintenance needed at the moment.")
            
            else:
                st.error("Error fetching weather data.")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        # Pause before updating again
        time.sleep(60)  # Update every 60 seconds

# Run the update data function
update_data()
