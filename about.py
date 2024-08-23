import streamlit as st

def show_about(section):
    st.title("ℹ️ About the App")

    if section == "overview":
        st.subheader("🌟 Overview")
        st.markdown("""
        **Welcome to our advanced crop analysis app!** This platform is designed to offer:
        
        - **🌾 Detailed Crop Insights**: Explore specific requirements and conditions for various crops.
        - **🔮 Predictive Analytics**: Utilize machine learning models to predict outcomes based on your inputs.
        - **📊 Comprehensive Data Analysis**: Uncover key insights from extensive crop data.
        - **🔍 Side-by-Side Comparisons**: Compare different crops to make informed decisions.
        - **📈 Advanced Visualizations**: Visualize data with sophisticated charts and graphs.
        - **🌱 Sustainability Tips**: Learn how to cultivate crops in an environmentally friendly manner.
        
        Whether you’re an agricultural expert, a data analyst, or someone passionate about sustainable farming, this tool is tailored to meet your needs.
        """, unsafe_allow_html=True)

    elif section == "features":
        st.subheader("✨ Features")
        st.markdown("""
        - **🚀 Prediction**: Leverage cutting-edge machine learning models for accurate predictions.
        - **🔍 Analysis**: Dive deep into crop data and discover actionable insights.
        - **⚖️ Comparison**: Analyze and compare multiple crops efficiently.
        - **📊 Visualization**: Explore your data through dynamic and interactive visualizations.
        - **🌍 Sustainability Tips**: Access valuable advice for sustainable crop cultivation.
        - **🔬 Crop Insights**: Gain in-depth knowledge about specific crops with detailed descriptions.
        """, unsafe_allow_html=True)

    elif section == "how_it_works":
        st.subheader("🔧 How It Works")
        st.markdown("""
        Our app combines state-of-the-art technologies and methodologies to offer a comprehensive analysis of crops:
        
        - **🤖 Machine Learning Models**: Predict outcomes based on historical data and current inputs.
        - **📊 Data Analysis Techniques**: Use various analytical methods to interpret crop data.
        - **📉 Visualization Tools**: View data in multiple formats, from simple charts to complex graphs.
        
        Navigate through the app's sections to utilize these features effectively and gain valuable insights into crop management.
        """, unsafe_allow_html=True)

    elif section == "credits":
        st.subheader("🙏 Credits")
        st.markdown("""
        Developed by [Devanik](https://www.linkedin.com/in/devanik/) with support from AI technologies. 
        Special thanks to all the supporters who made this project possible.
        """, unsafe_allow_html=True)
        # Display the image
        st.image("u.png", caption="Acknowledgments", use_column_width=True)

    # Style enhancements for a modern look
    st.markdown("""
    <style>
    .css-18e3th9 { font-family: 'Arial', sans-serif; }
    .css-1v0mbdj { color: #1f77b4; }
    .css-1k2he24 { color: #FF5733; } /* Example color for text */
    </style>
    """, unsafe_allow_html=True)
