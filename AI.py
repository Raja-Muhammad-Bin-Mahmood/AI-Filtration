import streamlit as st
import random
import time

# Set up the page layout
st.set_page_config(layout="wide")

# Styling with a water theme
st.markdown("""
    <style>
    body {background-color: #f0f4f7;}
    .stText {color: #0a74da; font-family: 'Arial', sans-serif;}
    .stBox {background-color: #0e4c92; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stGreenBox {background-color: #28a745; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stTitle {font-size: 2.5em; font-weight: bold; text-align: center; color: #0a74da;}
    .stBorder {border: 2px solid #0a74da; border-radius: 10px; padding: 10px; margin-bottom: 20px;}
    </style>
""", unsafe_allow_html=True)

# Title with custom font
st.markdown('<h1 class="stTitle">Water Filtration Plants PD Khan Thill Sharif</h1>', unsafe_allow_html=True)

# Function to simulate real-time changing values for water filtration
def generate_filter_data():
    return {
        "Osmosis Reactor": {
            "Flow Rate": f"{random.randint(400, 500)} Liters/day",
            "Temperature": f"{random.uniform(22.0, 25.0):.2f} °C",
            "Chemical Dosage": f"{random.randint(5, 15)} kg/day",
            "Maintenance": "29 days ago. Next maintenance due in 45 days."
        },
        "AquaGuard Filter": {
            "Flow Rate": f"{random.randint(350, 450)} Liters/day",
            "Temperature": f"{random.uniform(22.0, 25.0):.2f} °C",
            "Chemical Dosage": f"{random.randint(7, 12)} kg/day",
            "Maintenance": "25 days ago. Next maintenance due in 35 days."
        },
        "HydroFlow Unit": {
            "Flow Rate": f"{random.randint(380, 480)} Liters/day",
            "Temperature": f"{random.uniform(22.0, 25.0):.2f} °C",
            "Chemical Dosage": f"{random.randint(6, 14)} kg/day",
            "Maintenance": "20 days ago. Next maintenance due in 30 days."
        }
    }

# Function to display the filter data in columns
def display_filter_data():
    data = generate_filter_data()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f'<div class="stBox stBorder"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
        st.text(f"Flow Rate: {data['Osmosis Reactor']['Flow Rate']}")
        st.text(f"Temperature: {data['Osmosis Reactor']['Temperature']}")
        st.text(f"Chemical Dosage: {data['Osmosis Reactor']['Chemical Dosage']}")
        st.markdown(f'<div class="stGreenBox">Maintenance: {data["Osmosis Reactor"]["Maintenance"]}</div></div>', unsafe_allow_html=True)

    with col2:
        st.markdown(f'<div class="stBox stBorder"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
        st.text(f"Flow Rate: {data['AquaGuard Filter']['Flow Rate']}")
        st.text(f"Temperature: {data['AquaGuard Filter']['Temperature']}")
        st.text(f"Chemical Dosage: {data['AquaGuard Filter']['Chemical Dosage']}")
        st.markdown(f'<div class="stGreenBox">Maintenance: {data["AquaGuard Filter"]["Maintenance"]}</div></div>', unsafe_allow_html=True)

    with col3:
        st.markdown(f'<div class="stBox stBorder"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
        st.text(f"Flow Rate: {data['HydroFlow Unit']['Flow Rate']}")
        st.text(f"Temperature: {data['HydroFlow Unit']['Temperature']}")
        st.text(f"Chemical Dosage: {data['HydroFlow Unit']['Chemical Dosage']}")
        st.markdown(f'<div class="stGreenBox">Maintenance: {data["HydroFlow Unit"]["Maintenance"]}</div></div>', unsafe_allow_html=True)

# Refreshing the page every second without external packages
while True:
    display_filter_data()
    time.sleep(1)  # Refresh every second
    st.experimental_rerun()  # Re-run the app to refresh content
