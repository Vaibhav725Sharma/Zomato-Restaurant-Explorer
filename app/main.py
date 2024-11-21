import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Restaurant Dashboard",
    layout="wide",
)

# Navigation
st.title("Welcome to the Restaurant Dashboard")
st.sidebar.title("Navigation")
pages = ["Home", "Insights", "Recommendations", "Reviews"]
selected_page = st.sidebar.radio("Go to", pages)

if selected_page == "Home":
    st.write("This is the home page of the Restaurant Dashboard.")
    st.write("Navigate through the sidebar to explore insights, recommendations, and reviews.")
