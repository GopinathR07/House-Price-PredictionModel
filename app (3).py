import streamlit as st
import numpy as np
import pickle

st.title("🏠 House Price Prediction App")

# Dummy model (for testing)
def predict_price(data):
    return sum(data) * 0.1

MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
AveRooms = st.number_input("Average Rooms")
AveBedrms = st.number_input("Average Bedrooms")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
Latitude = st.number_input("Latitude")
Longitude = st.number_input("Longitude")

if st.button("Predict"):
    result = predict_price([
        MedInc, HouseAge, AveRooms, AveBedrms,
        Population, AveOccup, Latitude, Longitude
    ])
    st.success(f"Predicted Price: {result}")
