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

    # 1. Pairplot
    st.subheader("Pair Plot")
    selected_pairplot_features = st.multiselect("Select features for Pair Plot", numeric_columns)
    if selected_pairplot_features:
        fig = sns.pairplot(df[selected_pairplot_features])
        st.pyplot(fig)

    # 2. Joint Plot
    st.subheader("Joint Plot")
    joint_x = st.selectbox("Select X for Joint Plot", numeric_columns)
    joint_y = st.selectbox("Select Y for Joint Plot", numeric_columns, index=1)
    if joint_x and joint_y:
        fig = sns.jointplot(x=joint_x, y=joint_y, data=df, kind="hex", color='blue')
        st.pyplot(fig)

    # 3. Hexbin Plot
    st.subheader("Hexbin Plot")
    hex_x = st.selectbox("Select X for Hexbin Plot", numeric_columns)
    hex_y = st.selectbox("Select Y for Hexbin Plot", numeric_columns, index=1)
    if hex_x and hex_y:
        fig, ax = plt.subplots()
        hb = ax.hexbin(df[hex_x], df[hex_y], gridsize=50, cmap='Blues')
        cb = plt.colorbar(hb, ax=ax)
        cb.set_label('Counts')
        ax.set_xlabel(hex_x)
        ax.set_ylabel(hex_y)
        ax.set_title(f'Hexbin Plot of {hex_x} vs {hex_y}')
        st.pyplot(fig)

    # 4. Andrews Curves
    st.subheader("Andrews Curves")
    if 'label' in df.columns:
        fig = plt.figure()
        pd.plotting.andrews_curves(df, 'label')
        plt.title('Andrews Curves')
        st.pyplot(fig)

    # 5. Rug Plot
    st.subheader("Rug Plot")
    rug_feature = st.selectbox("Select Feature for Rug Plot", numeric_columns)
    if rug_feature:
        fig, ax = plt.subplots()
        sns.rugplot(df[rug_feature], ax=ax, color='red')
        ax.set_title(f'Rug Plot of {rug_feature}')
        st.pyplot(fig)

    # 6. Regression Plot
    st.subheader("Regression Plot")
    reg_x = st.selectbox("Select X for Regression Plot", numeric_columns)
    reg_y = st.selectbox("Select Y for Regression Plot", numeric_columns, index=1)
    if reg_x and reg_y:
        fig, ax = plt.subplots()
        sns.regplot(x=df[reg_x], y=df[reg_y], ax=ax, scatter_kws={'s':10}, line_kws={'color':'red'})
        ax.set_xlabel(reg_x)
        ax.set_ylabel(reg_y)
        ax.set_title(f'Regression Plot of {reg_x} vs {reg_y}')
        st.pyplot(fig)

    # 7. Heatmap
    st.subheader("Heatmap")
    heatmap_features = st.multiselect("Select features for Heatmap", numeric_columns)
    if heatmap_features:
        fig, ax = plt.subplots()
        corr = df[heatmap_features].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
        ax.set_title('Heatmap of Selected Features')
        st.pyplot(fig)

    # 8. Density Plot
    st.subheader("Density Plot")
    density_feature = st.selectbox("Select Feature for Density Plot", numeric_columns)
    if density_feature:
        fig, ax = plt.subplots()
        sns.kdeplot(df[density_feature], ax=ax, shade=True, color='purple')
        ax.set_title(f'Density Plot of {density_feature}')
        st.pyplot(fig)

    # 9. FacetGrid
    st.subheader("FacetGrid")
    facet_feature = st.selectbox("Select Feature for FacetGrid", numeric_columns)
    if facet_feature:
        g = sns.FacetGrid(df, col='label', col_wrap=3, height=4)
        g.map(sns.histplot, facet_feature)
        g.set_titles(col_template="{col_name}")
        st.pyplot(g.fig)

    # 10. ECDF (Empirical Cumulative Distribution Function) Plot
    st.subheader("ECDF Plot")
    ecdf_feature = st.selectbox("Select Feature for ECDF Plot", numeric_columns)
    if ecdf_feature:
        fig, ax = plt.subplots()
        sns.ecdfplot(df[ecdf_feature], ax=ax)
        ax.set_title(f'ECDF Plot of {ecdf_feature}')
        st.pyplot(fig)

    # 11. Residual Plot
    st.subheader("Residual Plot")
    res_x = st.selectbox("Select X for Residual Plot", numeric_columns)
    res_y = st.selectbox("Select Y for Residual Plot", numeric_columns, index=1)
    if res_x and res_y:
        fig, ax = plt.subplots()
        sns.residplot(x=df[res_x], y=df[res_y], ax=ax)
        ax.set_xlabel(res_x)
        ax.set_ylabel(res_y)
        ax.set_title(f'Residual Plot of {res_x} vs {res_y}')
        st.pyplot(fig)

    # 12. Pairplot with KDE
    st.subheader("Pairplot with KDE")
    selected_pairplot_features = st.multiselect("Select features for Pairplot with KDE", numeric_columns)
    if selected_pairplot_features:
        fig = sns.pairplot(df[selected_pairplot_features], kind='kde')
        st.pyplot(fig)

    # 13. Joint Plot with KDE
    st.subheader("Joint Plot with KDE")
    joint_x = st.selectbox("Select X for Joint Plot with KDE", numeric_columns)
    joint_y = st.selectbox("Select Y for Joint Plot with KDE", numeric_columns, index=1)
    if joint_x and joint_y:
        fig = sns.jointplot(x=joint_x, y=joint_y, data=df, kind="kde", color='purple')
        st.pyplot(fig)

    # 14. Violin Plot by Category
    st.subheader("Violin Plot by Category")
    violin_feature = st.selectbox("Select Feature for Violin Plot by Category", numeric_columns)
    if violin_feature:
        fig, ax = plt.subplots()
        sns.violinplot(x='label', y=violin_feature, data=df, ax=ax, palette='pastel')
        ax.set_title(f'Violin Plot of {violin_feature} by Category')
        st.pyplot(fig)

    # 15. Boxen Plot
    st.subheader("Boxen Plot")
    boxen_feature = st.selectbox("Select Feature for Boxen Plot", numeric_columns)
    if boxen_feature:
        fig, ax = plt.subplots()
        sns.boxenplot(x=df[boxen_feature], ax=ax, color='orange')
        ax.set_title(f'Boxen Plot of {boxen_feature}')
        st.pyplot(fig)

    # 16. Point Plot with Hue
    st.subheader("Point Plot with Hue")
    point_x = st.selectbox("Select X for Point Plot with Hue", numeric_columns)
    point_y = st.selectbox("Select Y for Point Plot with Hue", numeric_columns, index=1)
    if point_x and point_y:
        fig, ax = plt.subplots()
        sns.pointplot(x=df[point_x], y=df[point_y], hue=df['label'], ax=ax, palette='Set1')
        ax.set_title(f'Point Plot of {point_x} vs {point_y} with Hue')
        st.pyplot(fig)

    # 17. Swarm Plot with Size
    st.subheader("Swarm Plot with Size")
    swarm_x = st.selectbox("Select X for Swarm Plot with Size", numeric_columns)
    swarm_y = st.selectbox("Select Y for Swarm Plot with Size", numeric_columns, index=1)
    if swarm_x and swarm_y:
        fig, ax = plt.subplots()
        sns.swarmplot(x=df[swarm_x], y=df[swarm_y], size=8, ax=ax, palette='husl')
        ax.set_title(f'Swarm Plot of {swarm_x} vs {swarm_y} with Size')
        st.pyplot(fig)

    # 18. Strip Plot with Jitter
    st.subheader("Strip Plot with Jitter")
    strip_feature = st.selectbox("Select Feature for Strip Plot with Jitter", numeric_columns)
    if strip_feature:
        fig, ax = plt.subplots()
        sns.stripplot(x=df[strip_feature], jitter=True, ax=ax, color='pink')
        ax.set_title(f'Strip Plot of {strip_feature} with Jitter')
        st.pyplot(fig)

    # 19. Count Plot by Category
    st.subheader("Count Plot by Category")
    count_feature = st.selectbox("Select Feature for Count Plot by Category", numeric_columns)
    if count_feature:
        fig, ax = plt.subplots()
        sns.countplot(x=df[count_feature], ax=ax, palette='coolwarm')
        ax.set_title(f'Count Plot of {count_feature} by Category')
        st.pyplot(fig)

