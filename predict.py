import streamlit as st
import pandas as pd
import joblib

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Load the trained model
model = joblib.load("RF_crop recommendation.pkl")  # Replace with your actual model path

# Define colors for each crop
crop_colors = {
    "rice": "rgba(240, 255, 240, 0.2)",         # Honeydew
    "maize": "rgba(255, 228, 181, 0.2)",        # Moccasin
    "chickpea": "rgba(255, 239, 213, 0.2)",     # Papaya Whip
    "kidneybeans": "rgba(255, 182, 193, 0.2)",  # Light Pink
    "pigeonpeas": "rgba(255, 248, 220, 0.2)",   # Cornsilk
    "mothbeans": "rgba(230, 230, 250, 0.2)",    # Lavender
    "mungbean": "rgba(152, 251, 152, 0.2)",     # Pale Green
    "blackgram": "rgba(176, 224, 230, 0.2)",    # Powder Blue
    "lentil": "rgba(255, 228, 196, 0.2)",       # Bisque
    "pomegranate": "rgba(255, 160, 122, 0.2)",  # Light Salmon
    "banana": "rgba(255, 250, 205, 0.2)",       # Lemon Chiffon
    "mango": "rgba(255, 218, 185, 0.2)",        # Peach Puff
    "grapes": "rgba(216, 191, 216, 0.2)",       # Thistle
    "watermelon": "rgba(240, 128, 128, 0.2)",   # Light Coral
    "muskmelon": "rgba(255, 222, 173, 0.2)",    # Navajo White
    "apple": "rgba(250, 128, 114, 0.2)",        # Salmon
    "orange": "rgba(255, 165, 0, 0.2)",         # Orange
    "papaya": "rgba(144, 238, 144, 0.2)",       # Light Green
    "coconut": "rgba(245, 222, 179, 0.2)",      # Wheat
    "cotton": "rgba(255, 228, 225, 0.2)",       # Misty Rose
    "jute": "rgba(210, 180, 140, 0.2)",         # Tan
    "coffee": "rgba(139, 69, 19, 0.2)",         # Saddle Brown
}


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
    prediction = model.predict(input_df)[0]

    # Determine background color based on crop
    bg_color = crop_colors.get(prediction, "rgba(255, 255, 255, 0.5)")  # Default to light transparent white

    # Display the prediction result
    st.markdown(
        f"""
        <div style="background-color: {bg_color}; padding: 20px; border-radius: 10px;">
            <h2 style="color: #95dff5; text-align: center;">
                🌾 The recommended crop based on the input features is: <strong>{prediction}</strong>
            </h2>
        </div>
        """, unsafe_allow_html=True
    )

    # Optional note
    st.markdown("""
    <div style="margin-top: 20px; padding: 10px; border: 1px solid #ddd; border-radius: 5px;">
        <strong>Note:</strong> The prediction is based on the model's analysis of key agricultural factors.
    </div>
    """, unsafe_allow_html=True)

# Call the function to display the prediction page
show_predict()
