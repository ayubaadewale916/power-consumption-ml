import streamlit as st
import pandas as pd
import joblib
import warnings

warnings.filterwarnings("ignore")

st.set_page_config(page_title="Power Consumption Prediction")

st.title("🔌 Household Power Consumption Prediction")

# Load model
model = joblib.load("power_model.pkl")

st.sidebar.header("Input Electrical Parameters")

Voltage = st.sidebar.number_input("Voltage (V)", value=230.0)
Global_reactive_power = st.sidebar.number_input("Reactive Power (kVAR)", value=0.1)
Global_intensity = st.sidebar.number_input("Current (A)", value=5.0)

Sub_metering_1 = st.sidebar.number_input("Sub Metering 1", value=0.0)
Sub_metering_2 = st.sidebar.number_input("Sub Metering 2", value=0.0)
Sub_metering_3 = st.sidebar.number_input("Sub Metering 3", value=0.0)

Hour = st.sidebar.slider("Hour of Day", 0, 23, 12)

if st.button("Predict Power Consumption"):
    # EXACT SAME FEATURES + ORDER AS TRAINING
    input_df = pd.DataFrame(
        [[
            Voltage,
            Global_reactive_power,
            Global_intensity,
            Sub_metering_1,
            Sub_metering_2,
            Sub_metering_3,
            Hour
        ]],
        columns=[
            "Voltage",
            "Global_reactive_power",
            "Global_intensity",
            "Sub_metering_1",
            "Sub_metering_2",
            "Sub_metering_3",
            "Hour"
        ]
    )

    prediction = model.predict(input_df)
    st.success(f"⚡ Predicted Active Power: {prediction[0]:.3f} kW")
