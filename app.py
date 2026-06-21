import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("fraud_detection_model.pkl")

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
Upload a CSV file containing transaction data.
The model will classify each transaction as:

- **0 → Legitimate Transaction**
- **1 → Fraudulent Transaction**
""")

uploaded_file = st.file_uploader(
    "Upload Transaction CSV File",
    type=["csv"]
)

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)

        st.subheader("Uploaded Data")
        st.dataframe(data.head())

        prediction = model.predict(data)

        data["Prediction"] = prediction

        fraud_count = (prediction == 1).sum()
        legit_count = (prediction == 0).sum()

        st.subheader("Prediction Results")
        st.dataframe(data)

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Fraud Transactions",
                fraud_count
            )

        with col2:
            st.metric(
                "Legitimate Transactions",
                legit_count
            )

        csv = data.to_csv(index=False).encode("utf-8")

        st.download_button(
            "Download Results",
            csv,
            "prediction_results.csv",
            "text/csv"
        )

    except Exception as e:
        st.error(
            f"Error processing file: {e}"
        )