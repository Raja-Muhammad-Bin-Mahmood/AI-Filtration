import streamlit as st
import requests
import datetime
import time
import random

# OpenWeatherMap API configuration
api_key = "ec5dff3620be8d025f51f648826a4ada"
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Predictive model function
def predict_water_usage(temp):
    base_usage = 800 + (temp * random.uniform(10, 20))
    noise = random.uniform(-20, 20)  # Smaller noise for smoother transitions
    return base_usage + noise

# Filtration adjustment function
def adjust_filtration(usage):
    base_capacity = 1000
    adjustment = (usage - base_capacity) / 1000
    return adjustment

# Resource management function
def resource_management(adjustment):
    chemicals_used = 100 + adjustment * random.uniform(8, 12)
    energy_used = 50 + adjustment * random.uniform(3, 7)
    return chemicals_used, energy_used

# Streamlit app configuration
st.set_page_config(page_title="AI Water Filtration Dashboard", page_icon=":droplet:", layout="wide")

# Custom CSS for the design and dropdown menu
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
        body {
            font-family: 'Montserrat', sans-serif;
        }
        .stApp {
            background: #1e1e1e;
            color: #ffffff;
            overflow: hidden;
        }
        .stTitle {
            color: #ffffff;
            font-size: 3em;
            font-weight: bold;
            font-family: 'Montserrat', sans-serif;
        }
        .stHeader {
            font-size: 1.5em;
            color: #ffffff;
            font-family: 'Montserrat', sans-serif;
        }
        .dropdown {
            position: relative;
            display: inline-block;
            margin: 20px;
            padding: 20px;
            background-color: #333;
            border-radius: 10px;
            cursor: pointer;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #444;
            min-width: 200px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            padding: 20px;
            z-index: 1;
            border-radius: 10px;
            transition: opacity 0.3s ease-in-out;
            opacity: 0;
        }
        .dropdown:hover .dropdown-content {
            display: block;
            opacity: 1;
        }
        .dropdown:hover {
            background-color: #555;
        }
        .maintenance-bar {
            width: 100%;
            height: 30px;
            background-color: #444;
            border-radius: 15px;
            margin-top: 20px;
            overflow: hidden;
            position: relative;
        }
        .maintenance-fill {
            width: 0;
            height: 100%;
            background-color: #ff4757;
            border-radius: 15px;
            transition: width 1s ease-in-out;
            position: absolute;
        }
        .maintenance-ok .maintenance-fill {
            background-color: #2ecc71;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI Water Filtration Dashboard")

# Dropdown menu with hover effect
st.markdown("""
    <div class="dropdown">
        <span class="stHeader">Temperature</span>
        <div class="dropdown-content">
            <p>Current Temperature: Hover to see details</p>
            <p>Feels Like: Hover to see details</p>
            <p>Humidity: Hover to see details</p>
        </div>
    </div>
    <div class="dropdown">
        <span class="stHeader">Logistics</span>
        <div class="dropdown-content">
            <p>Predicted Water Usage: Hover to see details</p>
            <p>Filtration Adjustment Needed: Hover to see details</p>
            <p>Chemicals and Energy: Hover to see details</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# Function to update and display data
def update_data():
    data_placeholder = st.empty()
    
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

                # Maintenance calculation
                days_since_last_maintenance = (now - datetime.datetime(2024, 1, 1)).days
                maintenance_due = days_since_last_maintenance > 30
                maintenance_status = "Maintenance Due" if maintenance_due else "System OK"
                maintenance_class = "maintenance-ok" if not maintenance_due else ""
                maintenance_fill_width = "100%" if maintenance_due else f"{(days_since_last_maintenance / 30) * 100}%"

                # Update the display every second
                data_placeholder.markdown(
                    f"""
                    <div class="data-container">
                        <div class="card">
                            <div class="stHeader">Current Date: {current_date}</div>
                            <div class="stHeader">Current Time: {current_time}</div>
                        </div>
                        <div class="maintenance-bar {maintenance_class}">
                            <div class="maintenance-fill" style="width: {maintenance_fill_width};"></div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )
            
            else:
                st.error("Error fetching weather data.")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        # Update every second
        time.sleep(1)

# Run the update data function
update_data()
