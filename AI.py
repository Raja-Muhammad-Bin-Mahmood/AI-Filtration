import streamlit as st
import random

# Set up the page
st.set_page_config(layout="wide")

# Styling with a water theme
st.markdown("""
    <style>
    body {background-color: #f0f4f7;}
    .stText {color: #0a74da;}
    .stBox {background-color: #0e4c92; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stGreenBox {background-color: #28a745; border-radius: 15px; padding: 20px; color: #ffffff;}
    .stHeader {font-size: 24px; font-weight: bold; color: #ffffff; text-align: center;}
    </style>
""", unsafe_allow_html=True)

# Column layout for three filters
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="stBox"><div class="stHeader">Osmosis Reactor</div>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(400, 500)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(5, 15)} kg/day")
    st.text(f"Filter Life: {random.randint(30, 50)} days remaining")
    st.text(f"Humidity: {random.uniform(40.0, 60.0):.2f} %")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stBox"><div class="stHeader">AquaGuard Filter</div>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(350, 450)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(7, 12)} kg/day")
    st.text(f"Filter Life: {random.randint(25, 45)} days remaining")
    st.text(f"Humidity: {random.uniform(42.0, 58.0):.2f} %")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stBox"><div class="stHeader">HydroFlow Unit</div>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(380, 480)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(6, 14)} kg/day")
    st.text(f"Filter Life: {random.randint(20, 40)} days remaining")
    st.text(f"Humidity: {random.uniform(43.0, 57.0):.2f} %")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

# Reliable refresh mechanism
if st.button("Refresh Data"):
    st.experimental_rerun()
