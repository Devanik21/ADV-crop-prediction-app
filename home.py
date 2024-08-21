import streamlit as st

def show_home():
    st.markdown(
        """
        <div style="background-color: #f0f0f0; padding: 20px; border-radius: 10px;">
            <h1 style="color: #FF5733; text-align: center;">🌾 Welcome to the Crop Recommendation System 🌾</h1>
            <p style="font-size: 18px; color: #4A4A4A;">
                This web app is designed to assist farmers and agriculturists in predicting the most suitable crop based on various input features. 
            </p>
            <h3 style="color: #008080;">🎯 Key Features:</h3>
            <ul style="font-size: 18px; color: #333333;">
                <li><span style="color: #FF6347;">🔍 <strong>Predict:</strong></span> Get crop recommendations based on input features.</li>
                <li><span style="color: #4682B4;">📊 <strong>Analyze:</strong></span> Visualize data and understand patterns.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True
    )

# Call this function in the main app script where you handle the home page
