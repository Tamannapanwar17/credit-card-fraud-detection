import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# -----------------------------
# Load Trained Model
# -----------------------------
model = joblib.load("fraud_detection_model.pkl")

# -----------------------------
# Title
# -----------------------------
st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
This application predicts whether a credit card transaction is **Legitimate** or **Fraudulent** using a trained **XGBoost** model.

### Prediction Labels
- **0 → Legitimate Transaction**
- **1 → Fraudulent Transaction**
""")

# -----------------------------
# Expected Features
# -----------------------------
expected_columns = [
    'Time','V1','V2','V3','V4','V5','V6','V7','V8','V9',
    'V10','V11','V12','V13','V14','V15','V16','V17','V18',
    'V19','V20','V21','V22','V23','V24','V25','V26','V27',
    'V28','Amount'
]

# -----------------------------
# Upload CSV
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload Transaction CSV File",
    type=["csv"]
)

# -----------------------------
# Prediction
# -----------------------------
if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Dataset")

    st.dataframe(data.head())

    # Check columns
    if list(data.columns) != expected_columns:

        st.error("❌ Uploaded CSV does not contain the required columns.")

        st.write("Expected Columns:")

        st.write(expected_columns)

        st.stop()

    # Predict
    prediction = model.predict(data)

    probability = model.predict_proba(data)[:,1]

    data["Prediction"] = prediction

    data["Result"] = data["Prediction"].map({
        0: "Legitimate",
        1: "Fraud"
    })

    data["Fraud Probability"] = probability.round(4)

    # Display Result
    st.subheader("Prediction Results")

    st.dataframe(data)

    # -----------------------------
    # Summary
    # -----------------------------
    fraud = (data["Prediction"] == 1).sum()

    normal = (data["Prediction"] == 0).sum()

    total = len(data)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Transactions", total)

    col2.metric("Legitimate", normal)

    col3.metric("Fraudulent", fraud)

    # -----------------------------
    # Download
    # -----------------------------
    csv = data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction Results",
        data=csv,
        file_name="fraud_predictions.csv",
        mime="text/csv"
    )

else:

    st.info("Please upload a CSV file to begin prediction.")
