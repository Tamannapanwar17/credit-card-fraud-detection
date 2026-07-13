# 💳 Credit Card Fraud Detection using Machine Learning

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Latest-green.svg)](https://xgboost.readthedocs.io/)
[![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter%20Optimization-purple.svg)](https://optuna.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)](https://streamlit.io/)

## 📌 Project Overview

Credit card fraud is a major challenge in the financial industry due to the extremely small number of fraudulent transactions compared to legitimate ones. This project develops a machine learning pipeline to accurately identify fraudulent transactions while minimizing false alarms.

The project includes:

- Data preprocessing and exploratory data analysis (EDA)
- Handling class imbalance using **SMOTE**
- Training and comparing multiple machine learning models
- Hyperparameter optimization using **Optuna**
- Model explainability using **SHAP**
- Interactive prediction through a **Streamlit** web application

---

## 🎯 Problem Statement

Develop a machine learning model capable of detecting fraudulent credit card transactions using historical transaction data.

### Challenges

- Highly imbalanced dataset
- Fraud transactions represent only **0.17%** of all transactions
- Need to maximize fraud detection while minimizing false positives

---

## 📊 Dataset

**Source:** Kaggle Credit Card Fraud Detection Dataset

### Dataset Information

- **Total Transactions:** 284,807
- **Fraudulent Transactions:** 492
- **Normal Transactions:** 284,315
- **Features:** 31

| Feature | Description |
|----------|-------------|
| Time | Seconds elapsed between transactions |
| Amount | Transaction amount |
| V1 - V28 | PCA-transformed anonymized features |
| Class | Target (0 = Normal, 1 = Fraud) |

---

# 🛠️ Project Workflow

```
Problem Definition
        ↓
Data Understanding
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Scaling
        ↓
Train-Test Split
        ↓
SMOTE (Handle Class Imbalance)
        ↓
Baseline Model Training
        ↓
Model Comparison
        ↓
XGBoost Selection
        ↓
Hyperparameter Tuning (Optuna)
        ↓
Final Model Training
        ↓
Model Evaluation
        ↓
SHAP Explainability
        ↓
Save Model
        ↓
Streamlit Deployment
```

---

# 📈 Exploratory Data Analysis

The following analyses were performed:

- Dataset shape
- Missing value analysis
- Duplicate removal
- Class distribution
- Transaction amount distribution
- Correlation heatmap
- Feature distribution

---

# 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

Evaluation Metric:

- Precision
- Recall
- F1-score
- ROC-AUC Score

---

# ⚡ Hyperparameter Optimization

The best-performing baseline model (**XGBoost**) was further optimized using **Optuna**.

### Optimized Parameters

| Parameter | Value |
|-----------|------|
| n_estimators | 389 |
| learning_rate | 0.1107 |
| max_depth | 10 |
| subsample | 0.9067 |
| colsample_bytree | 0.6854 |
| gamma | 0.0515 |
| min_child_weight | 4 |
| reg_alpha | 0.4198 |
| reg_lambda | 1.8205 |

---

# 📊 Model Performance

## Final XGBoost (Optuna Tuned)

| Metric | Value |
|---------|--------|
| Accuracy | **99.93%** |
| Precision | **81.52%** |
| Recall | **78.95%** |
| F1 Score | **80.23%** |
| ROC-AUC | **0.9696** |

---

# 📉 Visualizations

The project includes the following visualizations:

- Class Distribution
- Correlation Heatmap
- Model Comparison
- Confusion Matrix
- ROC Curve
- Precision-Recall Curve
- Feature Importance
- SHAP Summary Plot

---

# 🔍 Model Explainability

To improve model transparency, **SHAP (SHapley Additive Explanations)** was used.

Key findings:

- **V14** was the most influential feature.
- **V4, V10, and V12** also had a significant impact on fraud prediction.
- SHAP explains how each feature contributes to individual predictions.

---

# 🌐 Streamlit Application

The project includes an interactive Streamlit web application.

Features:

- Upload transaction CSV
- Predict fraudulent transactions
- View prediction results
- Download predictions as CSV

Run locally:

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```
credit-card-fraud-detection/
│
├── Credit_Card_Fraud_Detection.ipynb
├── app.py
├── fraud_detection_model.pkl
├── requirements.txt
├── README.md
├── creditcard.csv
└── images/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Tamannapanwar17/credit-card-fraud-detection.git
```

Go to project directory

```bash
cd credit-card-fraud-detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the notebook or Streamlit app.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Optuna
- SHAP
- Joblib
- Streamlit

---

# 🚀 Future Improvements

- Real-time fraud detection
- Deep learning models
- Threshold optimization
- Ensemble learning
- API deployment using FastAPI
- Cloud deployment (AWS/Azure/GCP)

---

# 👩‍💻 Author

**Tamanna Panwar**

B.Tech Student, National Institute of Technology Uttarakhand

GitHub: https://github.com/Tamannapanwar17

---

## ⭐ If you found this project useful, consider giving it a star!
