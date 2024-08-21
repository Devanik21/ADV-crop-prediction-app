import streamlit as st
from home import show_home
from predict import show_predict
from analyze import show_analyze
from comparison import show_comparison
from visualization import show_visualization
from sustainability import show_sustainability
from insights import show_insights

# Apply custom CSS for a modern look
st.markdown(
    """
    <style>
    /* Style the sidebar */
    .sidebar .sidebar-content {
        background-color: #333333;
        padding: 20px;
        border-radius: 10px;
    }

    /* Style the sidebar title */
    .sidebar .sidebar-content h1 {
        color: #FF5733;
        text-align: center;
        font-size: 30px;
    }

    /* Style the sidebar radio buttons */
    .sidebar .sidebar-content .stRadio > label {
        color: #FFFFFF;
        font-size: 20px;
    }
    
    /* Style the selected radio button */
    .sidebar .sidebar-content .stRadio div[role=radiogroup] label span[data-baseweb=radio] {
        background-color: #FF5733;
    }
    
    /* Style the selected page content */
    .main .block-container {
        background-color: #1C1C1C;
        padding: 20px;
        border-radius: 10px;
        color: #FFFFFF;
    }
    
    /* General text color */
    .main .block-container p, .main .block-container h1, .main .block-container h2, .main .block-container h3, .main .block-container ul, .main .block-container ol {
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True
)

# Create a sidebar for navigation with a modern look
st.sidebar.title("🌟 Navigation")
page = st.sidebar.radio("Choose a Section:", 
                        ["🏠 Home", 
                         "🔍 Predict", 
                         "📊 Analyze", 
                         "🌾 Crop Comparison", 
                         "📈 Advanced Visualization", 
                         "🌍 Sustainability Tips", 
                         "🌱 Crop Insights"])

# Display the selected page
if page == "🏠 Home":
    show_home()
elif page == "🔍 Predict":
    show_predict()
elif page == "📊 Analyze":
    show_analyze()
elif page == "🌾 Crop Comparison":
    show_comparison()
elif page == "📈 Advanced Visualization":
    show_visualization()
elif page == "🌍 Sustainability Tips":
    show_sustainability()
elif page == "🌱 Crop Insights":
    show_insights()
