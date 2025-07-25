import pandas as pd
import streamlit as st
import joblib


# Load the model
model = joblib.load('Price_model.pkl')

# Set the title of the app
st.title("Boston House Price Prediction")


st.write("Adjust the features and click 'Predict'")

# Collect inputs with sliders or number inputs
inputs = {}
inputs['CRIM'] = st.number_input('CRIM (per capita crime rate)', min_value=0.0, max_value=100.0, value=0.1, step=0.01)
inputs['ZN'] = st.number_input('ZN (residential land zoned %)', min_value=0.0, max_value=100.0, value=18.0, step=0.1)
inputs['INDUS'] = st.number_input('INDUS (proportion non-retail business acres)', min_value=0.0, max_value=30.0, value=2.31, step=0.01)
inputs['CHAS'] = st.selectbox('CHAS (Charles River dummy variable)', options=[0, 1])
inputs['NOX'] = st.number_input('NOX (nitric oxides concentration)', min_value=0.3, max_value=1.0, value=0.54, step=0.01)
inputs['RM'] = st.number_input('RM (average rooms)', min_value=1.0, max_value=10.0, value=6.5, step=0.01)
inputs['AGE'] = st.number_input('AGE (proportion of owner-occupied units built before 1940)', min_value=0.0, max_value=100.0, value=65.0, step=0.1)
inputs['DIS'] = st.number_input('DIS (weighted distances)', min_value=1.0, max_value=15.0, value=4.0, step=0.01)
inputs['TAX'] = st.number_input('TAX (property tax rate)', min_value=100, max_value=800, value=300, step=1)
inputs['PTRATIO'] = st.number_input('PTRATIO (pupil-teacher ratio)', min_value=10.0, max_value=30.0, value=15.3, step=0.1)
inputs['B'] = st.number_input('B (proportion of blacks)', min_value=0.0, max_value=400.0, value=396.9, step=0.1)
inputs['LSTAT'] = st.number_input('LSTAT (% lower status population)', min_value=0.0, max_value=40.0, value=4.98, step=0.1)

# prepare inputs for pridection
input_df = pd.DataFrame([inputs])

# button to predict
if st.button("Predict"):
    prediction = model.predict(input_df)
    st.success(f"Predicted House Price : ${prediction[0]*1000:.2f}")
