import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Power Consumption Prediction")

st.title("🔌 Household Power Consumption Prediction")

st.write("Checking deployment files...")

# Show files (DEBUG)
st.write("Files in repo:", os.listdir())

# Load model safely
try:
    model = joblib.load("power_model.pkl")
    st.success("Model loaded successfully")
except Exception as e:
    st.error("❌ Model loading failed")
    st.error(e)
    st.stop()

st.sidebar.header("Input Parameters")

voltage = st.sidebar.number_input("Voltage (V)", value=230.0)
reactive_power = st.sidebar.number_input("Reactive Power", value=0.1)
current = st.sidebar.number_input("Current (A)", value=5.0)

sub1 = st.sidebar.number_input("Sub Metering 1", value=0.0)
sub2 = st.sidebar.number_input("Sub Metering 2", value=0.0)
sub3 = st.sidebar.number_input("Sub Metering 3", value=0.0)

hour = st.sidebar.slider("Hour", 0, 23, 12)

if st.button("Predict"):
    input_df = pd.DataFrame(
        [[voltage, reactive_power, current, sub1, sub2, sub3, hour]],
        columns=[
            "Voltage",
            "Global_reactive_power",
            "Global_intensity",
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3",
            "Hour",
        ],
    )

    prediction = model.predict(input_df)
    st.success(f"⚡ Predicted Power Consumption: {prediction[0]:.3f} kW")
