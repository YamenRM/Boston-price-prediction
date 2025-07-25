# 🏠 Boston Housing Price Prediction
This project predicts housing prices in Boston using machine learning techniques. It includes data preprocessing, feature engineering with polynomial features, model training with LassoCV, and deployment via a Streamlit web app.

# 📊 Dataset :-

Link : https://www.kaggle.com/datasets/vikrishnan/boston-house-prices

**📌 Feature Descriptions :**

CRIM :	Per capita crime rate by town

ZN :	Proportion of residential land zoned for large lots

INDUS :	Proportion of non-retail business acres

CHAS :	Charles River dummy variable (= 1 if tract bounds river)

NOX :	Nitric oxide concentration

RM :	Average number of rooms per dwelling

AGE :	Proportion of owner-occupied units built before 1940

DIS :	Weighted distances to employment centers

RAD :	Index of accessibility to radial highways

TAX :	Property-tax rate

PTRATIO :	Pupil-teacher ratio

LSTAT : % lower status of the population

MEDV :	Median value of owner-occupied homes (target)


# 🧠 Goals :-
 - Preprocess and engineer features using PolynomialFeatures.

 - Train a robust regression model using LassoCV with built-in cross-validation.

 - Evaluate the model thoroughly using MAE, MSE, RMSE, and R².

 - Deploy the model via a Streamlit app to make real-time predictions.

# 🔧 Technical Stack :-

 - Preprocessing :	StandardScaler, PolynomialFeatures

 - Modeling :	LassoCV (cross-validated L1 regression)

 - Model Evaluation :	mean_absolute_error, mean_squared_error, r2_score

 - Pipeline Creation :	Pipeline from sklearn

 - Serialization	: joblib

 - App Deployment : streamlit

# 🧪 Model Performance :-

 - MAE	: ~2.13
 - MSE	: ~13.09
 - RMSE :	~3.62
 - R² :	0.82 ✅

# 🧳 Why This Project Matters :-
 - This project is designed to reflect real-world ML workflows:

 - End-to-end process: from raw data to deployment.

 - Cross-validation with regularization.

 - Feature engineering with polynomial interactions.

 - Production-ready pipeline serialization.

 - Real-time inference in a web app.

# 👤 Author :-
 - Yamen Rafat Abu-Mailq , Palestine , GAZA  , UP

  💪 Stay strong
