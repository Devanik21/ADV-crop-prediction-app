import streamlit as st
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Load the trained model
model = joblib.load("RF_crop recommendation.pkl")  # Replace with your actual model path

def user_input_features():
    features = {}
    for col in df.columns[:-1]:
        min_value = float(df[col].min())
        max_value = float(df[col].max())
        default_value = float(df[col].mean())
        
        features[col] = st.sidebar.slider(
            f"{col}",
            min_value=min_value,
            max_value=max_value,
            value=default_value,
            step=(max_value - min_value) / 100,
            key=col  # Assign the column name as the unique key
        )

    input_df = pd.DataFrame(features, index=[0])
    return input_df

def show_predict():
    st.markdown(
        """
        <div style="background-color: #2c3e50; padding: 20px; border-radius: 10px;">
            <h1 style="color: #f39c12; text-align: center; font-family: 'Arial Black', sans-serif;">
                🌾 Crop Recommendation Prediction 🌾
            </h1>
        </div>
        """, unsafe_allow_html=True
    )
    
    # Get user input
    input_df = user_input_features()

    # Display user input
    st.markdown(
        """
        <div style="background-color: #34495e; padding: 15px; border-radius: 10px; margin-top: 20px;">
            <h3 style="color: #ecf0f1; font-family: 'Arial', sans-serif;">User Input Features</h3>
        </div>
        """, unsafe_allow_html=True
    )
    st.write(input_df)

    # Make prediction
    prediction = model.predict(input_df)

    # Display the prediction result
    st.markdown(
        f"""
        <div style="background-color: #27ae60; padding: 15px; border-radius: 10px; margin-top: 20px;">
            <h2 style="color: #ffffff; font-family: 'Arial', sans-serif; text-align: center;">
                🌾 The recommended crop based on the input features is: <strong>{prediction[0]}</strong>
            </h2>
        </div>
        """, unsafe_allow_html=True
    )

    # Additional note
    st.markdown(
        """
        <div style="background-color: #ecf0f1; padding: 15px; border-radius: 10px; margin-top: 20px;">
            <strong>Note:</strong> The prediction is derived from an advanced analysis of key agricultural factors, 
            ensuring the best possible crop recommendation.
        </div>
        """, unsafe_allow_html=True
    )

# Call the function to display the prediction page
show_predict()
