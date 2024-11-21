import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Import the necessary function after adding the path
from utils.recommend import get_recommendations

import streamlit as st

# Recommendations Page
st.title("Restaurant Recommendations")
st.write("Get personalized restaurant recommendations.")

# Input Section
user_input = st.text_input("Enter preferences or keywords for recommendation:")

if user_input:
    recommendations = get_recommendations(user_input)
    st.write("Here are some recommendations:")
    st.write(recommendations)
