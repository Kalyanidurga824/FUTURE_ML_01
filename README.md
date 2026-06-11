# 📊 Sales Demand Forecasting System

## 📌 Project Overview
This project is a Machine Learning-based Sales Demand Forecasting System developed using regression techniques.  
It predicts future sales based on historical data, store details, promotions, product categories, and date-related features.  
The goal is to help businesses improve inventory planning and decision-making efficiency.

---

## 📂 Dataset
- Store Sales / Retail Sales Dataset (Kaggle / Internal Sales Dataset)

---

## 🛠 Technologies Used
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- Matplotlib  
- Seaborn  
- Joblib  

---

## 🔄 Workflow
- Data Preprocessing  
- Handling Missing Values  
- Feature Engineering (Date, Month, Day, Weekday)  
- Encoding Categorical Variables  
- Train-Test Split  
- Random Forest Regression Model Training  
- Model Evaluation  
- Flask Web Application  

---

## 🎯 Features
- Sales Prediction based on input data  
- Store-wise forecasting  
- Promotion impact analysis  
- Date-based trend analysis  
- Interactive Flask web interface  
- Real-time prediction output  

---

## 🤖 Model
- Random Forest Regressor  

---

## 📈 Accuracy
- R² Score: ~85–90% (depending on dataset split)

---

## 🚀 How to Run
```bash
pip install -r requirements.txt  
python app/app.py  
```

---

## 📁 Project Structure
```
ml_sales_forecast/
│
├── app/
│   └── app.py
│
├── models/
│   └── model.pkl
│
├── data/
│   └── sales.csv
│
├── notebooks/
│   └── Sales_Forecasting.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🌐 Web Application
- Local URL: http://127.0.0.1:5000  
- Network URL: http://192.168.x.x:5000  
```