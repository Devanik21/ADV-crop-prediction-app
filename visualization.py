import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_visualization():
    st.title("Advanced Data Visualization")
    
    st.subheader("Scatter Plot")
    
    # Filter numeric columns for selection
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Allow user to select only numeric columns for scatter plot
    x_axis = st.selectbox("Select X-axis", numeric_columns)
    y_axis = st.selectbox("Select Y-axis", numeric_columns)
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], hue=df['label'], ax=ax)
    st.pyplot(fig)
    
    st.subheader("Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df[numeric_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

