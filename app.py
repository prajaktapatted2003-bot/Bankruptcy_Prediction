import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model/rf_model.pkl", "rb"))

st.title("Bankruptcy Prediction System")

st.write("Enter financial risk indicators to predict whether a company is Bankrupt or Non-Bankrupt.")

# Input fields
industrial_risk = st.selectbox("Industrial Risk", [0,0.5,1])
management_risk = st.selectbox("Management Risk", [0,0.5,1])
financial_flexibility = st.selectbox("Financial Flexibility", [0,0.5,1])
credibility = st.selectbox("Credibility", [0,0.5,1])
competitiveness = st.selectbox("Competitiveness", [0,0.5,1])
operating_risk = st.selectbox("Operating Risk", [0,0.5,1])

# Prediction button
if st.button("Predict Bankruptcy"):

    input_data = np.array([[industrial_risk,
                            management_risk,
                            financial_flexibility,
                            credibility,
                            competitiveness,
                            operating_risk]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ The company is likely to go Bankrupt")
    else:
        st.success("✅ The company is Non-Bankrupt")