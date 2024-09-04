import streamlit as st
import requests
import datetime
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
    chemical_dosage = 200 + adjustment * random.uniform(8, 12)  # Liters/day
    energy_consumption = 100 + adjustment * random.uniform(30, 50)  # kWh/day
    return chemical_dosage, energy_consumption

# Streamlit app configuration
st.set_page_config(page_title="AI Water Filtration Dashboard", page_icon="💧", layout="wide")

# Custom CSS for the design
st.markdown("""
    <style>
        body {
            background-color: #2f2f2f; /* Grey background */
            color: #00aaff; /* Blue text */
            font-family: 'Arial', sans-serif;
        }
        .filter-box {
            background-color: #4b79a1; /* Complementary color for boxes */
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .filter-title {
            font-size: 1.5em;
            font-weight: bold;
            margin-bottom: 10px;
            color: #ffffff;
        }
        .metric-label {
            font-size: 1.1em;
            font-weight: bold;
        }
        .metric-value {
            font-size: 1.3em;
            margin-bottom: 10px;
        }
        .maintenance-box {
            background-color: #28a745; /* Green background */
            border-radius: 10px;
            padding: 15px;
            color: #ffffff;
            font-size: 1.1em;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

st.title("AI Water Filtration Dashboard")

# Function to fetch weather data
@st.cache_data(ttl=60)
def fetch_weather_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        return {}

# Function to display filter plant data
def display_filter_plants(data):
    if 'main' in data:
        current_temp = data['main']['temp'] + random.uniform(-0.5, 0.5)
        feels_like = data['main']['feels_like'] + random.uniform(-0.5, 0.5)
        humidity = data['main']['humidity'] + random.uniform(-1, 1)

        # Names for the filter plants
        filter_names = ["AquaGuard", "Osmosis Pro", "HydroMax"]

        # Create three filter plants with similar temperature but different other metrics
        filter_plants = []
        for name in filter_names:
            plant_temp = current_temp + random.uniform(-0.2, 0.2)
            predicted_usage = predict_water_usage(plant_temp)
            filtration_adjustment = adjust_filtration(predicted_usage)
            chemical_dosage, energy_consumption = resource_management(filtration_adjustment)
            flow_rate = random.uniform(10000, 20000)  # Liters/day
            ro_status = {
                "membrane_life": f"{random.uniform(50, 100):.1f}%",
                "flow_rate": f"{flow_rate:.1f} L/day",
                "pressure": f"{random.uniform(50, 100):.1f} bar"
            }
            filter_plants.append({
                "Name": name,
                "Temperature": f"{plant_temp:.1f}°C",
                "Feels Like": f"{feels_like:.1f}°C",
                "Humidity": f"{humidity:.1f}%",
                "Predicted Water Usage": f"{predicted_usage:.2f} L/day",
                "Chemical Dosage Required": f"{chemical_dosage:.2f} L/day",
                "Energy Consumption": f"{energy_consumption:.2f} kWh/day",
                "RO Status": ro_status
            })

        # Display the filter plants vertically
        for plant in filter_plants:
            st.markdown(f"""
                <div class="filter-box">
                    <div class="filter-title">{plant['Name']}</div>
                    <div>
                        <span class="metric-label">Temperature:</span>
                        <span class="metric-value">{plant['Temperature']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Feels Like:</span>
                        <span class="metric-value">{plant['Feels Like']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Humidity:</span>
                        <span class="metric-value">{plant['Humidity']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Predicted Water Usage:</span>
                        <span class="metric-value">{plant['Predicted Water Usage']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Chemical Dosage Required:</span>
                        <span class="metric-value">{plant['Chemical Dosage Required']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Energy Consumption:</span>
                        <span class="metric-value">{plant['Energy Consumption']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Flow Rate:</span>
                        <span class="metric-value">{plant['RO Status']['flow_rate']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Membrane Life:</span>
                        <span class="metric-value">{plant['RO Status']['membrane_life']}</span>
                    </div>
                    <div>
                        <span class="metric-label">Pressure:</span>
                        <span class="metric-value">{plant['RO Status']['pressure']}</span>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.error("Error fetching weather data.")

# Function to display maintenance message
def display_maintenance_message():
    last_maintenance_date = datetime.datetime(2024, 4, 27)  # Example date
    now = datetime.datetime.now()
    days_since_last_maintenance = (now - last_maintenance_date).days
    next_maintenance_in = random.randint(20, 50)  # Days until next maintenance

    st.markdown(f"""
        <div class="maintenance-box">
            Maintenance done {days_since_last_maintenance} days ago.<br>
            Next maintenance should be done by {next_maintenance_in} days.
        </div>
    """, unsafe_allow_html=True)

# Main function to control the dashboard
def main():
    data = fetch_weather_data()
    display_filter_plants(data)
    display_maintenance_message()

# Automatically refresh the data every 60 seconds
st_autorefresh(interval=60000, key="data_refresh")

main()
