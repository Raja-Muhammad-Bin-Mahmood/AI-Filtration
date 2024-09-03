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

# Define the predictive model
def predict_water_usage(temp):
    base_usage = 800 + (temp * random.uniform(10, 20))
    noise = random.uniform(-20, 20)  # Smaller noise for smoother transitions
    return base_usage + noise

# Define filtration adjustment
def adjust_filtration(usage):
    base_capacity = 1000
    adjustment = (usage - base_capacity) / 1000
    return adjustment

# Define resource management
def resource_management(adjustment):
    chemicals_used = 100 + adjustment * random.uniform(8, 12)
    energy_used = 50 + adjustment * random.uniform(3, 7)
    return chemicals_used, energy_used

# Streamlit app configuration
st.set_page_config(page_title="AI Water Filtration Dashboard", page_icon=":droplet:", layout="wide")

# Custom CSS for the design and dropdown menu
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@300;400;700&display=swap');
        body {
            font-family: 'Roboto Condensed', sans-serif;
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
            font-family: 'Roboto Condensed', sans-serif;
        }
        .stHeader {
            font-size: 1.5em;
            color: #ffffff;
            font-family: 'Roboto Condensed', sans-serif;
        }
        .stMetric {
            font-size: 1.2em;
            margin: 10px 0;
            font-family: 'Roboto Condensed', sans-serif;
        }
        .data-container {
            padding: 20px;
            border-radius: 10px;
            background: rgba(255, 255, 255, 0.1);
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.2);
        }
        .card {
            background: rgba(0, 0, 0, 0.1);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
        }
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #333;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown-content a {
            color: white;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }
        .dropdown-content a:hover {
            background-color: #575757;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
        .dropdown:hover .dropbtn {
            background-color: #555;
        }
        .maintenance-indicator {
            width: 100px;
            height: 100px;
            background-color: #ff4757;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1em;
            color: white;
            font-weight: bold;
        }
        .maintenance-ok {
            background-color: #2ecc71;
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI Water Filtration Dashboard")

# Dropdown menu
st.markdown("""
    <div class="dropdown">
        <span class="stHeader dropbtn">Options</span>
        <div class="dropdown-content">
            <a href="#temperature">Temperature</a>
            <a href="#logistics">Logistics</a>
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

                # Update the display every second
                data_placeholder.markdown(
                    f"""
                    <div class="data-container">
                        <div class="card">
                            <div class="stHeader">Current Date: {current_date}</div>
                            <div class="stHeader">Current Time: {current_time}</div>
                        </div>
                        <div class="card" id="temperature">
                            <div class="stMetric">Temperature: {current_temp:.1f}°C</div>
                            <div class="stMetric">Feels Like: {feels_like:.1f}°C</div>
                            <div class="stMetric">Minimum Temperature: {min_temp:.1f}°C</div>
                            <div class="stMetric">Maximum Temperature: {max_temp:.1f}°C</div>
                            <div class="stMetric">Humidity: {humidity:.1f}%</div>
                        </div>
                        <div class="card" id="logistics">
                            <div class="stMetric">Predicted Water Usage: {predicted_usage:.2f} liters</div>
                            <div class="stMetric">Filtration Adjustment Needed: {filtration_adjustment:.2f}</div>
                            <div class="stMetric">Chemicals Needed: {chemicals:.2f} units</div>
                            <div class="stMetric">Energy Needed: {energy:.2f} kWh</div>
                        </div>
                        <div class="card">
                            <div class="maintenance-indicator {maintenance_class}">{maintenance_status}</div>
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
