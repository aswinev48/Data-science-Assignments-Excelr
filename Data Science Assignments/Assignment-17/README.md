# 📈 Assignment 17 — Time Series Analysis & Forecasting

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on **Time Series Analysis**, specifically analyzing and forecasting currency exchange rates. The project involves identifying temporal patterns such as trends, seasonality, and noise to predict future values with statistical precision.

---

## 📘 About This Assignment

The primary objective of this project is to master the techniques used for analyzing data points collected sequentially over time. Key tasks include:

* **Exploratory Data Analysis (EDA):** Visualizing time series data to identify underlying trends and seasonal fluctuations in exchange rates.
* **Stationarity Testing:** Utilizing the **Augmented Dickey-Fuller (ADF) Test** to determine if the series' statistical properties change over time.
* **Time Series Decomposition:** Breaking down the data into **Trend**, **Seasonality**, and **Residual** components using additive or multiplicative models.
* **Forecasting Models:** Implementing and evaluating models such as **ARIMA (AutoRegressive Integrated Moving Average)** and **Exponential Smoothing**.
* **Performance Evaluation:** Measuring model accuracy using metrics like **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_17(Timeseries).ipynb`**: The main notebook covering data cleaning, decomposition, model fitting, and forecasting.
2. **`exchange_rate.csv`**: The dataset containing historical exchange rate data.
3. **`Timeseries.docx`**: Documentation of the core theoretical concepts for time series analysis and assignment requirements.

---

## 🚀 Sections Covered

### Data Pre-processing & Visualization
* Handling date-time indexing and ensuring a consistent frequency in the data.
* Visualizing the raw time series to detect potential outliers or structural breaks.

### Statistical Diagnostics
* **Rolling Statistics:** Visualizing moving averages and standard deviations to check for stationarity.
* **Autocorrelation (ACF) & Partial Autocorrelation (PACF):** Using plots to determine the appropriate parameters (p, d, q) for ARIMA models.



### Modeling & Forecasting
* **ARIMA/SARIMA:** Modeling the linear dependencies in the data for short-term forecasting.
* **Exponential Smoothing:** Applying Holt-Winters methods to capture both trend and seasonality.
* **Forecast Visualization:** Plotting predicted values against actual historical data to validate model performance.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `exchange_rate.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the Colab session for the script to load the time series data.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn
jupyter notebook
