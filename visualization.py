import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_visualization():
    st.title("Advanced Data Visualization")
    
    st.subheader("Scatter Plot")
    x_axis = st.selectbox("Select X-axis", df.columns[:-1])
    y_axis = st.selectbox("Select Y-axis", df.columns[:-1])
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], hue=df['label'], ax=ax)
    st.pyplot(fig)
    
    st.subheader("Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)
