# 🧠 Assignment 18 — Neural Networks for Binary Classification

**Author:** Aswin E V

**Platform:** Google Colab

This assignment focuses on implementing **Artificial Neural Networks (ANN)** to solve a complex binary classification problem. Using the Sonar dataset, this project demonstrates how to build, train, and evaluate a deep learning model to distinguish between rocks and naval mines based on sonar signals.

---

## 📘 About This Assignment

The primary objective of this project is to master the fundamentals of Deep Learning using Keras and TensorFlow. Key tasks include:

* **Neural Network Architecture:** Designing a multi-layer perceptron (MLP) with input, hidden, and output layers.
* **Activation Functions:** Implementing **ReLU** for hidden layers to handle non-linearity and **Sigmoid** for the output layer to provide probability estimates.
* **Optimization & Loss:** Utilizing the **Adam optimizer** and **Binary Cross-Entropy** loss function for efficient model training.
* **Backpropagation:** Understanding how the model learns by updating weights and biases through gradient descent.
* **Model Evaluation:** Analyzing performance through **Accuracy**, **Loss curves**, and **Confusion Matrices**.

---

## 🗒️ Files Included

This folder contains the following resources:

1. **`Assignment_18(Neural_Networks).ipynb`**: The main notebook containing the data pre-processing, ANN architecture definition, and model training.
2. **`sonardataset.csv`**: The dataset containing 60 sonar return patterns for classification.
3. **`Neural Networks.docx`**: Documentation of the core theoretical concepts for Deep Learning and assignment requirements.

---

## 🚀 Sections Covered

### Data Pre-processing
* Scaling the 60 numerical features to a uniform range to improve the convergence speed of the neural network.
* Label encoding the target variable ('M' for Mine, 'R' for Rock).

### Model Training & Architecture
* **Input Layer:** 60 neurons corresponding to the sonar features.
* **Hidden Layers:** Experimenting with different numbers of neurons and layers to optimize performance.
* **Output Layer:** A single neuron with a sigmoid activation for binary classification.

[Image of an artificial neural network diagram with input, hidden, and output layers]

### Performance Monitoring
* **Training vs. Validation Loss:** Plotting loss curves to detect potential overfitting or underfitting.
* **Accuracy Metrics:** Evaluating how many signals were correctly identified in the test set.

---

## ▶️ How to Run the Notebook

### Open in Google Colab
1. Upload the `.ipynb` file and the `sonardataset.csv` file to your Google Drive.
2. Right-click the `.ipynb` file → **Open with** → **Google Colab**.
3. Ensure the CSV file is uploaded to the Colab session or provided via a correct path.

### Run Locally (optional)
Install the required libraries:
```bash
pip install pandas numpy matplotlib tensorflow scikit-learn
jupyter notebook
