import streamlit as st
import pandas as pd
import joblib
st.set_page_config(
    page_title="Energy Consumption Optimizer",
    page_icon="⚡",
    layout="wide"
)
model = joblib.load("energy_model.pkl")
st.title("⚡ Energy Consumption Optimizer")

st.write("""
Predict the energy consumption of a building using Machine Learning.
Enter the values in the sidebar and click **Predict**.
""")
st.sidebar.header("Input Parameters")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    15,
    40,
    28
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    20,
    90,
    50
)

occupancy = st.sidebar.slider(
    "Occupancy",
    1,
    10,
    5
)

appliances = st.sidebar.slider(
    "Running Appliances",
    1,
    20,
    10
)

hour = st.sidebar.slider(
    "Hour",
    0,
    23,
    12
)

previous_consumption = st.sidebar.number_input(
    "Previous Consumption (kWh)",
    value=250.0
)
input_df = pd.DataFrame({
    "Temperature":[temperature],
    "Humidity":[humidity],
    "Occupancy":[occupancy],
    "Appliances":[appliances],
    "Hour":[hour],
    "Previous_Consumption":[previous_consumption]
})
st.subheader("Current Input")

st.dataframe(input_df)
if st.button("Predict Energy Consumption"):

    prediction = model.predict(input_df)

    st.success(
        f"Predicted Energy Consumption: {prediction[0]:.2f} kWh"
    )

    st.subheader("Recommendations")

    if prediction[0] > 300:

        st.error("🔴 High Energy Consumption")

        st.write("✅ Reduce AC usage")
        st.write("✅ Turn off unused appliances")
        st.write("✅ Shift heavy loads to off-peak hours")
        st.write("✅ Use LED lighting")

    elif prediction[0] > 200:

        st.warning("🟡 Moderate Energy Consumption")

        st.write("• Monitor electricity usage")
        st.write("• Avoid standby power consumption")
        st.write("• Schedule heavy appliances efficiently")

    else:

        st.success("🟢 Excellent Energy Efficiency")

        st.write("🎉 Your energy consumption is efficient!")
st.caption("Built using Streamlit + Scikit-learn + Random Forest")