# 🐍 Assignment 4 — Basic Statistics (Level 2)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on advanced **Descriptive Statistics** and **Data Merging** techniques. It involves analyzing healthcare data across multiple datasets to uncover insights into patient billing, stay durations, and departmental performance.

---

## 📘 About This Assignment

The primary goal of this notebook is to perform statistical inference and data consolidation on hospital records. Key tasks include:

* **Data Integration:** Merging `Patient_Data` and `Billing_Data` using common identifiers to create a unified view.
* **Stay Analysis:** Calculating the duration of patient stays and analyzing the distribution of hospital days.
* **Financial Metrics:** Performing descriptive statistics on billing amounts to identify average costs and revenue drivers.
* **Categorical Analysis:** Grouping data by Department and Gender to find trends in healthcare utilization.
* **Advanced Statistics:** Calculating variance, skewness, and identifying outliers in medical billing.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_4(Basic stats - 2).ipynb`**: The main Google Colab notebook containing all data cleaning, merging, and statistical analysis.
2. **`Patient_Data.csv`**: Dataset containing patient demographics and admission details.
3. **`Billing_Data.csv`**: Dataset containing financial records and billing information.
4. **`Basic statistics-2.docx`**: Documentation of the assignment requirements and problem statements.

---

## 🚀 Sections Covered

### Data Merging & Cleaning
* Joining datasets using `Patient_ID` as the primary key.
* Handling missing values and ensuring data type consistency (dates, currency).

### Descriptive Statistics
* **Central Tendency:** Analyzing the mean and median of billing amounts.
* **Dispersion:** Calculating Standard Deviation and Range for patient age and stay duration.

### Healthcare Insights
* **Departmental Performance:** Identifying which hospital departments generate the highest billing volume.
* **Trend Analysis:** Visualizing the relationship between patient age and the cost of treatment.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and both `.csv` files to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the file paths in the `pd.read_csv()` commands match your Drive folder structure.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas matplotlib seaborn numpy
jupyter notebook
