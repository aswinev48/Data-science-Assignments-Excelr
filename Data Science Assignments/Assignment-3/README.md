# 🐍 Assignment 3 — Basic Statistics (Level 1)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Descriptive Statistics** and **Exploratory Data Analysis (EDA)**. It involves analyzing sales data to understand distributions, central tendencies, and the relationships between different numerical and categorical variables.

---

## 📘 About This Assignment

The primary goal of this notebook is to perform a comprehensive statistical analysis on a sales dataset. Key tasks include:

* **Descriptive Statistics:** Calculating Mean, Median, Mode, and Standard Deviation for numerical columns.
* **Data Visualization:** Creating Histograms to understand data distribution and Box Plots to identify outliers.
* **Feature Engineering:** Implementing Dummy Variables for categorical data to prepare it for machine learning models.
* **Correlation Analysis:** Evaluating the relationships between Price, Quantity, and Discounts.
* **Data Transformation:** Applying Skewness analysis and identifying data types.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_3(Basic Stats-1).ipynb`**: The main Google Colab notebook containing all statistical calculations and visualizations.
2. **`sales_data_with_discounts.csv`**: The raw dataset used for the analysis.
3. **`Basic statistics.docx`**: Documentation of the assignment requirements and problem statements.

---

## 🚀 Sections Covered

### Statistical Analysis
* Analysis of numerical columns: **Volume**, **Avg Price**, **Total Sales Value**, and **Discount Rate**.
* Comparing Mean, Median, and Mode to determine the skewness of the data.

### Data Visualization
* **Histograms:** Visualizing the frequency distribution of sales metrics.
* **Box Plots:** Identifying the spread of data and detecting potential outliers in pricing and volume.

### Pre-processing & Transformation
* **Categorical Encoding:** Converting 'Day' into dummy variables (One-Hot Encoding).
* **Data Standardization:** Preparing numerical features for further analysis.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `sales_data_with_discounts.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file path in the code matches your Drive location.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas matplotlib seaborn
jupyter notebook
