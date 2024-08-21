import streamlit as st
from home import show_home
from predict import show_predict
from analyze import show_analyze
from comparison import show_comparison
from visualization import show_visualization
from sustainability import show_sustainability
from insights import show_insights

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Predict", "Analyze", "Crop Comparison", "Advanced Visualization", "Sustainability Tips", "Crop Insights"])

# Display the selected page
if page == "Home":
    show_home()
elif page == "Predict":
    show_predict()
elif page == "Analyze":
    show_analyze()
elif page == "Crop Comparison":
    show_comparison()
elif page == "Advanced Visualization":
    show_visualization()
elif page == "Sustainability Tips":
    show_sustainability()
elif page == "Crop Insights":
    show_insights()
