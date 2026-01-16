# ✍️ Assignment 19 — Natural Language Processing (NLP)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Natural Language Processing (NLP)** to perform sentiment analysis on Amazon reviews. The goal is to build a computational model that can automatically classify text as positive or negative by understanding the linguistic patterns within customer feedback.

---

## 📘 About This Assignment

The primary objective of this project is to master the text pre-processing and vectorization pipeline required for machine learning with unstructured data. Key tasks include:

* **Text Pre-processing:** Implementing tokenization, stop-word removal, and stemming/lemmatization to clean raw review data.
* **Vectorization:** Converting text into numerical format using techniques like **TF-IDF (Term Frequency-Inverse Document Frequency)** or **Bag of Words**.
* **Sentiment Classification:** Training a classifier (such as Naive Bayes or Logistic Regression) to predict review sentiment.
* **N-grams Analysis:** Exploring combinations of words (bigrams/trigrams) to capture more context from the reviews.
* **Model Evaluation:** Using Accuracy, Precision, Recall, and the Confusion Matrix to assess how well the model identifies customer sentiment.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_19(NLP).ipynb`**: The main notebook containing the full NLP pipeline, from text cleaning to model prediction.
2. **`amazonreviews.tsv`**: The dataset containing thousands of Amazon customer reviews and their corresponding labels.
3. **`Natural language processing.docx`**: Documentation of the core theoretical concepts for NLP and assignment requirements.

---

## 🚀 Sections Covered

### Text Cleaning & Tokenization
* Removing special characters, numbers, and punctuation.
* Converting text to lowercase and filtering out common stop-words (e.g., "the", "is", "at").

### Feature Extraction
* Transforming the cleaned text into a sparse matrix of TF-IDF features.
* Analyzing word importance across the entire corpus of reviews.



### Sentiment Prediction
* **Classification:** Training the model to distinguish between positive and negative reviews.
* **Word Clouds:** Visualizing the most frequent words used in positive versus negative feedback.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `amazonreviews.tsv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the `.tsv` file is uploaded to the Colab session storage for the script to load the data.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn nltk scikit-learn
jupyter notebook
