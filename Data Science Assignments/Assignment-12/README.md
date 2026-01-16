# 🌲 Assignment 12 — Random Forest Classification

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on implementing a **Random Forest** classifier to categorize different types of glass based on their chemical composition. By leveraging an ensemble of decision trees, this project demonstrates how to improve predictive accuracy and control overfitting in complex datasets.

---

## 📘 About This Assignment

The primary objective of this project is to master ensemble learning techniques. Key tasks include:

* **Ensemble Classification:** Developing a robust model to classify glass types (e.g., building windows, containers, headlamps) using the `RandomForestClassifier`.
* **Feature Analysis:** Evaluating chemical elements like **Refractive Index (RI)**, **Sodium (Na)**, **Magnesium (Mg)**, **Aluminum (Al)**, and **Silicon (Si)**.
* **Bagging & Randomness:** Understanding how Bootstrap Aggregating (Bagging) and random feature selection contribute to the model's stability.
* **Hyperparameter Tuning:** Optimizing parameters such as `n_estimators`, `max_features`, and `bootstrap` to enhance performance.
* **Out-of-Bag (OOB) Error:** Utilizing internal cross-validation to estimate the generalization accuracy of the forest.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment-12(Random Forest).ipynb`**: The main notebook covering data exploration, ensemble training, and model diagnostics.
2. **`glass.xlsx - glass.csv`**: The primary dataset containing chemical proportions and glass classifications.
3. **`glass.xlsx - Description.csv`**: Metadata explaining the specific chemical attributes and glass categories.
4. **`Random Forest.docx`**: Documentation of Random Forest theoretical concepts and assignment requirements.

---

## 🚀 Sections Covered

### Data Exploration & Preparation
* **Chemical Profiling:** Analyzing the distribution of elements across different glass types to find distinguishing characteristics.
* **Data Splitting:** Partitioning the dataset into training and testing sets to validate the ensemble's predictive power.

### Model Training & Ensemble Logic
* Building a forest of multiple decision trees to reduce variance.



### Performance Evaluation
* **Confusion Matrix:** Identifying which glass types are most commonly confused by the model.
* **Feature Importance:** Using the Random Forest's internal scoring to rank which chemical elements are most critical for classification.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and both `.csv` files to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV files are uploaded to your Colab session for the script to load the data.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
