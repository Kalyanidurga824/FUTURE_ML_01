📊 Sales Demand Forecasting System
# Project Overview

This project is a Machine Learning-based Sales Demand Forecasting System developed using Regression techniques.
The system predicts future sales based on historical data, store details, promotions, product categories, and date-related features to help businesses improve inventory planning and decision-making efficiency.

# Dataset

• Store Sales / Retail Sales Dataset (Kaggle / Internal Sales Dataset)

# Technologies Used

• Python
• Pandas
• NumPy
• Scikit-learn
• Flask
• Matplotlib
• Seaborn
• Joblib

# Workflow

• Data Preprocessing
• Handling Missing Values
• Feature Engineering (Date, Month, Day, Weekday)
• Encoding Categorical Variables
• Train-Test Split
• Random Forest Regression Model Training
• Model Evaluation
• Flask Web Application

# Features

• Sales Prediction Based on Input Data
• Store-wise Forecasting
• Promotion Impact Analysis
• Date-based Trend Analysis
• Interactive Flask Web Interface
• Real-time Prediction Output

# Model

• Random Forest Regressor

# Accuracy

• R² Score: ~85–90% (depending on dataset split)

# How to Run
pip install -r requirements.txt  
python app/app.py  
# Project Structure
ml_sales_forecast/
│
├── app/
│   └── app.py
├── models/
│   └── model.pkl
├── data/
│   └── sales.csv
├── notebooks/
│   └── Sales_Forecasting.ipynb
├── requirements.txt
├── README.md
└── .gitignore
# Future Improvements

• Deep Learning-based Time Series Models (LSTM, Prophet)
• Real-time Sales Dashboard
• Cloud Deployment (AWS / Render / Azure)
• Automated Data Pipeline
• Advanced Feature Engineering

# Web Application

• Local URL: http://127.0.0.1:5000
• Network URL: http://192.168.x.x:5000