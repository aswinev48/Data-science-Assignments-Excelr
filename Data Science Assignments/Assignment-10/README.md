# 🐍 Assignment 10 — Support Vector Machine (SVM)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on implementing a **Support Vector Machine (SVM)** classifier within the pharmaceutical industry context. The goal is to predict drug response categories based on patient biomarkers and chemical properties, utilizing the power of high-dimensional margins.

---

## 📘 About This Assignment

The primary objective of this project is to master non-linear classification and margin optimization. Key tasks include:

* **SVM Classification:** Building a robust model to classify pharmaceutical drug responses using `SVC` from scikit-learn.
* **Kernel Exploration:** Experimenting with different kernels such as **Linear**, **Polynomial**, and **RBF (Radial Basis Function)** to handle non-linear data boundaries.
* **Hyperparameter Tuning:** Optimizing parameters like **C** (regularization) and **Gamma** to find the ideal balance between margin width and classification error.
* **Feature Engineering:** Pre-processing medical and chemical data through scaling to ensure optimal SVM performance.
* **Evaluation:** Assessing the model using a classification report, including **Precision**, **Recall**, and the **Confusion Matrix**.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_10(SVM).ipynb`**: The main notebook covering data pre-processing, kernel comparisons, and final model evaluation.
2. **`Pharma_Industry.csv`**: The dataset containing patient records and drug response indicators.
3. **`Support Vector mechine.docx`**: Documentation of the core SVM theoretical concepts and assignment requirements.
4. **`Drug Response Classification.docx`**: Detailed problem statement regarding the pharmaceutical classification task.

---

## 🚀 Sections Covered

### Data Pre-processing
* Scaling numerical features using **StandardScaler**, as SVM is highly sensitive to the scale of input data.
* Label encoding target variables to prepare for multi-class or binary classification.

### Model Development
* Implementing a base Linear SVM model for initial benchmarking.
* Transitioning to RBF and Polynomial kernels to capture complex, non-linear relationships in the pharmaceutical data.



### Analysis & Results
* **Hyperparameter Analysis:** Visualizing how the 'C' parameter impacts the decision boundary.
* **Confusion Matrix:** Detailed breakdown of misclassifications to understand model weaknesses in specific drug categories.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `Pharma_Industry.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the Colab session storage.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
