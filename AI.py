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

# Custom CSS for the design
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(135deg, #1f005c, #5b0060, #870160, #ac255e, #ca485c, #e16b5c, #f39060, #ffb56b);
            color: #ffffff;
            overflow: hidden;
        }
        .stTitle {
            color: #ffffff;
            font-size: 3em;
            font-weight: bold;
        }
        .stHeader {
            font-size: 1.5em;
            color: #ffffff;
        }
        .stMetric {
            font-size: 1.2em;
            margin: 10px 0;
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
    </style>
""", unsafe_allow_html=True)

st.title("AI Water Filtration Dashboard")

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

                # Update the display every second
                data_placeholder.markdown(
                    f"""
                    <div class="data-container">
                        <div class="card">
                            <div class="stHeader">Current Date: {current_date}</div>
                            <div class="stHeader">Current Time: {current_time}</div>
                        </div>
                        <div class="card">
                            <div class="stMetric">Temperature: {current_temp:.1f}°C</div>
                            <div class="stMetric">Feels Like: {feels_like:.1f}°C</div>
                            <div class="stMetric">Minimum Temperature: {min_temp:.1f}°C</div>
                            <div class="stMetric">Maximum Temperature: {max_temp:.1f}°C</div>
                            <div class="stMetric">Humidity: {humidity:.1f}%</div>
                        </div>
                        <div class="card">
                            <div class="stMetric">Predicted Water Usage: {predicted_usage:.2f} liters</div>
                            <div class="stMetric">Filtration Adjustment Needed: {filtration_adjustment:.2f}</div>
                            <div class="stMetric">Chemicals Needed: {chemicals:.2f} units</div>
                            <div class="stMetric">Energy Needed: {energy:.2f} kWh</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )

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
        
        # Update every second
        time.sleep(1)

# Run the update data function
update_data()
