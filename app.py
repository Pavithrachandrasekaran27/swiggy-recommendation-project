import streamlit as st
import pandas as pd
from recommendation_engine import recommend

df = pd.read_csv('cleaned_data.csv')

st.title("🍽️ Swiggy Restaurant Recommendation System")

st.sidebar.header("🔍 Your Preferences")
city = st.sidebar.selectbox("Select City", df['city'].unique())
cuisine = st.sidebar.text_input("Enter Cuisine (e.g., Chinese, Italian)")
rating = st.sidebar.slider("Minimum Rating", 1.0, 5.0, 3.5)
cost = st.sidebar.slider("Approximate Cost for Two", 100, 2000, 500, step=50)

if st.sidebar.button("Get Recommendations"):
    results = recommend(city, cuisine, rating, cost)
    st.subheader("Top Restaurant Recommendations")
    st.write(results[['name', 'rating', 'cost', 'cuisine', 'address']])