
import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_model.pkl")

st.title("Credit Card Fraud Detection")

uploaded_file = st.file_uploader(
    "Upload transaction CSV",
    type=["csv"]
)

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    prediction = model.predict(data)

    data["Prediction"] = prediction

    st.write(data)

    st.write(
        f"Fraud Transactions: {(prediction==1).sum()}"
    )
