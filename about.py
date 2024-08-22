import streamlit as st

def show_about(section):
    if section == "overview":
        st.title("Overview")
        st.write("""
        This app is designed to provide detailed insights into various crops, predict potential outcomes, 
        analyze data, compare different crops, and offer sustainability tips.
        It's a comprehensive tool for anyone interested in agriculture, data analysis, or sustainability.
        """)
    elif section == "features":
        st.title("Features")
        st.write("""
        - **Prediction**: Use advanced machine learning models to predict outcomes based on your input.
        - **Analysis**: Analyze crop data to uncover key insights.
        - **Comparison**: Compare different crops side by side.
        - **Visualization**: Explore data through advanced visualizations.
        - **Sustainability Tips**: Get tips on how to grow crops sustainably.
        - **Crop Insights**: Gain insights into specific crops with detailed information.
        """)
    elif section == "how_it_works":
        st.title("How It Works")
        st.write("""
        The app uses a combination of machine learning models, data analysis techniques, and visualization tools 
        to help you understand and predict crop-related outcomes. You can navigate through different sections 
        to perform various tasks like predictions, analysis, and visualizations.
        """)
    elif section == "credits":
        st.title("Credits")
        st.write("""
        This app was developed by Devanik with the assistance of AI. 
        """)
