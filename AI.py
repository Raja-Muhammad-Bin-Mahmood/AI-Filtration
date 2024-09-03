import streamlit as st
import requests
import datetime
import time
import numpy as np
import random

# Set Streamlit page configuration
st.set_page_config(
    page_title="AI Water Filtration Dashboard",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    /* Background styling */
    .stApp {
        background: linear-gradient(120deg, #000428, #004e92);
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Navbar styling */
    .navbar {
        display: flex;
        justify-content: space-around;
        padding: 1rem 0;
        background-color: rgba(0, 0, 0, 0.7);
        backdrop-filter: blur(5px);
        border-radius: 10px;
    }

    .navbar a {
        color: #ffffff;
        text-decoration: none;
        font-size: 1.5rem;
        transition: color 0.3s;
    }

    .navbar a:hover {
        color: #00ffff;
    }

    /* Dropdown menu styling */
    .dropdown-content {
        display: none;
        position: absolute;
        background-color: #333333;
        min-width: 200px;
        box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
        z-index: 1;
    }

    .dropdown-content a {
        color: white;
        padding: 12px 16px;
        text-decoration: none;
        display: block;
        transition: background-color 0.3s;
    }

    .dropdown-content a:hover {
        background-color: #575757;
    }

    .dropdown:hover .dropdown-content {
        display: block;
    }

    /* Maintenance bar */
    .maintenance-bar {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #ff5555;
        text-align: center;
        padding: 1rem;
        font-weight: bold;
        font-size: 1.2rem;
        color: white;
    }

    /* Animated values */
    .animated-value {
        font-size: 2rem;
        font-weight: bold;
        color: #00ffff;
        animation: changeValue 1s infinite alternate;
    }

    @keyframes changeValue {
        0% { color: #00ffff; }
        100% { color: #ffcc00; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navbar with dropdown menus
st.markdown(
    """
    <div class="navbar">
        <div class="dropdown">
            <a href="#">Temperature</a>
            <div class="dropdown-content">
                <a href="#">Temperature: Dynamic data...</a>
                <a href="#">Feels Like: Dynamic data...</a>
                <a href="#">Humidity: Dynamic data...</a>
            </div>
        </div>
        <div class="dropdown">
            <a href="#">Logistics</a>
            <div class="dropdown-content">
                <a href="#">Chemicals: Dynamic data...</a>
                <a href="#">Energy Usage: Dynamic data...</a>
                <a href="#">Maintenance: Dynamic data...</a>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# OpenWeatherMap API configuration
api_key = "ec5dff3620be8d025f51f648826a4ada"
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

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
    response = requests.get(url)
    data = response.json()

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

        # Get current date and time
        now = datetime.datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        current_time = now.strftime("%H:%M:%S")

        # Display data
        st.markdown(f"<div class='animated-value'>Temperature: {current_temp:.1f}°C</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='animated-value'>Feels Like: {feels_like:.1f}°C</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='animated-value'>Humidity: {humidity:.1f}%</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='animated-value'>Predicted Water Usage: {predicted_usage:.2f} liters</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='animated-value'>Chemicals Needed: {chemicals:.2f} units</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='animated-value'>Energy Needed: {energy:.2f} kWh</div>", unsafe_allow_html=True)

        # Maintenance prediction
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
