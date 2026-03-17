🏠 House Price Prediction System using Machine Learning
📌 Project Overview

This project is a Machine Learning-based web application that predicts house prices based on various features such as income, house age, number of rooms, population, and location.

The model is trained using historical housing data and deployed using Streamlit, allowing users to input details and get real-time price predictions.

🚨 Problem Statement

Determining the correct price of a house is a complex task influenced by multiple factors like location, size, and economic conditions.

Manual estimation can lead to incorrect pricing, affecting both buyers and sellers. Therefore, an automated system using Machine Learning is required to predict accurate house prices.

🤖 Machine Learning Algorithm Used
Linear Regression

Linear Regression is a supervised learning algorithm used for predicting continuous values.

It works by finding a relationship between input features and the target variable (house price).

Formula

y = b0 + b1x1 + b2x2 + ... + bnxn

Where:

y = Predicted house price

x = Input features

b = Coefficients learned by the model

📊 Dataset Used

Dataset Name: California Housing Dataset

Source: Scikit-learn

Features include:

Median Income

House Age

Average Rooms

Average Bedrooms

Population

Average Occupancy

Latitude

Longitude

Target Variable:

House Price

🛠️ Technologies Used

Python

NumPy

Pandas

Scikit-learn

Matplotlib

Streamlit

⚙️ Machine Learning Workflow

Data Collection

Data Preprocessing

Train-Test Split

Model Training

Model Evaluation

Model Saving

Deployment using Streamlit

📈 Model Evaluation

The model is evaluated using:

Mean Squared Error (MSE)

R² Score

R² Score explains how well the model predicts house prices.

📂 Project Structure

HousePricePrediction/

app.py → Streamlit application

house_model.pkl → Trained model

requirements.txt → Dependencies

README.md → Project documentation

🚀 How to Run the Project
Step 1: Clone Repository

git clone https://github.com/GopinathR07/House-Price-PredictionModel/tree/main

Step 2: Navigate to Folder

cd house-price-prediction

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Run Application

streamlit run app.py

🌐 Deployment

This project is deployed using Streamlit Cloud.

Steps:

Upload project to GitHub

Connect GitHub to Streamlit Cloud

Select app.py

Deploy

🎯 Key Features

Real-time house price prediction

Simple and interactive UI

Fast and efficient model

Easy to use

🔮 Future Improvements

Use advanced models like Random Forest or XGBoost

Add more real-world features

Improve UI design

Deploy using Docker or cloud platforms

👨‍💻 Author

Gopinath R
Computer Science Student
Machine Learning Enthusiast


🔗 Connect

LinkedIn: https://www.linkedin.com/in/gopinath-r-90852233a/
GitHub: https://github.com/GopinathR07

#MachineLearning #AI #DataScience #Python #Streamlit #Regression
