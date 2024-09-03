import streamlit as st
import requests
import datetime
import time
import numpy as np
from sklearn.linear_model import LinearRegression

# OpenWeatherMap API configuration
api_key = "ec5dff3620be8d025f51f648826a4ada"  # Replace with your actual OpenWeatherMap API key
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Define the predictive model
def predict_water_usage(temp):
    # Placeholder for actual model
    X = np.array([[25], [30], [35], [40], [45]])
    y = np.array([1000, 1500, 2000, 2500, 3000])
    model = LinearRegression().fit(X, y)
    return model.predict(np.array([[temp]]))[0]

# Define filtration adjustment
def adjust_filtration(usage):
    base_capacity = 1000
    adjustment = (usage - base_capacity) / 1000
    return adjustment

# Define resource management
def resource_management(adjustment):
    chemicals_used = 100
    energy_used = 50
    chemicals_used += adjustment * 10
    energy_used += adjustment * 5
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
            background: linear-gradient(135deg, rgba(0, 51, 0, 0.5), rgba(0, 0, 0, 0.5));
            animation: moveBackground 30s linear infinite;
            z-index: -1;
        }
        @keyframes moveBackground {
            0% { background-position: 0% 0%; }
            100% { background-position: 100% 100%; }
        }
    </style>
    <div class="animated-background"></div>
""", unsafe_allow_html=True)

# Function to update and display data
def update_data():
    while True:
        # Fetch weather data
        response = requests.get(url)
        data = response.json()

        # Extract data
        if 'main' in data:
            current_temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            min_temp = data['main']['temp_min']
            max_temp = data['main']['temp_max']
            humidity = data['main']['humidity']
            
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
            st.write(f"Current Date: {current_date}")
            st.write(f"Current Time: {current_time}")
            st.write(f"Temperature: {current_temp}°C")
            st.write(f"Feels Like: {feels_like}°C")
            st.write(f"Minimum Temperature: {min_temp}°C")
            st.write(f"Maximum Temperature: {max_temp}°C")
            st.write(f"Humidity: {humidity}%")
            st.write(f"Predicted Water Usage: {predicted_usage:.2f} liters")
            st.write(f"Filtration Adjustment Needed: {filtration_adjustment:.2f}")
            st.write(f"Chemicals Needed: {chemicals:.2f}")
            st.write(f"Energy Needed: {energy:.2f}")

            # Maintenance prediction
            days_since_last_maintenance = (now - datetime.datetime(2024, 1, 1)).days
            maintenance_due = days_since_last_maintenance > 30

            if maintenance_due:
                st.warning("Maintenance is due for the filtration system.")
            else:
                st.success("No maintenance needed at the moment.")
        
        # Pause before updating again
        time.sleep(60)  # Update every 60 seconds

# Run the update data function
update_data()
