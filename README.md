FUTURE_ML_01 – Sales Demand Forecasting System
Project Overview

This project is a Machine Learning-based Sales Demand Forecasting System designed to predict future sales using historical retail data. The system analyzes factors such as store information, promotional activities, product categories, and date-related features to generate accurate sales predictions.

The project follows a complete Machine Learning workflow, including data preprocessing, feature engineering, model training, evaluation, and deployment through a Flask web application. The forecasting model helps businesses make data-driven decisions related to inventory management, demand planning, workforce allocation, and sales strategy.

Objectives
Forecast future sales using historical business data.
Identify patterns and trends affecting sales performance.
Support inventory and demand planning decisions.
Provide a user-friendly web interface for sales prediction.
Dataset Used

The project utilizes retail sales datasets containing:

Historical sales records
Store information
Promotional activities
Holiday and event data
Oil price data
Transaction records
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Flask
Joblib
Jupyter Notebook
Machine Learning Workflow
Data Collection
Data Cleaning and Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Feature Selection
Train-Test Split
Model Training
Model Evaluation
Model Deployment
Feature Engineering

Date features were extracted to capture temporal patterns:

Year
Month
Day
Day of Week

Categorical variables were encoded for model training.

Model Used

Random Forest Regressor

The Random Forest Regression algorithm was used to learn sales patterns from historical data and generate future sales predictions.

Model Evaluation

The model was evaluated using:

Mean Absolute Error (MAE)
Root Mean Squared Error (RMSE)
R² Score

These metrics measure prediction accuracy and model performance.

Web Application

A Flask-based web application was developed to provide an interactive interface where users can enter sales-related inputs and receive instant sales forecasts.

Input Features
Store Number
Promotion Status
Product Family
Year
Month
Day
Day of Week
Output
Predicted Sales Value
Business Benefits
Improved inventory planning
Better demand forecasting
Reduced stock shortages and overstocking
Enhanced business decision-making
Support for sales and marketing strategies

Future Enhancements
Advanced forecasting models (XGBoost, LightGBM)
Interactive dashboards using Power BI or Tableau
Real-time sales forecasting
Cloud deployment and API integration
Automated model retraining