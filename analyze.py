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
    feature = st.selectbox("Select a feature to visualize", numeric_columns)
    
    # Create a histogram for the selected feature
    fig, ax = plt.subplots()
    df[feature].hist(ax=ax, bins=20)
    ax.set_title(f'Distribution of {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    st.subheader("Correlation Matrix")
    numeric_df = df[numeric_columns]
    corr = numeric_df.corr()
    st.write(corr)
    
    # Create a heatmap for the correlation matrix
    fig, ax = plt.subplots()
    cax = ax.matshow(corr, cmap='coolwarm')
    fig.colorbar(cax)
    ax.set_xticks(range(len(numeric_columns)))
    ax.set_yticks(range(len(numeric_columns)))
    ax.set_xticklabels(numeric_columns, rotation=90)
    ax.set_yticklabels(numeric_columns)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    st.subheader("Heatmap")
    selected_columns = st.multiselect("Select columns for heatmap", numeric_columns, default=numeric_columns)
    
    if selected_columns:
        fig, ax = plt.subplots()
        sns.heatmap(df[selected_columns].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Heatmap of Selected Features')
        st.pyplot(fig)
