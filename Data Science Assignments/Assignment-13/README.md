# 🐍 Assignment 13 — Gradient Boosting (XGBM & LGBM)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on implementing advanced boosting algorithms, specifically **XGBoost (Extreme Gradient Boosting)** and **LightGBM (Light Gradient Boosting Machine)**. Using medical data, this project explores how gradient-boosted trees can be used to achieve high predictive accuracy for disease classification.

---

## 📘 About This Assignment

The primary objective of this project is to master state-of-the-art boosting techniques used in competitive data science. Key tasks include:

* **Gradient Boosting Classification:** Developing high-performance models to predict diabetes using both the `XGBClassifier` and `LGBMClassifier`.
* **Algorithmic Comparison:** Analyzing the differences between XGBoost’s level-wise growth and LightGBM’s leaf-wise growth strategies.
* **Hyperparameter Optimization:** Tuning parameters such as `learning_rate`, `n_estimators`, `max_depth`, and `reg_alpha` to maximize the Area Under the Curve (AUC).
* **Speed & Efficiency:** Evaluating the computational advantages of LightGBM's histogram-based algorithms on the dataset.
* **Feature Importance:** Utilizing the built-in importance plots of both libraries to identify the most significant clinical predictors.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_13(XGBM & LGBM).ipynb`**: The main notebook containing the data pipeline, model training for both XGBoost and LightGBM, and evaluation metrics.
2. **`diabetes.csv`**: The dataset containing diagnostic measurements for classification.
3. **`LGBM & XGBM.docx`**: Documentation of the core theoretical concepts for both boosting frameworks and assignment requirements.

---

## 🚀 Sections Covered

### Data Analysis & Preparation
* Cleaning medical records and handling features like Glucose, BMI, and Insulin levels.
* Scaling data where necessary, though boosting models are generally robust to feature scaling.

### Boosting Model Implementation
* **XGBoost:** Implementing the level-wise tree growth approach known for its strong regularization features.
* **LightGBM:** Implementing the faster, leaf-wise growth approach optimized for lower memory usage.



### Evaluation & Comparison
* **Metrics:** Comparing models using Accuracy, Precision-Recall, and F1-score.
* **ROC-AUC:** Plotting the Receiver Operating Characteristic curve to compare the diagnostic ability of both models.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `diabetes.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the Colab session for the script to read the data.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn xgboost lightgbm scikit-learn
jupyter notebook
