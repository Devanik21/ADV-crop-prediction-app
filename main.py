import streamlit as st
from home import show_home
from predict import show_predict
from analyze import show_analyze
from comparison import show_comparison
from visualization import show_visualization
from sustainability import show_sustainability
from insights import show_insights
from about import show_about  # Assuming you have a function to show the About page

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

    /* Style the sidebar selectbox */
    .sidebar .sidebar-content .stSelectbox label {
        color: #FFFFFF;
        font-size: 20px;
    }
    
    /* Style the selectbox */
    .sidebar .sidebar-content .stSelectbox div[data-baseweb=select] > div {
        background-color: #FF5733;
        color: #FFFFFF;
        font-size: 20px;
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

# Create a sidebar for navigation with a selectbox slider for main sections
st.sidebar.title("🌟 Navigation")
page = st.sidebar.selectbox("Choose a Section:", 
                            ["🏠 Home", 
                             "🔍 Predict", 
                             "📊 Analyze", 
                             "🌾 Crop Comparison", 
                             "📈 Advanced Visualization", 
                             "🌍 Sustainability Tips", 
                             "🌱 Crop Insights"
                             "ℹ️ About"])

# Create a sidebar selectbox for 'About the App'
st.sidebar.title("ℹ️ About the App")
about_page = st.sidebar.selectbox("Learn More:", 
                                  ["Overview", "Features", "How It Works", "Credits"])

# Display the selected page for main sections
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

# Display the selected 'About the App' page
if about_page == "Overview":
    show_about("overview")  # Pass a parameter to load the correct content
elif about_page == "Features":
    show_about("features")
elif about_page == "How It Works":
    show_about("how_it_works")
elif about_page == "Credits":
    show_about("credits")
