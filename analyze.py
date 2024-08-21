import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_analyze():
    st.title("Data Analysis and Visualization")
    
    st.subheader("Dataset Overview")
    st.write(df.head())
    
    st.subheader("Feature Distributions")
    feature = st.selectbox("Select a feature to visualize", df.select_dtypes(include=['float64', 'int64']).columns)
    
    fig, ax = plt.subplots()
    df[feature].hist(ax=ax, bins=20)
    st.pyplot(fig)
    
    st.subheader("Correlation Matrix")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr = numeric_df.corr()
    st.write(corr)
    fig, ax = plt.subplots()
    cax = ax.matshow(corr, cmap='coolwarm')
    fig.colorbar(cax)
    st.pyplot(fig)
