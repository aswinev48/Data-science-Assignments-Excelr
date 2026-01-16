# 🧠 Assignment 20 — Recurrent Neural Networks (RNN & LSTM)

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Deep Learning for Sequential Data** using **Recurrent Neural Networks (RNN)** and **Long Short-Term Memory (LSTM)** networks. The project demonstrates how to handle data where the order of observations matters, such as time-series forecasting and natural language sequences.

---

## 📘 About This Assignment

The primary objective of this project is to implement neural architectures that possess "memory" to capture temporal dependencies. Key tasks include:

* **Time-Series Forecasting:** Predicting future values of **Monthly Milk Production** based on historical trends.
* **RNN Architecture:** Building a sequential model that utilizes feedback loops to process sequences of data.
* **LSTM Implementation:** Utilizing LSTM cells to overcome the vanishing gradient problem and capture long-term dependencies.
* **Data Windowing:** Transforming time-series data into supervised learning format using sliding window sequences.
* **Sequence Modeling:** Exploring the theoretical foundations of many-to-one and many-to-many architectures for text and numerical sequences.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignement_20(RNN).ipynb`**: The main notebook containing the data pre-processing, RNN/LSTM model construction, and forecasting results.
2. **`monthly_milk_production.csv`**: The dataset containing historical records of milk production over several years.
3. **`Text Classification using RNN.docx`**: Documentation covering the theoretical application of RNNs in NLP and classification tasks.

---

## 🚀 Sections Covered

### Sequential Data Pre-processing
* **Scaling:** Applying `MinMaxScaler` to normalize time-series data, which is essential for the stability of neural network weights.
* **TimeSeriesGenerator:** Using Keras utilities to automatically create training batches of sequences.

### Model Development
* **SimpleRNN vs. LSTM:** Comparing the performance of basic recurrent layers against gated memory cells.



* **Dropout Layers:** Implementing regularization to prevent the model from overfitting on historical noise.

### Forecasting & Evaluation
* **In-Sample Prediction:** Testing the model's ability to "predict" the last known year of data.
* **Out-of-Sample Forecasting:** Generating future production values and visualizing the predicted trend against actual data.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `monthly_milk_production.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the Colab session or provided via a correct path.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib tensorflow scikit-learn
jupyter notebook
