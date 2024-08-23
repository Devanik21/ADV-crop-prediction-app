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
        
        features[col] = st.sidebar.slider(f"{col}", min_value, max_value, default_value)

    input_df = pd.DataFrame(features, index=[0])
    return input_df

def show_predict():
    st.title("Crop Recommendation Prediction")
    
    # Get user input
    input_df = user_input_features()

    # Display user input
    st.subheader('User Input Features')
    st.write(input_df)

    # Make prediction
    prediction = model.predict(input_df)

    # Display the prediction result
    st.subheader('Prediction Result')
    st.success(f"🌾 The recommended crop based on the input features is: **{prediction[0]}**")

    # Optionally, you can add more details or a description below the result
    st.markdown("""
    <div style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
        <strong>Note:</strong> The prediction is based on the model's analysis of key agricultural factors.
    </div>
    """, unsafe_allow_html=True)
