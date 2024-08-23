import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_visualization():
    st.title("Advanced Data Visualization")

    # Scatter Plot Section
    st.subheader("Scatter Plot")
    
    # Filter numeric columns for selection
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Allow user to select numeric columns for scatter plot
    x_axis = st.selectbox("Select X-axis", numeric_columns)
    y_axis = st.selectbox("Select Y-axis", numeric_columns)
    
    # Option to choose point size and color palette
    point_size = st.slider("Select Point Size", min_value=5, max_value=100, value=30)
    color_palette = st.selectbox("Select Color Palette", ['viridis', 'plasma', 'inferno', 'magma', 'cividis'])

    # Create scatter plot
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], hue=df['label'], ax=ax, s=point_size, palette=color_palette)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f'Scatter Plot: {x_axis} vs {y_axis}')
    st.pyplot(fig)
    
    # Heatmap Section
    st.subheader("Heatmap")
    
    # Option to select subset of features for the heatmap
    feature_subset = st.multiselect("Select Features for Heatmap", options=numeric_columns, default=numeric_columns)
    
    if feature_subset:
        fig, ax = plt.subplots()
        sns.heatmap(df[feature_subset].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Correlation Heatmap')
        st.pyplot(fig)
    else:
        st.warning("Please select at least one feature to display the heatmap.")
