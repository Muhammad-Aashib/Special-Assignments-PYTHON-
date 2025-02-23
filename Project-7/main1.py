import streamlit as st
import pandas as pd 

st.title("BMI Calculator")

height = st.slider("Enter your Height (in cm) : ", 100 , 250 , 175)
weight = st.slider("Enter your Weight (in kg) : ", 40 , 200 , 70)

bmi = weight / ((height / 100) ** 2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("--- BMI CATEGORIES ---")
st.write("-Under Weight : BMI less than 18.5")
st.write("-Normal Weight : BMi between 18.5 and 24.9")
st.write("-Over Weight : BMi between 25 and 29")
st.write("-Obesity : BMi 30 or greater ")
