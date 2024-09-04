import streamlit as st
import random
from datetime import datetime, timedelta

# Error handling for temperature formatting (fixed)
def get_formatted_temperature(min_value, max_value, decimals=2):
    try:
        return f"{random.uniform(min_value, max_value):.{decimals}f} °C"
    except ValueError:
        st.error("Error generating temperature. Please ensure valid minimum and maximum values.")
        return None

# Weather data simulation (using `datetime` for semi-realistic updates)
def simulate_weather_data():
    current_time = datetime.now()
    base_temp = 23.5  # Adjust this base temperature as needed

    # Simulate slight temperature fluctuations throughout the day
    temperature_offset = random.uniform(-1.0, 1.0)
    current_temp = base_temp + temperature_offset

    # Calculate feels like based on a simple formula (adjust as needed)
    feels_like = current_temp + random.uniform(-0.5, 0.5)

    # Simulate realistic min/max temperatures within a range
    min_temp = current_temp - random.uniform(1.0, 2.0)
    max_temp = current_temp + random.uniform(1.0, 2.0)

    # Simulate random but realistic humidity (adjust range as needed)
    humidity = random.randint(40, 70)

    return {
        "Temperature": f"{current_temp:.2f}°C",
        "Feels Like": f"{feels_like:.2f}°C",
        "Minimum Temperature": f"{min_temp:.2f}°C",
        "Maximum Temperature": f"{max_temp:.2f}°C",
        "Humidity": f"{humidity}%",
    }

# Improved refresh functionality using `st.experimental_rerun`
def refresh_data():
    if st.button("Refresh Data"):
        # Simulate a short delay to mimic data retrieval from an API
        time.sleep(1)  # Adjust delay as needed
        st.experimental_rerun()

# Set page config and styling (enhanced)
st.set_page_config(layout="wide")

st.markdown("""
<style>
body {
    background-color: #f0f4f7;
    font-family: Arial, sans-serif;  /* Add a nice font */
}
.stText {
    color: #0a74da;
}
.stBox {
    background-color: #0e4c92;
    border-radius: 15px;
    padding: 20px;
    color: #ffffff;
    border: 5px solid #28a745;  /* Curved border with green color */
    margin: 10px;  /* Add margin for spacing */
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);  /* Add subtle shadow */
}
.stGreenBox {
    background-color: #28a745; /* Consistent green color */
    border-radius: 10px;  /* Adjust green box border radius */
    padding: 10px;
    color: #ffffff;
    margin: 5px;  /* Adjust margin for spacing within box */
}
</style>
""", unsafe_allow_html=True)

# Filter information with placeholders (replace with actual data)
filter_data = [
    {
        "title": "Osmosis Reactor",
        "flow_rate": random.randint(400, 500),
        "temperature": get_formatted_temperature(22.0, 25.0),
        "chemical_dosage": random.randint(5, 15),
        "maintenance_done": (datetime.now() - timedelta(days=29)).strftime("%Y-%m-%d"),
        "maintenance_due": (datetime.now() + timedelta(days=45)).strftime("%Y-%m-%d"),
    },
    {
        "title": "AquaGuard Filter",
        "flow_rate": random.randint(350, 450),
        "temperature": get_formatted_temperature(22.0, 25.0),
