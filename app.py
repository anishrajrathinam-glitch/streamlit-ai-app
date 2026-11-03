import streamlit as st
import numpy as np

st.title("AI Prediction Demo")

st.write("This application demonstrates an AI prediction using Streamlit.")

value = st.slider("Select a value", 0, 100, 50)

if value >= 50:
    prediction = "Positive"
else:
    prediction = "Negative"

st.subheader("Prediction")
st.success(prediction)
