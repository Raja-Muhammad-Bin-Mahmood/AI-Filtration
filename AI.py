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
    </style>
""", unsafe_allow_html=True)

# Column layout for three filters
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="stBox"><h3>Osmosis Reactor</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(400, 500)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(5, 15)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="stBox"><h3>AquaGuard Filter</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(350, 450)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(7, 12)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="stBox"><h3>HydroFlow Unit</h3>', unsafe_allow_html=True)
    st.text(f"Flow Rate: {random.randint(380, 480)} Liters/day")
    st.text(f"Temperature: {random.uniform(22.0, 25.0):.2f} °C")
    st.text(f"Chemical Dosage: {random.randint(6, 14)} kg/day")
    st.markdown('<div class="stGreenBox">Maintenance done 29 days ago. Next maintenance due in 45 days.</div></div>', unsafe_allow_html=True)

# Implementing a refresh using Streamlit's rerun method
if st.button("Refresh Data"):
    st.experimental_rerun()
