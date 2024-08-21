import streamlit as st

def show_home():
    st.title("Welcome to the Crop Recommendation System")
    st.markdown("""
    This web app helps farmers and agriculturists to predict the best crop based on input features.
    
    ### Features:
    - **Predict:** Get recommendations based on input features.
    - **Analyze:** Visualize data and understand patterns.
    """)
