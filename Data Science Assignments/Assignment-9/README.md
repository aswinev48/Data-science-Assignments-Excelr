# 🐍 Assignment 9 — Data Transformation & Feature Engineering

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on the critical phase of the Data Science pipeline: **Data Transformation**. Using the "Adult" census dataset, this project demonstrates how to convert raw data into a high-quality format suitable for machine learning models through advanced scaling, encoding, and transformation techniques.

---

## 📘 About This Assignment

The primary objective of this notebook is to master feature engineering and data pre-processing. Key tasks include:

* **Data Cleaning:** Identifying and handling missing values, duplicates, and inconsistent entries in the census data.
* **Feature Scaling:** Applying **StandardScaler** and **MinMaxScaler** to normalize numerical features like `age`, `education-num`, and `hours-per-week`.
* **Categorical Encoding:** Implementing **Label Encoding** and **One-Hot Encoding** for variables such as `workclass`, `education`, and `occupation`.
* **Handling Skewness:** Identifying skewed numerical distributions and applying Log or Power transformations to achieve a more Gaussian-like distribution.
* **Dimensionality Reduction:** Exploring techniques to simplify the dataset while retaining essential information.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_9(Data Transformation).ipynb`**: The main notebook containing all pre-processing steps, code implementations, and comparative analysis of scaling methods.
2. **`adult_with_headers.csv`**: The census dataset used for the transformation tasks.
3. **`Data Trasformation.docx`**: Documentation detailing the specific transformation requirements and theoretical questions.

---

## 🚀 Sections Covered

### Exploratory Data Analysis (EDA)
* Statistical summary of numerical features to detect variance and scale differences.
* Visualizing categorical distributions to identify high-cardinality features.

### Feature Engineering Pipeline
* **Normalizing vs. Standardizing:** A comparative study on when to use Min-Max scaling versus Z-score normalization.
* **Encoding Strategies:** Strategic use of One-Hot encoding for nominal data versus Label encoding for ordinal data.

### Transformation Analysis
* Using Histograms and Q-Q plots to visualize the data distribution before and after transformations.
* Analyzing the impact of these transformations on potential model performance.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `adult_with_headers.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is accessible to the notebook environment.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
