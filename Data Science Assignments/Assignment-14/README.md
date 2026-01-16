# 🍷 Assignment 14 — Principal Component Analysis (PCA)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Dimensionality Reduction** using **Principal Component Analysis (PCA)**. By transforming a high-dimensional wine dataset into a lower-dimensional space, this project demonstrates how to retain maximum variance while simplifying the data for visualization and clustering.

---

## 📘 About This Assignment

The primary objective of this project is to master unsupervised learning and feature extraction. Key tasks include:

* **Dimensionality Reduction:** Reducing the complexity of the wine dataset while preserving the essential patterns and variance.
* **Feature Transformation:** Converting 13 chemical attributes into a set of linearly uncorrelated Principal Components (PCs).
* **Variance Analysis:** Utilizing **Scree Plots** and cumulative variance ratios to determine the optimal number of components.
* **Data Visualization:** Creating 2D and 3D scatter plots to visualize how different wine varieties cluster in the reduced feature space.
* **Clustering Comparison:** Applying K-Means or Hierarchical clustering on the PCA-transformed data to observe improvements in cluster separation.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_14(PCA).ipynb`**: The main notebook containing the data standardization, PCA implementation, and visualization code.
2. **`wine.csv`**: The dataset containing chemical analysis results of wines grown in the same region in Italy but derived from three different cultivars.
3. **`PCA.docx`**: Documentation of the core theoretical concepts of Principal Component Analysis and assignment requirements.

---

## 🚀 Sections Covered

### Data Pre-processing
* **Standardization:** Using `StandardScaler` to ensure all chemical features (like Alcohol, Malic acid, and Ash) have a mean of 0 and variance of 1, which is critical for PCA performance.

### PCA Implementation
* Computing the covariance matrix and identifying eigenvalues and eigenvectors.
* Selecting the top Principal Components that capture the majority of the dataset's information.



### Visual Insights
* **Biplots:** Visualizing both the position of the data points and the loading vectors of the original features.
* **Cluster Separation:** Observing how the three different wine cultivars become distinct when projected onto the first two principal components.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `wine.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the Colab session for the script to load the data.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
