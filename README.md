# 🚗 Used Car Price Prediction – Regression Analysis

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nikkibhoot-29/UsedCarPrice-Regression-Analysis/blob/main/Regression%20Case%20Study%20-%20Portfolio.ipynb)

## 📌 Project Overview
This project focuses on predicting used car prices using machine learning regression techniques.  
The dataset was cleaned, processed, and analyzed to build predictive models capable of estimating car prices based on multiple features.  
This project demonstrates both exploratory analysis using Jupyter Notebook and a production-style implementation using a structured Python script.

---

## 🎯 Problem Statement
Develop a regression model that accurately predicts the price of used cars based on relevant attributes such as vehicle age, power, brand, and other characteristics.

---

## 🛠️ Project Workflow

### 1️⃣ Data Cleaning & Preprocessing
- Removed irrelevant columns  
- Handled missing values (Omitted & Imputed versions)  
- Treated extreme outliers (price, power, registration year)  

### 2️⃣ Feature Engineering
- Created new variable **Age** from year and month of registration  
- Encoded categorical variables using dummy encoding  

### 3️⃣ Model Building
- Linear Regression  
- Random Forest Regressor  

### 4️⃣ Model Evaluation
Models were evaluated using:
- Mean Squared Error (MSE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 📊 Results

| Model              | R² Score   |
|--------------------|------------|
| Linear Regression  | 0.65 – 0.68 |
| Random Forest      | 0.77 – 0.81 |

✅ Random Forest performed better by capturing non-linear relationships in the dataset.

---

## 🧰 Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## 📂 Repository Structure
- `Regression Case Study - Portfolio.ipynb` → Main analysis notebook  
- `main.py` → Modular Python script for end-to-end ML pipeline  
- `cars_sampled.csv` → Dataset used for training and evaluation   

---

## ▶️ How to Run

### Option 1: Run Notebook
Click the **Open in Colab** badge above and run all cells.

### Option 2: Run Python Script
Make sure required libraries are installed, then run:
`python main.py`

## 📌 Key Highlights
- End-to-end regression modeling workflow  
- Data preprocessing & feature engineering  
- Model building & performance comparison  

---
