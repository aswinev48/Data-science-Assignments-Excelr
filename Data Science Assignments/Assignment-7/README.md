# 🐍 Assignment 7 — Multiple Linear Regression (MLR)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on building and refining a **Multiple Linear Regression** model to predict the price of used Toyota Corolla cars. The goal is to identify which technical and physical attributes most significantly impact a vehicle's market value.

---

## 📘 About This Assignment

The primary objective of this notebook is to implement a complete predictive modeling pipeline. Key tasks include:

* **Feature Selection:** Analyzing multiple independent variables such as **Age**, **Mileage (KM)**, **Horsepower (HP)**, **Engine Volume (cc)**, and **Weight** to predict the **Price**.
* **Correlation Analysis:** Using heatmaps to detect multicollinearity between car features.
* ]**Model Building:** Implementing MLR using both `statsmodels` for detailed statistical summaries and `scikit-learn` for predictive accuracy.
* **Model Diagnostics:** Checking for assumptions of linearity, homoscedasticity, and normality of residuals.
* **Performance Evaluation:** Calculating metrics like **R-squared**, **Adjusted R-squared**, and **Root Mean Squared Error (RMSE)** to validate the model.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_7(MLR).ipynb`**: The main Google Colab notebook containing the end-to-end regression analysis and model code.
2. **`ToyotaCorolla - MLR.csv`**: The dataset containing specifications and pricing for 1,436 Toyota Corolla vehicles.
3. **`Multiple Linear Regression.docx`**: Documentation of the assignment requirements and specific technical questions.

---

## 🚀 Sections Covered

### Exploratory Data Analysis (EDA)
* Visualization of relationships between price and physical features (Weight, Doors, Gears).
* Identification of influential data points and outliers using Cook's Distance.

### Regression Modeling
* **Model 1 (Base):** Building an initial model with all primary features.
* **Model Refinement:** Improving the model by handling multicollinearity (Variance Inflation Factor - VIF) and removing insignificant variables.

### Residual Analysis
* Generating Q-Q plots to verify the normality of error terms.
* Residual vs. Fitted plots to check for constant variance.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `ToyotaCorolla - MLR.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the file path in the `read_csv` function matches the location of your uploaded dataset.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels
jupyter notebook
