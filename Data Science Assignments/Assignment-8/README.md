# 🐍 Assignment 8 — Logistic Regression Model Training & Deployment

**Author:** Aswin E V

**Platform:** Google Colab / Python

This assignment focuses on building a binary classification model using **Logistic Regression** to predict the likelihood of diabetes in patients based on medical diagnostic measurements. It covers the full lifecycle from data exploration to model deployment.

---

## 📘 About This Assignment

The primary objective of this project is to develop a reliable classification system. Key tasks include:

* **Classification Modeling:** Implementing a Logistic Regression algorithm to predict a binary outcome (Diabetes: Yes/No).
* **Feature Analysis:** Evaluating medical predictors such as **Glucose**, **Blood Pressure**, **BMI**, and **Age**.
* **Model Evaluation:** Using a **Confusion Matrix**, **Precision**, **Recall**, **F1-Score**, and **ROC-AUC curves** to measure performance.
* **Deployment Script:** Creating a standalone Python script (`Model_Dep.py`) to demonstrate how the trained model can be used for real-time predictions.
* **Data Pre-processing:** Handling scaling and splitting data into training and testing sets to ensure model generalizability.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_8(Logistic Regression Model Training).ipynb`**: The main notebook covering data analysis, model training, and evaluation.
2. **`diabetes.csv`**: The dataset containing patient health records.
3. **`Model_Dep.py`**: A Python deployment script designed to load the model and process new inputs.
4. **`Logistic Regression.docx`**: Documentation of the assignment requirements and theoretical concepts.

---

## 🚀 Sections Covered

### Exploratory Data Analysis (EDA)
* Visualization of class distribution to check for data imbalance.
* Correlation analysis to identify the strongest predictors of diabetes.

### Model Training & Tuning
* Splitting the dataset into 80% training and 20% testing sets.
* Training the Logistic Regression model using `scikit-learn`.
* Optimization of the decision threshold for better sensitivity.

### Performance Metrics
* **Confusion Matrix:** Visualizing True Positives, True Negatives, False Positives, and False Negatives.
* **ROC Curve:** Analyzing the trade-off between the True Positive Rate and False Positive Rate.

---

## ▶️ How to Run the Notebook & Script

### Running the Notebook (Colab)
1. Upload the `.ipynb` file and `diabetes.csv` to your Google Drive.
2. Open with **Google Colab**.
3. Run all cells to train the model and see the evaluation plots.

### Running the Deployment Script
To run the prediction script locally:
```bash
python Model_Dep.py
