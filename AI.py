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

# Define the predictive model for water usage
def predict_water_usage(temp):
    base_usage = 800 + (temp * random.uniform(10, 20))
    noise = random.uniform(-20, 20)
    return base_usage + noise

# Define filtration adjustment based on water usage
def adjust_filtration(usage):
    base_capacity = 1000
    adjustment = (usage - base_capacity) / 1000
    return adjustment

# Define resource management based on filtration adjustment
def resource_management(adjustment):
    chemical_dosage = 200 + adjustment * random.uniform(8, 12)
    energy_consumption = 100 + adjustment * random.uniform(30, 50)
    return chemical_dosage, energy_consumption

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

# Function to update and display data for each filter plant
def update_data():
    data_placeholder = st.empty()
    
    while True:
        try:
            response = requests.get(url)
            data = response.json()

            if 'main' in data:
                current_temp = data['main']['temp'] + random.uniform(-0.5, 0.5)
                feels_like = data['main']['feels_like'] + random.uniform(-0.5, 0.5)
                humidity = data['main']['humidity'] + random.uniform(-1, 1)

                # Data for three filter plants
                plant_data = []
                for i in range(3):
                    plant_temp = current_temp + random.uniform(-0.2, 0.2)
                    predicted_usage = predict_water_usage(plant_temp)
                    filtration_adjustment = adjust_filtration(predicted_usage)
                    chemical_dosage, energy_consumption = resource_management(filtration_adjustment)
                    flow_rate = random.uniform(10000, 20000)
                    ro_status = {
                        "membrane_life": f"{random.uniform(50, 100):.1f}%",
                        "flow_rate": f"{flow_rate:.1f} L/day",
                        "pressure": f"{random.uniform(50, 100):.1f} bar"
                    }
                    plant_data.append({
                        "Temperature": f"{plant_temp:.1f}°C",
                        "Feels Like": f"{feels_like:.1f}°C",
                        "Humidity": f"{humidity:.1f}%",
                        "Predicted Water Usage": f"{predicted_usage:.2f} L/day",
                        "Chemical Dosage Required": f"{chemical_dosage:.2f} L/day",
                        "Energy Consumption": f"{energy_consumption:.2f} kWh/day",
                        "RO Status": ro_status
                    })

                # Update the display
                data_placeholder.markdown(
                    f"""
                    <div class="data-container">
                        <div class="card">
                            <div class="stHeader">Filter Plant 1</div>
                            <div class="stMetric">Temperature: {plant_data[0]['Temperature']}</div>
                            <div class="stMetric">Feels Like: {plant_data[0]['Feels Like']}</div>
                            <div class="stMetric">Humidity: {plant_data[0]['Humidity']}</div>
                            <div class="stMetric">Predicted Water Usage: {plant_data[0]['Predicted Water Usage']}</div>
                            <div class="stMetric">Chemical Dosage Required: {plant_data[0]['Chemical Dosage Required']}</div>
                            <div class="stMetric">Energy Consumption: {plant_data[0]['Energy Consumption']}</div>
                            <div class="stMetric">Flow Rate: {plant_data[0]['RO Status']['flow_rate']}</div>
                            <div class="stMetric">Membrane Life: {plant_data[0]['RO Status']['membrane_life']}</div>
                            <div class="stMetric">Pressure: {plant_data[0]['RO Status']['pressure']}</div>
                        </div>
                        <div class="card">
                            <div class="stHeader">Osmosis Pro</div>
                            <div class="stMetric">Temperature: {plant_data[1]['Temperature']}</div>
                            <div class="stMetric">Feels Like: {plant_data[1]['Feels Like']}</div>
                            <div class="stMetric">Humidity: {plant_data[1]['Humidity']}</div>
                            <div class="stMetric">Predicted Water Usage: {plant_data[1]['Predicted Water Usage']}</div>
                            <div class="stMetric">Chemical Dosage Required: {plant_data[1]['Chemical Dosage Required']}</div>
                            <div class="stMetric">Energy Consumption: {plant_data[1]['Energy Consumption']}</div>
                            <div class="stMetric">Flow Rate: {plant_data[1]['RO Status']['flow_rate']}</div>
                            <div class="stMetric">Membrane Life: {plant_data[1]['RO Status']['membrane_life']}</div>
                            <div class="stMetric">Pressure: {plant_data[1]['RO Status']['pressure']}</div>
                        </div>
                        <div class="card">
                            <div class="stHeader">H2O Max</div>
                            <div class="stMetric">Temperature: {plant_data[2]['Temperature']}</div>
                            <div class="stMetric">Feels Like: {plant_data[2]['Feels Like']}</div>
                            <div class="stMetric">Humidity: {plant_data[2]['Humidity']}</div>
                            <div class="stMetric">Predicted Water Usage: {plant_data[2]['Predicted Water Usage']}</div>
                            <div class="stMetric">Chemical Dosage Required: {plant_data[2]['Chemical Dosage Required']}</div>
                            <div class="stMetric">Energy Consumption: {plant_data[2]['Energy Consumption']}</div>
                            <div class="stMetric">Flow Rate: {plant_data[2]['RO Status']['flow_rate']}</div>
                            <div class="stMetric">Membrane Life: {plant_data[2]['RO Status']['membrane_life']}</div>
                            <div class="stMetric">Pressure: {plant_data[2]['RO Status']['pressure']}</div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True
                )

                # Maintenance prediction
                now = datetime.datetime.now()
                days_since_last_maintenance = (now - datetime.datetime(2024, 1, 1)).days
                maintenance_due = days_since_last_maintenance > 30

                if maintenance_due:
                    st.warning(f"Maintenance is required. It's been {days_since_last_maintenance} days since the last maintenance.")
                else:
                    st.success("No maintenance needed at the moment.")

            else:
                st.error("Error fetching weather data.")

        except Exception as e:
            st.error(f"An error occurred: {e}")
        
        time.sleep(1)

# Run the update data function
update_data()
