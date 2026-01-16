# 🐍 Assignment 5 — Exploratory Data Analysis (EDA)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Exploratory Data Analysis (EDA)** using a Cardiotocography dataset. The goal is to perform a deep dive into the data to understand its structure, identify patterns, and prepare it for further statistical or machine learning analysis.

---

## 📘 About This Assignment

The primary objective of this notebook is to clean and explore medical data to uncover underlying trends. Key tasks include:

* **Data Profiling:** Examining the dataset for types, non-null counts, and basic structural information.
* **Univariate Analysis:** Analyzing individual features like Fetal Heart Rate (FHR) and uterine contractions using statistical summaries.
* **Bivariate Analysis:** Investigating the relationships between different fetal health parameters.
* **Data Visualization:** Using Seaborn and Matplotlib to create insightful charts such as Histograms, Box Plots, and Heatmaps.
* **Outlier Detection:** Identifying anomalies in the data that could impact diagnostic accuracy.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_5(EDA).ipynb`**: The main Google Colab notebook containing the complete exploratory analysis and visualizations.
2. **`Cardiotocographic.csv`**: The dataset containing fetal heart rate and uterine contraction data.
3. **`EDA1.docx`**: Documentation of the assignment requirements and project goals.

---

## 🚀 Sections Covered

### Data Cleaning & Pre-processing
* Handling missing values and ensuring numerical consistency across medical measurements.
* Renaming columns for better readability and standardizing units.

### Statistical Exploration
* **Central Tendency:** Calculating mean and median for critical fetal health indicators.
* **Spread & Skewness:** Analyzing the variance and distribution of heart rate variability.

### Visual Insights
* **Correlation Heatmaps:** Visualizing how different features interact with each other.
* **Distribution Plots:** Using KDE and Histograms to see the frequency of specific medical readings.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `Cardiotocographic.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is loaded correctly in the Colab environment.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn
jupyter notebook
