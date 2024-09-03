import streamlit as st
import requests
import datetime
import time
import random

# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Water Filtration Dashboard",
    page_icon="💧",
    layout="centered",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* General styling */
    .stApp {
        background-color: #f0f2f6;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }

    /* Main content styling */
    .content {
        padding: 20px;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }

    /* Label styling */
    .label {
        font-size: 1.25rem;
        font-weight: bold;
        margin-bottom: 5px;
    }

    /* Value styling */
    .value {
        font-size: 2rem;
        font-weight: bold;
        color: #007BFF;
    }

    /* Maintenance bar */
    .maintenance-bar {
        padding: 10px;
        background-color: #ff3333;
        text-align: center;
        font-weight: bold;
        font-size: 1rem;
        color: white;
        border-radius: 5px;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# OpenWeatherMap API configuration
api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Function to fetch weather data
def fetch_weather_data():
    response = requests.get(url)
    data = response.json()
    return data

# Define the predictive model
def predict_water_usage(temp):
    base_usage = 1000
    variability = random.uniform(0.9, 1.1)
    return base_usage * variability

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

# Function to update and display data
def update_data():
    # Fetch weather data
    data = fetch_weather_data()

    # Extract data and update dynamically
    if 'main' in data:
        current_temp = data['main']['temp'] + random.uniform(-0.5, 0.5)
        feels_like = data['main']['feels_like'] + random.uniform(-0.5, 0.5)
        humidity = data['main']['humidity'] + random.uniform(-1, 1)
        
        # Predict water usage
        predicted_usage = predict_water_usage(current_temp)
        
        # Adjust filtration
        filtration_adjustment = adjust_filtration(predicted_usage)
        
        # Resource management
        chemicals, energy = resource_management(filtration_adjustment)

        # Display data in a structured way
        st.markdown("<div class='content'>", unsafe_allow_html=True)
        st.markdown(f"<div class='label'>Temperature:</div> <div class='value'>{current_temp:.1f}°C</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='label'>Feels Like:</div> <div class='value'>{feels_like:.1f}°C</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='label'>Humidity:</div> <div class='value'>{humidity:.1f}%</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='label'>Predicted Water Usage:</div> <div class='value'>{predicted_usage:.2f} liters</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='label'>Chemicals Needed:</div> <div class='value'>{chemicals:.2f} units</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='label'>Energy Needed:</div> <div class='value'>{energy:.2f} kWh</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        # Maintenance prediction
        now = datetime.datetime.now()
        days_since_last_maintenance = (now - datetime.datetime(2024, 1, 1)).days
        maintenance_due = days_since_last_maintenance > 30

        # Maintenance bar
        if maintenance_due:
            st.markdown("<div class='maintenance-bar'>Maintenance is due for the filtration system.</div>", unsafe_allow_html=True)

    else:
        st.error("Error fetching weather data.")

# Run the update data function every second
if __name__ == "__main__":
    while True:
        update_data()
        time.sleep(1)  # Update every second
