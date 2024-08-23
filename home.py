import streamlit as st

def show_home():
    st.markdown(
        """
        <div style="background-color: #1c1c1c; padding: 30px; border-radius: 15px;">
            <h1 style="color: #f39c12; text-align: center; font-family: 'Arial Black', sans-serif;">
                🌾 Welcome to the Crop Recommendation System 🌾
            </h1>
            <p style="font-size: 20px; color: #ecf0f1; text-align: center; line-height: 1.6; font-family: 'Verdana', sans-serif;">
                Empowering farmers and agriculturists with intelligent crop predictions and insights to boost productivity and sustainability.
            </p>
            <div style="margin-top: 30px; text-align: center;">
                <h3 style="color: #27ae60; font-family: 'Arial', sans-serif;">🎯 Key Features:</h3>
                <ul style="list-style-type: none; padding-left: 0; font-size: 18px; color: #bdc3c7; text-align: left; font-family: 'Verdana', sans-serif;">
                    <li style="margin-bottom: 10px;">
                        <span style="color: #e74c3c; font-weight: bold;">🔍 Predict:</span> 
                        Receive tailored crop recommendations based on your specific inputs.
                    </li>
                    <li style="margin-bottom: 10px;">
                        <span style="color: #3498db; font-weight: bold;">📊 Analyze:</span> 
                        Delve into data visualizations to uncover patterns and trends.
                    </li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True
    )
