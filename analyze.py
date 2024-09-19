import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

# Filter numeric columns for selection
numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

def show_analyze():
    st.title("Data Analysis and Visualization")

    st.subheader("Dataset Overview")
    st.write(df.head())

    # User selects columns for analysis
    st.subheader("Select Columns for Cleaning")
    selected_columns = st.multiselect("Select Columns to Include in Cleaned Data:", df.columns)
    if selected_columns:
        cleaned_df = df[selected_columns].dropna()
        st.write(cleaned_df.head())

        # Allow the user to download the cleaned CSV
        csv_buffer = io.StringIO()
        cleaned_df.to_csv(csv_buffer, index=False)
        st.download_button(label="Download Cleaned Data as CSV", data=csv_buffer.getvalue(), file_name="cleaned_crop_data.csv", mime="text/csv")

    # Feature Distributions
    st.subheader("Feature Distributions")
    feature = st.selectbox("Select a feature to visualize", numeric_columns)
    if feature:
        # Create a histogram for the selected feature
        fig, ax = plt.subplots()
        df[feature].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
        ax.set_title(f'Distribution of {feature}')
        ax.set_xlabel(feature)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

    # Correlation Matrix
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

    # More advanced analysis
    st.subheader("More Advanced Analysis")

    # 1. Box Plot
    box_feature = st.selectbox("Select a feature for box plot", numeric_columns)
    if box_feature:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[box_feature], ax=ax, color='lightblue')
        ax.set_title(f'Box Plot of {box_feature}')
        st.pyplot(fig)

    # 2. Scatter Plot
    x_axis = st.selectbox("Select X-axis feature for scatter plot", numeric_columns)
    y_axis = st.selectbox("Select Y-axis feature for scatter plot", numeric_columns)
    if x_axis and y_axis:
        fig, ax = plt.subplots()
        ax.scatter(df[x_axis], df[y_axis], alpha=0.5, color='#417f85')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f'Scatter Plot of {x_axis} vs {y_axis}')
        st.pyplot(fig)

    # 3. KDE Plot
    kde_feature = st.selectbox("Select a feature for KDE plot", numeric_columns)
    if kde_feature:
        fig, ax = plt.subplots()
        sns.kdeplot(df[kde_feature], ax=ax, fill=True, color='purple')
        ax.set_title(f'KDE Plot of {kde_feature}')
        ax.set_xlabel(kde_feature)
        ax.set_ylabel('Density')
        st.pyplot(fig)

    # 4. Heatmap of Feature Distributions
    st.subheader("Heatmap of Feature Distributions")
    heatmap_feature = st.multiselect("Select features for heatmap (numeric only)", numeric_columns)
    if heatmap_feature:
        fig, ax = plt.subplots()
        sns.heatmap(df[heatmap_feature].corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
        ax.set_title(f'Heatmap of Selected Features')
        st.pyplot(fig)

    # 5. Violin Plot
    violin_feature = st.selectbox("Select a feature for Violin plot", numeric_columns)
    if violin_feature:
        fig, ax = plt.subplots()
        sns.violinplot(x=df[violin_feature], ax=ax, color='orange')
        ax.set_title(f'Violin Plot of {violin_feature}')
        st.pyplot(fig)

    # 6. Histogram with Density Plot Overlay
    hist_feature = st.selectbox("Select a feature for Histogram with Density Overlay", numeric_columns)
    if hist_feature:
        fig, ax = plt.subplots()
        sns.histplot(df[hist_feature], kde=True, ax=ax, color='steelblue')
        ax.set_title(f'Histogram with Density Plot of {hist_feature}')
        ax.set_xlabel(hist_feature)
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

    # 7. Pair Plot
    st.subheader("Pair Plot of Selected Features")
    selected_pairplot_features = st.multiselect("Select features for pair plot", numeric_columns)
    if selected_pairplot_features:
        fig = sns.pairplot(df[selected_pairplot_features])
        st.pyplot(fig)

    # 8. Joint Plot
    joint_x = st.selectbox("Select X for Joint Plot", numeric_columns)
    joint_y = st.selectbox("Select Y for Joint Plot", numeric_columns, index=1)
    if joint_x and joint_y:
        fig = sns.jointplot(x=joint_x, y=joint_y, data=df, kind="scatter", color='green')
        st.pyplot(fig)

    # 9. Line Plot
    line_feature = st.selectbox("Select a feature for Line plot", numeric_columns)
    if line_feature:
        fig, ax = plt.subplots()
        df[line_feature].plot(ax=ax, color='red')
        ax.set_title(f'Line Plot of {line_feature}')
        ax.set_xlabel('Index')
        ax.set_ylabel(line_feature)
        st.pyplot(fig)

    # 10. Swarm Plot
    swarm_feature = st.selectbox("Select a feature for Swarm plot", numeric_columns)
    if swarm_feature:
        fig, ax = plt.subplots()
        sns.swarmplot(x=df[swarm_feature], ax=ax, color='blue')
        ax.set_title(f'Swarm Plot of {swarm_feature}')
        st.pyplot(fig)

    # 11. Strip Plot
    strip_feature = st.selectbox("Select a feature for Strip plot", numeric_columns)
    if strip_feature:
        fig, ax = plt.subplots()
        sns.stripplot(x=df[strip_feature], ax=ax, color='brown')
        ax.set_title(f'Strip Plot of {strip_feature}')
        st.pyplot(fig)

    # 12. Bar Plot
    bar_feature = st.selectbox("Select a feature for Bar plot", numeric_columns)
    if bar_feature:
        fig, ax = plt.subplots()
        df[bar_feature].value_counts().plot(kind='bar', ax=ax, color='blue')
        ax.set_title(f'Bar Plot of {bar_feature}')
        st.pyplot(fig)

    # 13. Rug Plot
    rug_feature = st.selectbox("Select a feature for Rug plot", numeric_columns)
    if rug_feature:
        fig, ax = plt.subplots()
        sns.rugplot(x=df[rug_feature], ax=ax, color='green')
        ax.set_title(f'Rug Plot of {rug_feature}')
        st.pyplot(fig)

    # 14. Point Plot
    point_feature = st.selectbox("Select a feature for Point plot", numeric_columns)
    if point_feature:
        fig, ax = plt.subplots()
        sns.pointplot(x=df.index, y=point_feature, data=df, ax=ax, color='purple')
        ax.set_title(f'Point Plot of {point_feature}')
        st.pyplot(fig)

    # 15. Density Plot
    density_feature = st.selectbox("Select a feature for Density plot", numeric_columns)
    if density_feature:
        fig, ax = plt.subplots()
        sns.kdeplot(df[density_feature], ax=ax, color='cyan')
        ax.set_title(f'Density Plot of {density_feature}')
        st.pyplot(fig)

    # 16. Count Plot
    count_feature = st.selectbox("Select a feature for Count plot", numeric_columns)
    if count_feature:
        fig, ax = plt.subplots()
        sns.countplot(x=df[count_feature], ax=ax, palette='pastel')
        ax.set_title(f'Count Plot of {count_feature}')
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
