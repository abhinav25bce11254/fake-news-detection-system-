import streamlit as st
from src.prediction import load_model, predict

model, vectorizer = load_model()

st.title("📰 Fake News Detector")

user_input = st.text_area("Enter News Text:")

if st.button("Predict"):
    if user_input:
        result = predict(user_input, model, vectorizer)
        st.success(f"Prediction: {result}")
    else:
        st.warning("Please enter some text!")