"""
Created on TUS July 23 23:36:29 2026

@author: Pooja
"""

import streamlit as st
import pickle
import numpy as np

# Load the trained model
try:
    with open(r"Salary_prediction_model.pkl", "rb") as model_file:
        model = pickle.load(model_file)

except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Title and description
st.title("💰 Salary Prediction App")
st.subheader("🔎 Estimate your expected salary based on experience, job_title, and education level.")
st.write("Provide the details below to estimate the expected salary.")

# Input fields
age = st.number_input("🧑 Age", min_value=18, max_value=70, step=1)

gender = st.selectbox("⚤ Gender", options=["Male", "Female", "Other"])

education_level = st.selectbox(
    "🎓 Education Level",
    options=["High School", "Bachelor's", "Master's", "PhD"]
)

job_title = st.selectbox(
    "💼 Job Title",
    options=[
        "Junior Developer", "Software Engineer", "Senior Developer", "Manager",
        "Director", "Data Analyst", "Product Manager", "Sales Manager", "HR Manager",
        "Financial Analyst", "Project Manager", "Marketing Manager", "Data Scientist",
        "Operations Manager", "Senior Software Engineer", "Chief Technology Officer"
    ]
)

years_of_experience = st.number_input(
    "📆 Years of Experience", min_value=0.0, max_value=50.0, step=0.1
)

# Map categorical inputs to numerical values
gender_mapping = {"Male": 0, "Female": 1, "Other": 2}
education_mapping = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
job_title_mapping = {
    "Junior Developer": 1, "Software Engineer": 2, "Senior Developer": 3,
    "Data Analyst": 4, "Product Manager": 5, "Sales Manager": 6, "Marketing Manager": 7,
    "HR Manager": 8, "Financial Analyst": 9, "Project Manager": 10, "Operations Manager": 11,
    "Manager": 12, "Senior Software Engineer": 13, "Director": 14, "Chief Technology Officer": 15
}

# Convert inputs
gender_num = gender_mapping.get(gender, 0)
education_num = education_mapping.get(education_level, 0)
job_title_num = job_title_mapping.get(job_title, 0)

# Predict salary
if st.button("🔍 Predict Salary"):
    try:
        # Combine inputs into a single array
        features = np.array([[age, gender_num, education_num, job_title_num, years_of_experience]])
        
        # Predict using the model
        predicted_salary = model.predict(features)
        
        # Display the prediction
        st.success(f"💵 The estimated salary is: **₹{predicted_salary[0]:,.2f}**")
    
    except Exception as e:
        st.error(f"Prediction error: {e}")
