# ✈️ Assignment 15 — Clustering Analysis

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Unsupervised Learning** through **Clustering Analysis**. Using data from the EastWestAirlines frequent flyer program, this project explores how to group passengers into distinct segments based on their travel patterns and loyalty program usage.

---

## 📘 About This Assignment

The primary objective of this project is to identify natural groupings within a dataset to inform targeted marketing and loyalty strategies. Key tasks include:

* **Hierarchical Clustering:** Building a dendrogram to visualize the nested groupings of passengers and determining the optimal number of clusters using different linkage methods.
* **K-Means Clustering:** Implementing the K-Means algorithm and utilizing the **Elbow Method** (Inertia) and **Silhouette Scores** to find the ideal number of clusters ($K$).
* **DBSCAN:** Exploring density-based clustering to identify core samples and filter out noise or outliers in the passenger data.
* **Data Standardization:** Pre-processing features like **Balance**, **Bonus Miles**, and **Flight Trans** using normalization to ensure equal weighting in distance calculations.
* **Segment Profiling:** Analyzing the characteristics of each cluster to provide actionable business insights.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_15(Clustering).ipynb`**: The main notebook containing the data pre-processing, implementation of all clustering algorithms, and cluster visualizations.
2. **`EastWestAirlines.xlsx - data.csv`**: The primary dataset containing information on 3,999 frequent flyer members.
3. **`EastWestAirlines.xlsx - Description.csv`**: Metadata explaining the meaning of variables like `Balance`, `Qual_miles`, and `cc1_miles`.
4. **`Clustering Analysis.docx`**: Documentation of the core theoretical concepts for Hierarchical, K-Means, and DBSCAN clustering.

---

## 🚀 Sections Covered

### Data Pre-processing
* Scaling the data to handle features with widely different ranges (e.g., total miles vs. number of transactions).

### Clustering Implementation
* **Hierarchical:** Visualizing passenger relationships through dendrograms.

* **K-Means:** Finding the "elbow" point to determine the most efficient number of segments.

* **DBSCAN:** Identifying outliers and high-density passenger groups.

### Business Interpretation
* Describing the resulting clusters (e.g., "High-Value Loyalists" vs. "Infrequent Travelers") based on their average feature values.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and both `.csv` files to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV files are uploaded to the Colab session storage.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn scipy
jupyter notebook
