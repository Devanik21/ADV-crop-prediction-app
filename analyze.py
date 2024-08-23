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
    df[feature].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
    ax.set_title(f'Distribution of {feature}')
    ax.set_xlabel(feature)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    st.subheader("Correlation Matrix")
    numeric_df = df[numeric_columns]
    corr = numeric_df.corr()
    st.write(corr)
    
    # Create a correlation matrix plot
    fig, ax = plt.subplots()
    cax = ax.matshow(corr, cmap='coolwarm')
    fig.colorbar(cax)
    ax.set_xticks(range(len(numeric_columns)))
    ax.set_yticks(range(len(numeric_columns)))
    ax.set_xticklabels(numeric_columns, rotation=90)
    ax.set_yticklabels(numeric_columns)
    ax.set_title('Correlation Matrix')
    st.pyplot(fig)

    st.subheader("More Advanced Analysis")

    # Box Plot
    box_feature = st.selectbox("Select a feature for box plot", numeric_columns)
    fig, ax = plt.subplots()
    sns.boxplot(x=df[box_feature], ax=ax, color='lightblue')
    ax.set_title(f'Box Plot of {box_feature}')
    st.pyplot(fig)

    # Scatter Plot
    x_axis = st.selectbox("Select X-axis feature for scatter plot", numeric_columns)
    y_axis = st.selectbox("Select Y-axis feature for scatter plot", numeric_columns)
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis], alpha=0.5, color='coral')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'Scatter Plot of {x_axis} vs {y_axis}')
        st.pyplot(fig)

    # KDE Plot
    kde_feature = st.selectbox("Select a feature for KDE plot", numeric_columns)
    fig, ax = plt.subplots()
    sns.kdeplot(df[kde_feature], ax=ax, fill=True, color='purple')
    ax.set_title(f'KDE Plot of {kde_feature}')
    ax.set_xlabel(kde_feature)
    ax.set_ylabel('Density')
    st.pyplot(fig)

    # Heatmap of Feature Distributions
    st.subheader("Heatmap of Feature Distributions")
    feature_heatmap = st.selectbox("Select features for heatmap", numeric_columns, key="heatmap_selectbox", index=0)
    fig, ax = plt.subplots()
    sns.heatmap(df[[feature_heatmap]].apply(pd.Series.value_counts).fillna(0), annot=True, fmt="d", cmap='YlGnBu', ax=ax)
    ax.set_title(f'Heatmap of {feature_heatmap}')
    st.pyplot(fig)

    # Violin Plot
    violin_feature = st.selectbox("Select a feature for Violin plot", numeric_columns)
    fig, ax = plt.subplots()
    sns.violinplot(x=df[violin_feature], ax=ax, color='orange')
    ax.set_title(f'Violin Plot of {violin_feature}')
    st.pyplot(fig)

    # Histogram with Density Plot Overlay
    hist_feature = st.selectbox("Select a feature for Histogram with Density Overlay", numeric_columns)
    fig, ax = plt.subplots()
    sns.histplot(df[hist_feature], kde=True, ax=ax, color='steelblue')
    ax.set_title(f'Histogram with Density Plot of {hist_feature}')
    ax.set_xlabel(hist_feature)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    # Customizing plot appearance
    st.markdown("""
    <style>
    .main .block-container {
        background-color: #000000;
        color: #FFFFFF;
    }
    .css-18e3th9 { font-family: 'Arial', sans-serif; }
    .css-1v0mbdj { color: #1f77b4; }
    </style>
    """, unsafe_allow_html=True)
