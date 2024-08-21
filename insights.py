import streamlit as st

def show_insights():
    st.title("🌾 Crop Insights")

    st.markdown("""
    <style>
    .insight {
        font-size: 1.2em;
        margin: 15px 0;
        padding: 10px;
        border-left: 5px solid #4CAF50; /* Green border for emphasis */
        background-color: #FFFFFF; /* White background for insights */
        border-radius: 5px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    .insight-title {
        color: #FF5722; /* Orange for insight titles */
        font-weight: bold;
    }
    p {
        color: #333333; /* Dark grey for paragraph text */
    }
    </style>
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
    """, unsafe_allow_html=True)
