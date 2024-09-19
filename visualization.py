import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import lag_plot

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_visualization():
    st.title("Advanced Data Visualization")

    # Sample 100 rows from the dataset
    df_sample = df.sample(n=100, random_state=1)

    # Filter numeric columns for selection
    numeric_columns = df_sample.select_dtypes(include=['float64', 'int64']).columns

    # 1. Heatmap with Annotations
    st.subheader("Heatmap with Annotations")
    heatmap_feature = st.multiselect("Select Features for Heatmap with Annotations", numeric_columns)
    if heatmap_feature:
        fig, ax = plt.subplots()
        sns.heatmap(df_sample[heatmap_feature].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Heatmap with Annotations')
        st.pyplot(fig)

    # 2. Pair Grid
    st.subheader("Pair Grid")
    pairgrid_features = st.multiselect("Select Features for Pair Grid", numeric_columns)
    if pairgrid_features:
        g = sns.PairGrid(df_sample[pairgrid_features])
        g.map_lower(sns.scatterplot)
        g.map_diag(sns.kdeplot)
        st.pyplot(g.fig)

    # 3. Regression Plot
    st.subheader("Regression Plot")
    reg_x = st.selectbox("Select X-axis for Regression Plot", numeric_columns)
    reg_y = st.selectbox("Select Y-axis for Regression Plot", numeric_columns)
    if reg_x and reg_y:
        fig, ax = plt.subplots()
        sns.regplot(x=df_sample[reg_x], y=df_sample[reg_y], ax=ax, color='blue')
        ax.set_title(f'Regression Plot: {reg_x} vs {reg_y}')
        st.pyplot(fig)

    # 4. Residual Plot
    st.subheader("Residual Plot")
    res_x = st.selectbox("Select X-axis for Residual Plot", numeric_columns)
    res_y = st.selectbox("Select Y-axis for Residual Plot", numeric_columns)
    if res_x and res_y:
        fig, ax = plt.subplots()
        sns.residplot(x=df_sample[res_x], y=df_sample[res_y], ax=ax, color='orange')
        ax.set_title(f'Residual Plot: {res_x} vs {res_y}')
        st.pyplot(fig)

    # 5. Joint Plot with KDE
    st.subheader("Joint Plot with KDE")
    joint_x = st.selectbox("Select X for Joint Plot with KDE", numeric_columns)
    joint_y = st.selectbox("Select Y for Joint Plot with KDE", numeric_columns)
    if joint_x and joint_y:
        fig = sns.jointplot(x=joint_x, y=joint_y, data=df_sample, kind='kde', color='purple')
        st.pyplot(fig)

    # 6. Rug Plot with KDE Overlay
    st.subheader("Rug Plot with KDE Overlay")
    rug_feature = st.selectbox("Select Feature for Rug Plot with KDE", numeric_columns)
    if rug_feature:
        fig, ax = plt.subplots()
        sns.kdeplot(df_sample[rug_feature], ax=ax, color='red', fill=True)
        sns.rugplot(df_sample[rug_feature], ax=ax, color='blue')
        ax.set_title(f'Rug Plot with KDE Overlay of {rug_feature}')
        st.pyplot(fig)

    # 7. Hexbin Plot
    st.subheader("Hexbin Plot")
    hex_x = st.selectbox("Select X-axis for Hexbin Plot", numeric_columns)
    hex_y = st.selectbox("Select Y-axis for Hexbin Plot", numeric_columns)
    if hex_x and hex_y:
        fig, ax = plt.subplots()
        hb = ax.hexbin(df_sample[hex_x], df_sample[hex_y], gridsize=30, cmap='inferno')
        fig.colorbar(hb, ax=ax)
        ax.set_xlabel(hex_x)
        ax.set_ylabel(hex_y)
        ax.set_title(f'Hexbin Plot: {hex_x} vs {hex_y}')
        st.pyplot(fig)

    # 8. Andrews Curves
    st.subheader("Andrews Curves")
    if 'label' in df_sample.columns:
        fig, ax = plt.subplots()
        pd.plotting.andrews_curves(df_sample, 'label', ax=ax)
        ax.set_title('Andrews Curves')
        st.pyplot(fig)

    # 9. Lag Plot
    st.subheader("Lag Plot")
    lag_feature = st.selectbox("Select Feature for Lag Plot", numeric_columns)
    if lag_feature:
        fig, ax = plt.subplots()
        lag_plot(df_sample[lag_feature], ax=ax)
        ax.set_title(f'Lag Plot of {lag_feature}')
        st.pyplot(fig)

    # 10. Parallel Coordinates
    st.subheader("Parallel Coordinates")
    if 'label' in df_sample.columns:
        fig, ax = plt.subplots()
        pd.plotting.parallel_coordinates(df_sample, 'label', ax=ax)
        ax.set_title('Parallel Coordinates')
        st.pyplot(fig)

    # 11. Bubble Plot
    st.subheader("Bubble Plot")
    bubble_x = st.selectbox("Select X-axis for Bubble Plot", numeric_columns)
    bubble_y = st.selectbox("Select Y-axis for Bubble Plot", numeric_columns)
    bubble_size = st.selectbox("Select Size Feature for Bubble Plot", numeric_columns)
    if bubble_x and bubble_y and bubble_size:
        fig, ax = plt.subplots()
        sns.scatterplot(x=df_sample[bubble_x], y=df_sample[bubble_y], size=df_sample[bubble_size], hue=df_sample['label'], ax=ax, palette='viridis', sizes=(20, 200))
        ax.set_xlabel(bubble_x)
        ax.set_ylabel(bubble_y)
        ax.set_title(f'Bubble Plot: {bubble_x} vs {bubble_y}')
        st.pyplot(fig)

    # 12. Heatmap of Feature Pair Correlations
    st.subheader("Heatmap of Feature Pair Correlations")
    feature_pair_heatmap = st.multiselect("Select Features for Pair Correlation Heatmap", numeric_columns)
    if feature_pair_heatmap:
        fig, ax = plt.subplots()
        sns.heatmap(df_sample[feature_pair_heatmap].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Heatmap of Feature Pair Correlations')
        st.pyplot(fig)

    # 13. Contour Plot
    st.subheader("Contour Plot")
    contour_x = st.selectbox("Select X-axis for Contour Plot", numeric_columns)
    contour_y = st.selectbox("Select Y-axis for Contour Plot", numeric_columns)
    if contour_x and contour_y:
        fig, ax = plt.subplots()
        sns.kdeplot(x=df_sample[contour_x], y=df_sample[contour_y], ax=ax, fill=True)
        ax.set_title(f'Contour Plot: {contour_x} vs {contour_y}')
        st.pyplot(fig)

    # 14. Density Plot with Multiple Features
    st.subheader("Density Plot with Multiple Features")
    density_features = st.multiselect("Select Features for Multi-density Plot", numeric_columns)
    if density_features:
        fig, ax = plt.subplots()
        for feature in density_features:
            sns.kdeplot(df_sample[feature], ax=ax, label=feature)
        ax.legend()
        ax.set_title('Density Plot with Multiple Features')
        st.pyplot(fig)

    # 15. Custom Plot with Regression and Residual
    st.subheader("Custom Plot with Regression and Residual")
    custom_x = st.selectbox("Select X-axis for Custom Plot", numeric_columns)
    custom_y = st.selectbox("Select Y-axis for Custom Plot", numeric_columns)
    if custom_x and custom_y:
        fig, ax = plt.subplots()
        sns.regplot(x=df_sample[custom_x], y=df_sample[custom_y], ax=ax, color='blue', label='Regression')
        sns.residplot(x=df_sample[custom_x], y=df_sample[custom_y], ax=ax, color='red', label='Residual')
        ax.set_title(f'Custom Plot with Regression and Residual: {custom_x} vs {custom_y}')
        ax.legend()
        st.pyplot(fig)

    # 16. Facet Grid
    st.subheader("Facet Grid")
    facet_feature = st.selectbox("Select Feature for Facet Grid", numeric_columns)
    if facet_feature:
        g = sns.FacetGrid(df_sample, col='label', height=4, aspect=2)
        g.map(sns.histplot, facet_feature)
        st.pyplot(g.fig)

    # 17. Matrix Plot
    st.subheader("Matrix Plot")
    matrix_features = st.multiselect("Select Features for Matrix Plot", numeric_columns)
    if matrix_features:
        pairplot_fig = sns.pairplot(df_sample[matrix_features])
        pairplot_fig.fig.set_size_inches(12, 8)
        pairplot_fig.fig.suptitle('Matrix Plot', y=1.02)
        st.pyplot(pairplot_fig.fig)

    # 18. Cat Plot
    st.subheader("Cat Plot")
    cat_feature = st.selectbox("Select Feature for Cat Plot", numeric_columns)
    if cat_feature:
        fig, ax = plt.subplots()
        sns.catplot(x=cat_feature, kind='count', data=df_sample, ax=ax)
        ax.set_title(f'Cat Plot of {cat_feature}')
        st.pyplot(fig)

    # 19. Violin Plot
    st.subheader("Violin Plot")
    violin_x = st.selectbox("Select X-axis for Violin Plot", numeric_columns)
    violin_y = st.selectbox("Select Y-axis for Violin Plot", numeric_columns)
    if violin_x and violin_y:
        fig, ax = plt.subplots()
        sns.violinplot(x=df_sample[violin_x], y=df_sample[violin_y], ax=ax)
        ax.set_title(f'Violin Plot: {violin_x} vs {violin_y}')
        st.pyplot(fig)

    # 20. Box Plot
    st.subheader("Box Plot")
    box_x = st.selectbox("Select X-axis for Box Plot", numeric_columns)
    box_y = st.selectbox("Select Y-axis for Box Plot", numeric_columns)
    if box_x and box_y:
        fig, ax = plt.subplots()
        sns.boxplot(x=df_sample[box_x], y=df_sample[box_y], ax=ax)
        ax.set_title(f'Box Plot: {box_x} vs {box_y}')
        st.pyplot(fig)

if __name__ == "__main__":
    show_visualization()
