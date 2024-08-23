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
    x_axis = st.selectbox("Select X-axis for Scatter Plot", numeric_columns)
    y_axis = st.selectbox("Select Y-axis for Scatter Plot", numeric_columns)
    
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], hue=df['label'], ax=ax)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f'Scatter Plot: {x_axis} vs {y_axis}')
    st.pyplot(fig)
    
    # Histogram Section
    st.subheader("Histogram")
    
    histogram_feature = st.selectbox("Select Feature for Histogram", numeric_columns)
    
    fig, ax = plt.subplots()
    df[histogram_feature].hist(ax=ax, bins=30, color='skyblue')
    ax.set_xlabel(histogram_feature)
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {histogram_feature}')
    st.pyplot(fig)
    
    # Box Plot Section
    st.subheader("Box Plot")
    
    box_feature = st.selectbox("Select Feature for Box Plot", numeric_columns)
    
    fig, ax = plt.subplots()
    sns.boxplot(x=df[box_feature], ax=ax, color='lightgreen')
    ax.set_xlabel(box_feature)
    ax.set_title(f'Box Plot of {box_feature}')
    st.pyplot(fig)
    
    # Pair Plot Section
    st.subheader("Pair Plot")
    
    pair_features = st.multiselect("Select Features for Pair Plot", options=numeric_columns, default=numeric_columns[:2])
    
    if len(pair_features) > 1:
        # Ensure the data does not contain missing values
        pair_df = df[pair_features].dropna()
        
        # Check if there are enough unique values for pairplot
        if pair_df.shape[1] > 1:
            fig = sns.pairplot(pair_df, hue=df['label'].loc[pair_df.index])
            st.pyplot(fig)
        else:
            st.warning("Please select at least two features with enough unique values for the pair plot.")
    else:
        st.warning("Please select at least two features for the pair plot.")
    
    # Line Plot Section
    st.subheader("Line Plot")
    
    line_feature = st.selectbox("Select Feature for Line Plot", numeric_columns)
    
    fig, ax = plt.subplots()
    df.sort_values(by=line_feature).plot(x=line_feature, y=line_feature, kind='line', ax=ax, color='orange')
    ax.set_xlabel(line_feature)
    ax.set_ylabel('Value')
    ax.set_title(f'Line Plot of {line_feature}')
    st.pyplot(fig)
    
    # Violin Plot Section
    st.subheader("Violin Plot")
    
    violin_feature = st.selectbox("Select Feature for Violin Plot", numeric_columns)
    
    fig, ax = plt.subplots()
    sns.violinplot(x=df['label'], y=df[violin_feature], ax=ax, palette='muted')
    ax.set_xlabel('Crop Label')
    ax.set_ylabel(violin_feature)
    ax.set_title(f'Violin Plot of {violin_feature} by Crop')
    st.pyplot(fig)
