# 🌳 Assignment 11 — Decision Tree Classification

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on implementing a **Decision Tree** classifier to predict the presence of heart disease. The project involves building a tree-based model that can make clinical predictions by splitting data based on key health indicators like cholesterol, age, and blood pressure.

---

## 📘 About This Assignment

The primary objective of this project is to understand the logic of recursive partitioning and tree pruning. Key tasks include:

* **Tree Classification:** Developing a model to classify patients into "Heart Disease" or "No Heart Disease" categories using the `DecisionTreeClassifier`.
* **Attribute Selection:** Evaluating features like **Chest Pain Type**, **Maximum Heart Rate**, and **Thallium Stress Test** results.
* **Information Gain:** Utilizing metrics such as **Gini Impurity** and **Entropy** to determine the best splits at each node.
* **Pruning & Optimization:** Implementing hyperparameter tuning (like `max_depth` and `min_samples_leaf`) to prevent the model from overfitting.
* **Visualization:** Generating a visual representation of the decision tree to interpret the decision logic.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_11(Decison Tree).ipynb`**: The main notebook covering data cleaning, tree induction, and model evaluation.
2. **`heart_disease.xlsx - Heart_disease.csv`**: The primary dataset containing patient clinical records.
3. **`heart_disease.xlsx - Description.csv`**: Metadata explaining the meaning of the various health attributes.
4. **`Decision Tree.docx`**: Documentation of the core Decision Tree theoretical concepts and assignment requirements.

---

## 🚀 Sections Covered

### Data Analysis & Preparation
* Cleaning the heart disease dataset and handling any missing values or categorical encoding.
* Splitting the data into training and testing sets to validate model performance on unseen patients.

### Model Training
* Training the classifier and experimenting with both Gini and Entropy criteria.



### Performance Evaluation
* **Confusion Matrix:** Analyzing the balance between sensitivity (identifying patients with heart disease) and specificity.
* **Feature Importance:** Ranking which clinical factors (e.g., age vs. cholesterol) are the strongest predictors in the tree.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and both `.csv` files to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV files are uploaded to the session for the code to read the data correctly.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
