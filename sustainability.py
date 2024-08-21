import streamlit as st

def show_sustainability():
    st.title("🌱 Sustainability Tips for Farming")

    st.markdown("""
    <style>
    .main-title {
        color: #2E8B57;
        font-size: 2.5em;
        text-align: center;
        margin-bottom: 20px;
    }
    .sustainability-tips {
        background-color: #000000;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }
    .tip {
        font-size: 1.2em;
        margin: 10px 0;
        color: #a36e3c;
    }
    .tip-title {
        color: #4682B4;
        font-weight: bold;
    }
    </style>
    <div class="main-title">Sustainable Farming Practices</div>
    <div class="sustainability-tips">
        <div class="tip">
            <span class="tip-title">🌾 Crop Rotation:</span> Rotating crops helps maintain soil health and reduces the need for chemical fertilizers.
        </div>
        <div class="tip">
            <span class="tip-title">💧 Water Management:</span> Use drip irrigation and rainwater harvesting to conserve water.
        </div>
        <div class="tip">
            <span class="tip-title">🦠 Integrated Pest Management:</span> Combining biological, cultural, and mechanical control methods to manage pests sustainably.
        </div>
        <div class="tip">
            <span class="tip-title">🌿 Organic Farming:</span> Avoid synthetic chemicals and fertilizers, opting for organic alternatives.
        </div>
    </div>
    """, unsafe_allow_html=True)
