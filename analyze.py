import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Filter numeric columns for selection
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

def show_analyze():
    st.title("Data Analysis and Visualization")
    
    st.subheader("Dataset Overview")
    st.write(df.head())
    
    st.subheader("Feature Distributions")
    selected_feature = st.selectbox("Select a feature to visualize", numeric_columns)
    
    fig, ax = plt.subplots()
    ax.hist(df[selected_feature], bins=20, color='#00A86B', edgecolor='black')
    ax.set_title(f'Distribution of {selected_feature}', fontsize=16)
    ax.set_xlabel(selected_feature, fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    st.pyplot(fig)
    
    st.subheader("Correlation Matrix")
    selected_columns = st.multiselect("Select columns to include in the correlation matrix", numeric_columns, default=numeric_columns)
    if selected_columns:
        corr = df[selected_columns].corr()
        fig, ax = plt.subplots()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax, linewidths=0.5)
        ax.set_title('Correlation Matrix', fontsize=16)
        st.pyplot(fig)
    
    st.subheader("Heatmap")
    if selected_columns:
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(df[selected_columns].corr(), annot=True, cmap='coolwarm', ax=ax, linewidths=0.5)
        ax.set_title('Heatmap of Selected Features', fontsize=16)
        st.pyplot(fig)

# To display the analysis page
show_analyze()
