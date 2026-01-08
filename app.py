import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("power_model.pkl")

st.set_page_config(page_title="Power Consumption Prediction")

st.title("🔌 Household Power Consumption Prediction")
st.write("Predict electrical power consumption using machine learning")

st.sidebar.header("Input Electrical Parameters")

voltage = st.sidebar.number_input("Voltage (V)", 100.0, 300.0, 230.0)
reactive_power = st.sidebar.number_input("Reactive Power (kVAR)", 0.0, 5.0, 0.1)
current = st.sidebar.number_input("Current (A)", 0.0, 50.0, 5.0)

sub1 = st.sidebar.number_input("Sub Metering 1 (Kitchen)", 0.0, 50.0, 0.0)
sub2 = st.sidebar.number_input("Sub Metering 2 (Laundry)", 0.0, 50.0, 0.0)
sub3 = st.sidebar.number_input("Sub Metering 3 (AC/Heater)", 0.0, 50.0, 0.0)

hour = st.sidebar.slider("Hour of Day", 0, 23, 12)

if st.button("🔍 Predict Power Consumption"):
    input_data = np.array(
        [[voltage, reactive_power, current, sub1, sub2, sub3, hour]]
    )
    
    prediction = model.predict(input_data)
    
    st.success(
        f"⚡ Predicted Active Power Consumption: {prediction[0]:.3f} kW"
    )

st.markdown("---")
st.caption("ML Project | Electrical Engineering | Streamlit Deployment")
