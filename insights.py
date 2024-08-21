import streamlit as st

def show_insights():
    st.title("🌾 Crop Insights")

    st.markdown("""
    <style>
    .main-title {
        color: #F5F5F5; /* Soft White for the title text */
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 20px;
    }
    .insights-body {
        background-color: #000000; /* Black background for the body */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.3);
    }
    .insight {
        font-size: 1.2em;
        margin: 10px 0;
        color: #F5F5F5; /* Soft White for the text */
    }
    .insight-title {
        color: #F5F5F5; /* Soft White for insight titles */
        font-weight: bold;
    }
    </style>
    <div class="main-title">Crop Insights</div>
    <div class="insights-body">
        <p>Get detailed insights on the recommended crops.</p>

        <div class="insight">
            <span class="insight-title">Wheat:</span> Suitable for temperate regions with moderate rainfall. Requires well-drained loamy soil.
        </div>
        <div class="insight">
            <span class="insight-title">Rice:</span> Thrives in tropical climates with high humidity and rainfall. Prefers clayey soil.
        </div>
        <div class="insight">
            <span class="insight-title">Maize:</span> Grows best in regions with warm temperatures and adequate rainfall. Needs fertile, well-drained soil.
        </div>
        
        <p>You can customize this section with more detailed insights based on the crops in your dataset.</p>
    </div>
    """, unsafe_allow_html=True)
