# 💳 Credit Card Fraud Detection using Machine Learning

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge)
![XGBoost](https://img.shields.io/badge/XGBoost-Gradient%20Boosting-success?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

## 📌 Overview

Credit card fraud is a major challenge for financial institutions worldwide. Due to the highly imbalanced nature of transaction data, detecting fraudulent activities accurately is difficult.

This project develops a Machine Learning-based Fraud Detection System capable of identifying fraudulent transactions from legitimate ones using historical transaction data.

The project explores multiple machine learning algorithms and evaluates their performance using industry-standard metrics such as Precision, Recall, F1-Score, and ROC-AUC.

---

## 🚀 Highlights

✅ Built an end-to-end fraud detection pipeline on 284,807 real-world transactions

✅ Compared multiple machine learning models:
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

Financial institutions process millions of transactions every day. Even a small percentage of fraudulent transactions can result in significant financial losses.

The goal of this project is to develop a machine learning model that can:

- Detect fraudulent transactions accurately
- Minimize false negatives
- Handle highly imbalanced datasets effectively

---

## 📊 Dataset Information

### Dataset

Credit Card Fraud Detection Dataset

### Source

Kaggle

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

### Dataset Characteristics

- Total Transactions: 284,807
- Fraudulent Transactions: 492
- Legitimate Transactions: 284,315
- Highly Imbalanced Dataset

### Features

| Feature Type | Description |
|-------------|-------------|
| Time | Seconds elapsed between transactions |
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

- Imported dataset
- Explored dataset structure
- Checked class distribution

### 2. Data Preprocessing

- Missing value analysis
- Feature scaling
- Train-test split
- Class imbalance analysis

### 3. Handling Imbalanced Data

- SMOTE (Synthetic Minority Oversampling Technique)
- Comparison with original dataset performance

### 4. Model Training

Models used:

1. Logistic Regression
2. Logistic Regression + SMOTE
3. Random Forest
4. Random Forest + SMOTE
5. XGBoost

### 5. Model Evaluation

Metrics used:

- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

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

### Random Forest (Without SMOTE)

Fraud Class Performance:

| Metric | Score |
|----------|----------|
| Precision | 0.94 |
| Recall | 0.83 |
| F1-Score | 0.88 |

Why it performed best:

- High precision reduced false alarms
- Strong recall detected most fraud cases
- Best balance between precision and recall

---

## 📊 XGBoost Performance

### ROC-AUC Score

| Metric | Value |
|----------|----------|
| ROC-AUC | 0.9528 |

A ROC-AUC score of 95.28% indicates excellent discrimination between fraudulent and legitimate transactions.

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
├── creditcard.csv
├── Credit_Card_Fraud_Detection.ipynb
├── README.md
├── requirements.txt
└── screenshots/
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/Tamannapanwar17/credit-card-fraud-detection.git
```

### Move Into Project Directory

```bash
cd credit-card-fraud-detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Open Jupyter Notebook:

```bash
jupyter notebook
```

or upload the notebook to Google Colab and run all cells.

---

## 📷 Project Outputs

Add screenshots of:

- Dataset Distribution
- Correlation Heatmap
- Confusion Matrix
- ROC Curve
- Feature Importance Plot

Example:

```text
screenshots/
├── class_distribution.png
├── confusion_matrix.png
├── roc_curve.png
└── feature_importance.png
```

---

## 💡 Key Learnings

- Data preprocessing techniques
- Handling imbalanced datasets
- SMOTE oversampling
- Classification algorithms
- Ensemble learning methods
- Fraud detection systems
- Model evaluation on real-world datasets

---

## 🔮 Future Improvements

- Hyperparameter Tuning
- LightGBM Implementation
- Deep Learning Models
- Real-Time Fraud Detection API
- Streamlit Deployment
- Docker Containerization
- Cloud Deployment (AWS/GCP)

---

## 🤝 Contributing

Contributions are welcome.

Feel free to fork this repository and submit a pull request.

---

## 👩‍💻 Author

### Tamanna Panwar

Aspiring Machine Learning Engineer | Data Science Enthusiast

GitHub:
https://github.com/Tamannapanwar17

LinkedIn:
https://www.linkedin.com/in/tamanna-p-947299229/

---

## ⭐ Support

If you found this project useful, please consider giving it a star on GitHub.

A star helps others discover the project and motivates further improvements.
