# 💳 # 💳 Credit Card Fraud Detection using Machine Learning | Random Forest, SMOTE & XGBoost
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

> Detecting fraudulent credit card transactions using Machine Learning techniques on a highly imbalanced real-world financial dataset.

---

## 📌 Overview

Credit card fraud is a significant challenge for financial institutions worldwide. Since fraudulent transactions represent only a tiny fraction of all transactions, building an effective fraud detection system requires handling highly imbalanced data.

This project develops a Machine Learning-based fraud detection system capable of identifying fraudulent transactions using historical transaction records. Multiple machine learning algorithms were trained and compared to determine the most effective approach.

---

## 🚀 Highlights

✅ Built an end-to-end fraud detection pipeline on **284,807 real-world transactions**

✅ Compared multiple machine learning algorithms:

- Logistic Regression
- Logistic Regression + SMOTE
- Random Forest
- Random Forest + SMOTE
- XGBoost

✅ Achieved:

- 94% Precision using Random Forest
- 83% Recall using Random Forest
- 88% F1-Score using Random Forest
- 95.28% ROC-AUC using XGBoost

✅ Addressed the challenge of highly imbalanced financial transaction data

---

## 🎯 Problem Statement

Financial institutions process millions of transactions every day. Even a small percentage of fraudulent transactions can result in substantial financial losses.

The objective of this project is to build a machine learning model capable of:

- Detecting fraudulent transactions accurately
- Minimizing false negatives
- Handling highly imbalanced datasets
- Improving fraud detection reliability

---

## 💼 Business Impact

An effective fraud detection system can:

- Reduce financial losses
- Improve customer trust
- Detect suspicious transactions quickly
- Support risk management strategies
- Enhance transaction security

This project focuses on maximizing fraud detection performance while minimizing false alarms.

---

## 📊 Dataset Information

### Dataset Source

Kaggle Credit Card Fraud Detection Dataset

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Dataset Snapshot

| Metric | Value |
|----------|----------|
| Total Transactions | 284,807 |
| Legitimate Transactions | 284,315 |
| Fraudulent Transactions | 492 |
| Fraud Percentage | 0.172% |

### Features

| Feature | Description |
|----------|----------|
| Time | Time elapsed between transactions |
| Amount | Transaction Amount |
| V1 - V28 | PCA-transformed confidential features |
| Class | Target Variable |

Target Variable:

- 0 → Legitimate Transaction
- 1 → Fraudulent Transaction

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- Imbalanced-Learn (SMOTE)
- XGBoost
- Jupyter Notebook
- Google Colab

---

## 🔄 Project Workflow

### 1. Data Collection

- Loaded transaction dataset
- Explored dataset structure
- Analyzed class distribution

### 2. Data Preprocessing

- Missing value analysis
- Feature scaling
- Train-test split
- Data visualization

### 3. Handling Class Imbalance

- Applied SMOTE oversampling
- Compared results before and after SMOTE

### 4. Model Training

Models used:

1. Logistic Regression
2. Logistic Regression + SMOTE
3. Random Forest
4. Random Forest + SMOTE
5. XGBoost

### 5. Model Evaluation

Evaluation metrics:

- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## 📊 Exploratory Data Analysis

Key observations from the dataset:

- The dataset contains 284,807 transactions.
- Only 492 transactions are fraudulent.
- Fraudulent transactions account for approximately 0.172% of the data.
- The dataset is highly imbalanced, making fraud detection a challenging classification problem.
- Most transaction amounts are relatively small, with a few high-value outliers.
- Features V1–V28 are PCA-transformed variables that preserve confidentiality while retaining predictive information.

These observations highlight the importance of using Precision, Recall, F1-Score, and ROC-AUC instead of relying solely on Accuracy.

---

## 📈 Model Performance Comparison

| Model | Precision | Recall | F1-Score |
|---------|---------|---------|---------|
| Logistic Regression | 0.83 | 0.64 | 0.72 |
| Logistic Regression + SMOTE | 0.06 | 0.92 | 0.11 |
| Random Forest | 0.94 | 0.83 | 0.88 |
| Random Forest + SMOTE | 0.87 | 0.83 | 0.85 |

---

## 🏆 Best Performing Model

### Random Forest

| Metric | Score |
|----------|----------|
| Precision | 0.94 |
| Recall | 0.83 |
| F1-Score | 0.88 |

### Why Random Forest?

Random Forest achieved the best balance between fraud detection capability and minimizing false alarms.

Benefits:

- High fraud detection precision
- Strong fraud recall
- Robust performance on imbalanced data
- Best overall F1-Score

---

## 📊 XGBoost Performance

| Metric | Value |
|----------|----------|
| ROC-AUC Score | 0.9528 |

A ROC-AUC score of 95.28% demonstrates excellent ability to distinguish fraudulent transactions from legitimate transactions.

---

## 🔍 Feature Importance (XGBoost)

Top features contributing to fraud prediction:

| Rank | Feature | Importance |
|---------|---------|---------|
| 1 | V17 | 0.1346 |
| 2 | V12 | 0.1258 |
| 3 | V14 | 0.1223 |
| 4 | V10 | 0.0893 |
| 5 | V16 | 0.0807 |
| 6 | V11 | 0.0804 |
| 7 | V7 | 0.0339 |
| 8 | V4 | 0.0316 |
| 9 | V9 | 0.0307 |
| 10 | V18 | 0.0305 |

---

## 📂 Project Structure

```text
credit-card-fraud-detection/
│
├── .gitignore
├── app.py
├── Credit_Card_Fraud_Detection.ipynb
├── requirements.txt
└── README.md
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Tamannapanwar17/credit-card-fraud-detection.git
```

Move into the project directory:

```bash
cd credit-card-fraud-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open:

```text
Credit_Card_Fraud_Detection.ipynb
```

Run all cells.

---

## 🧠 Skills Demonstrated

- Machine Learning
- Classification Modeling
- Fraud Detection
- Data Preprocessing
- Data Visualization
- Feature Scaling
- SMOTE Oversampling
- Ensemble Learning
- Random Forest
- XGBoost
- Model Evaluation
- Python Programming

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- LightGBM Implementation
- Deep Learning Models
- Streamlit Dashboard
- Real-Time Fraud Detection API
- Docker Deployment
- AWS/GCP Deployment

---

## 👩‍💻 Author

### Tamanna Panwar

Machine Learning Enthusiast | Aspiring Data Scientist

GitHub:
https://github.com/Tamannapanwar17

LinkedIn:
https://www.linkedin.com/in/tamanna-p-947299229/

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
