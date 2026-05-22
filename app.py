import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("YouTube Ad Revenue Predictor")

views = st.number_input("Views", min_value=0)
likes = st.number_input("Likes", min_value=0)
comments = st.number_input("Comments", min_value=0)

watch_time_minutes = st.number_input("Watch Time (minutes)", min_value=0.0)
video_length_minutes = st.number_input("Video Length (minutes)", min_value=0.0)

subscribers = st.number_input("Subscribers", min_value=0)

category = st.number_input("Category (encoded)", min_value=0)
device = st.number_input("Device (encoded)", min_value=0)
country = st.number_input("Country (encoded)", min_value=0)

features = np.array([[
    views,
    likes,
    comments,
    watch_time_minutes,
    video_length_minutes,
    subscribers,
    category,
    device,
    country
]])

features = scaler.transform(features)

if st.button("Predict Revenue"):
    prediction = model.predict(features)
    st.success(f"Predicted Revenue: ${prediction[0]:.2f}")

