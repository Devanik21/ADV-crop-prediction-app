import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_comparison():
    st.title("Crop Comparison")
    
    st.subheader("Select Crops to Compare")
    crop1 = st.selectbox("Select Crop 1", df['label'].unique())
    crop2 = st.selectbox("Select Crop 2", df['label'].unique())

    st.subheader(f"Comparison of {crop1} and {crop2}")
    
    comparison_df = df[df['label'].isin([crop1, crop2])]
    
    st.write(comparison_df.describe())
    
    st.markdown(f"""
    - **{crop1}:** {crop1} is typically grown in conditions A, B, C.
    - **{crop2}:** {crop2} is better suited for conditions X, Y, Z.
    """)
