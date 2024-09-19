import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_visualization():
    st.title("Advanced Data Visualization")

    # Filter numeric columns for selection
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

    # 1. Heatmap with Annotations
    st.subheader("Heatmap with Annotations")
    heatmap_feature = st.multiselect("Select Features for Heatmap with Annotations", numeric_columns)
    if heatmap_feature:
        fig, ax = plt.subplots()
        sns.heatmap(df[heatmap_feature].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Heatmap with Annotations')
        st.pyplot(fig)

    # 2. Pair Grid
    st.subheader("Pair Grid")
    pairgrid_features = st.multiselect("Select Features for Pair Grid", numeric_columns)
    if pairgrid_features:
        g = sns.PairGrid(df[pairgrid_features])
        g.map_lower(sns.scatterplot)
        g.map_diag(sns.kdeplot)
        st.pyplot(g.fig)

    # 3. Regression Plot
    st.subheader("Regression Plot")
    reg_x = st.selectbox("Select X-axis for Regression Plot", numeric_columns)
    reg_y = st.selectbox("Select Y-axis for Regression Plot", numeric_columns)
    if reg_x and reg_y:
        fig, ax = plt.subplots()
        sns.regplot(x=df[reg_x], y=df[reg_y], ax=ax, color='blue')
        ax.set_title(f'Regression Plot: {reg_x} vs {reg_y}')
        st.pyplot(fig)

    # 4. Residual Plot
    st.subheader("Residual Plot")
    res_x = st.selectbox("Select X-axis for Residual Plot", numeric_columns)
    res_y = st.selectbox("Select Y-axis for Residual Plot", numeric_columns)
    if res_x and res_y:
        fig, ax = plt.subplots()
        sns.residplot(x=df[res_x], y=df[res_y], ax=ax, color='orange')
        ax.set_title(f'Residual Plot: {res_x} vs {res_y}')
        st.pyplot(fig)

    # 5. Joint Plot with KDE
    st.subheader("Joint Plot with KDE")
    joint_x = st.selectbox("Select X for Joint Plot with KDE", numeric_columns)
    joint_y = st.selectbox("Select Y for Joint Plot with KDE", numeric_columns)
    if joint_x and joint_y:
        fig = sns.jointplot(x=joint_x, y=joint_y, data=df, kind='kde', color='purple')
        st.pyplot(fig)

    # 6. Rug Plot with KDE Overlay
    st.subheader("Rug Plot with KDE Overlay")
    rug_feature = st.selectbox("Select Feature for Rug Plot with KDE", numeric_columns)
    if rug_feature:
        fig, ax = plt.subplots()
        sns.kdeplot(df[rug_feature], ax=ax, color='red', fill=True)
        sns.rugplot(df[rug_feature], ax=ax, color='blue')
        ax.set_title(f'Rug Plot with KDE Overlay of {rug_feature}')
        st.pyplot(fig)

    # 7. Hexbin Plot
    st.subheader("Hexbin Plot")
    hex_x = st.selectbox("Select X-axis for Hexbin Plot", numeric_columns)
    hex_y = st.selectbox("Select Y-axis for Hexbin Plot", numeric_columns)
    if hex_x and hex_y:
        fig, ax = plt.subplots()
        hb = ax.hexbin(df[hex_x], df[hex_y], gridsize=30, cmap='inferno')
        fig.colorbar(hb, ax=ax)
        ax.set_xlabel(hex_x)
        ax.set_ylabel(hex_y)
        ax.set_title(f'Hexbin Plot: {hex_x} vs {hex_y}')
        st.pyplot(fig)

    # 8. Andrews Curves
    st.subheader("Andrews Curves")
    if 'label' in df.columns:
        fig, ax = plt.subplots()
        pd.plotting.andrews_curves(df, 'label', ax=ax)
        ax.set_title('Andrews Curves')
        st.pyplot(fig)

    # 9. Lag Plot
    st.subheader("Lag Plot")
    lag_feature = st.selectbox("Select Feature for Lag Plot", numeric_columns)
    if lag_feature:
        fig = sns.lag_plot(df[lag_feature])
        st.pyplot(fig)

    # 10. Parallel Coordinates
    st.subheader("Parallel Coordinates")
    if 'label' in df.columns:
        fig, ax = plt.subplots()
        pd.plotting.parallel_coordinates(df, 'label', ax=ax)
        ax.set_title('Parallel Coordinates')
        st.pyplot(fig)

    # 11. Bubble Plot
    st.subheader("Bubble Plot")
    bubble_x = st.selectbox("Select X-axis for Bubble Plot", numeric_columns)
    bubble_y = st.selectbox("Select Y-axis for Bubble Plot", numeric_columns)
    bubble_size = st.selectbox("Select Size Feature for Bubble Plot", numeric_columns)
    if bubble_x and bubble_y and bubble_size:
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[bubble_x], y=df[bubble_y], size=df[bubble_size], hue=df['label'], ax=ax, palette='viridis', sizes=(20, 200))
        ax.set_xlabel(bubble_x)
        ax.set_ylabel(bubble_y)
        ax.set_title(f'Bubble Plot: {bubble_x} vs {bubble_y}')
        st.pyplot(fig)

    # 12. Heatmap of Feature Pair Correlations
    st.subheader("Heatmap of Feature Pair Correlations")
    feature_pair_heatmap = st.multiselect("Select Features for Pair Correlation Heatmap", numeric_columns)
    if feature_pair_heatmap:
        fig, ax = plt.subplots()
        sns.heatmap(df[feature_pair_heatmap].corr(), annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Heatmap of Feature Pair Correlations')
        st.pyplot(fig)

    # 13. Contour Plot
    st.subheader("Contour Plot")
    contour_x = st.selectbox("Select X-axis for Contour Plot", numeric_columns)
    contour_y = st.selectbox("Select Y-axis for Contour Plot", numeric_columns)
    if contour_x and contour_y:
        fig, ax = plt.subplots()
        sns.kdeplot(x=df[contour_x], y=df[contour_y], ax=ax, fill=True)
        ax.set_title(f'Contour Plot: {contour_x} vs {contour_y}')
        st.pyplot(fig)

    # 14. Density Plot with Multiple Features
    st.subheader("Density Plot with Multiple Features")
    density_features = st.multiselect("Select Features for Multi-density Plot", numeric_columns)
    if density_features:
        fig, ax = plt.subplots()
        for feature in density_features:
            sns.kdeplot(df[feature], ax=ax, label=feature)
        ax.legend()
        ax.set_title('Density Plot with Multiple Features')
        st.pyplot(fig)

    # 15. Custom Plot with Regression and Residual
    st.subheader("Custom Plot with Regression and Residual")
    custom_x = st.selectbox("Select X-axis for Custom Plot", numeric_columns)
    custom_y = st.selectbox("Select Y-axis for Custom Plot", numeric_columns)
    if custom_x and custom_y:
        fig, ax = plt.subplots()
        sns.regplot(x=df[custom_x], y=df[custom_y], ax=ax, color='blue', label='Regression')
        sns.residplot(x=df[custom_x], y=df[custom_y], ax=ax, color='red', label='Residual')
        ax.set_title(f'Custom Plot with Regression and Residual: {custom_x} vs {custom_y}')
        ax.legend()
        st.pyplot(fig)

    # 16. Facet Grid
    st.subheader("Facet Grid")
    facet_feature = st.selectbox("Select Feature for Facet Grid", numeric_columns)
    if facet_feature:
        g = sns.FacetGrid(df, col='label')
        g.map(sns.histplot, facet_feature)
        st.pyplot(g.fig)

    # 17. Matrix Plot
    st.subheader("Matrix Plot")
    matrix_features = st.multiselect("Select Features for Matrix Plot", numeric_columns)
    if matrix_features:
        fig, ax = plt.subplots()
        sns.plotting.matrix(df[matrix_features], ax=ax)
        ax.set_title('Matrix Plot')
        st.pyplot(fig)

    # 18. Cat Plot
    st.subheader("Cat Plot")
    cat_feature = st.selectbox("Select Feature for Cat Plot", numeric_columns)
    if cat_feature:
        fig, ax = plt.subplots()
        sns.catplot(x='label', y=cat_feature, kind='bar', data=df, ax=ax)
        ax.set_title(f'Cat Plot: {cat_feature} by Label')
        st.pyplot(fig)

    # 19. Time Series Plot
    st.subheader("Time Series Plot")
    if 'Date' in df.columns:
        time_series_feature = st.selectbox("Select Feature for Time Series Plot", numeric_columns)
        fig, ax = plt.subplots()
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date')[time_series_feature].plot(ax=ax)
        ax.set_title(f'Time Series Plot of {time_series_feature}')
        st.pyplot(fig)

    # 20. Bootstrap Plot
    st.subheader("Bootstrap Plot")
    bootstrap_feature = st.selectbox("Select Feature for Bootstrap Plot", numeric_columns)
    if bootstrap_feature:
        fig, ax = plt.subplots()
        sns.histplot(df[bootstrap_feature], kde=True, stat='density', linewidth=0, ax=ax)
        ax.set_title(f'Bootstrap Plot of {bootstrap_feature}')
        st.pyplot(fig)
