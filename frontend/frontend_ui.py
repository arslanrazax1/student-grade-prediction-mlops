import streamlit as st
import requests
import pandas as pd
import os


API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

st.title("🎓Student Grade Prediction")

hours_studied = st.number_input("Hours Studied", 0, 10)

previous_scores = st.number_input("Previous Scores", 1, 100)

extracurricular = st.selectbox("Extracurricular Activities", ["Yes", "No"])

sleep_hours = st.number_input("Sleep Hours", 0, 10)

papers_practiced = st.number_input("Sample Question Papers Practiced", 0, 10)




if st.button("Predict"):
    data = {
        "Hours_Studied": hours_studied,
        "Previous_Scores": previous_scores,
        "Extracurricular_Activities": extracurricular,
        "Sleep_Hours": sleep_hours,
        "Sample_Question_Papers_Practiced": papers_practiced
    }
    response = requests.post(f"{API_URL}/predict",json=data)

    
    if response.status_code==201:
        result = response.json()
        # st.success(f"📊Grade: {result['Grade']}")   
        # st.markdown(f"📊Grade: {result['Grade']}")
        st.markdown(
        f"<h2 style='text-align: center; color: green;'>📊 Grade: <span style='color: white;'>{result['Grade']}</span></h2>",
        unsafe_allow_html=True
    )          
    else:
        st.error(f"❌ API Error: {response.status_code}")