# 🎌 Assignment 16 — Anime Recommendation System

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on building a **Recommendation System** to suggest anime to users based on their preferences. The project explores the core algorithms behind personalized content delivery, such as those used by Netflix, YouTube, and Amazon.

---

## 📘 About This Assignment

The primary objective of this project is to implement and evaluate different filtering techniques for content discovery. Key tasks include:

* **Collaborative Filtering:** Building a system that recommends items by identifying similar users and their shared interests.
* **Content-Based Filtering:** Recommending anime based on item metadata like **Genre**, **Type**, and **Rating**.
* **Similarity Measures:** Implementing and comparing distance metrics such as **Cosine Similarity** and **Pearson Correlation**.
* **Matrix Factorization:** Exploring techniques to handle sparse user-item interaction matrices.
* **Cold Start Problem:** Analyzing strategies for making recommendations for new users or items with no previous data.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_16(Recommendation System).ipynb`**: The main notebook containing data pre-processing, similarity matrix calculations, and recommendation logic.
2. **`anime.csv`**: The dataset containing information on thousands of anime, including genres, user ratings, and member counts.
3. **`Recommendation System.docx`**: Documentation of the core theoretical concepts for building recommendation engines and assignment requirements.

---

## 🚀 Sections Covered

### Data Pre-processing & EDA
* Cleaning the anime dataset and handling missing values in the genre and rating columns.
* Analyzing the distribution of user ratings to identify popular vs. niche content.

### Implementation of Recommendation Logic
* **User-Item Matrix:** Constructing a pivot table to represent user interactions.
* **Cosine Similarity:** Calculating the angular distance between vectors to find "neighbor" items or users.



### Model Evaluation
* Testing the system with specific anime titles to see if the recommendations are contextually relevant (e.g., suggesting other "Shounen" titles for a Naruto fan).
* Analyzing the diversity and serendipity of the suggested results.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `anime.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the session for the code to read the data correctly.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn
jupyter notebook
