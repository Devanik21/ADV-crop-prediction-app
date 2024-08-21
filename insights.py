import streamlit as st

def show_insights():
    st.title("🌾 Crop Insights")

    st.markdown("""
    <style>
    .insight-title {
        color: #FF5722; /* Orange for insight titles */
        font-weight: bold;
    }
    .insight-body {
        background-color: #F0F8FF; /* Light Alice Blue background for the body */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .crop-item {
        background-color: #FFFFFF; /* White background for each crop item */
        border-left: 5px solid #4CAF50; /* Green border for emphasis */
        padding: 10px;
        margin: 10px 0;
        border-radius: 5px;
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    .crop-item:nth-child(even) {
        background-color: #F5F5F5; /* Light gray for alternate rows */
    }
    </style>
    <div class="insight-body">
        <p>Get detailed insights on the recommended crops.</p>

        <div class="crop-item">
            <span class="insight-title">Wheat:</span> Suitable for temperate regions with moderate rainfall. Requires well-drained loamy soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Rice:</span> Thrives in tropical climates with high humidity and rainfall. Prefers clayey soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Maize:</span> Grows best in regions with warm temperatures and adequate rainfall. Needs fertile, well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Chickpea:</span> Grows well in dry regions and requires well-drained soil. Prefers a warm climate.
        </div>
        <div class="crop-item">
            <span class="insight-title">Kidney Beans:</span> Thrives in well-drained, fertile soil with moderate rainfall. Prefers a warm climate.
        </div>
        <div class="crop-item">
            <span class="insight-title">Pigeon Peas:</span> Suited for tropical and subtropical climates. Requires well-drained soil and moderate rainfall.
        </div>
        <div class="crop-item">
            <span class="insight-title">Moth Beans:</span> Grows in arid and semi-arid regions. Requires well-drained soil and moderate rainfall.
        </div>
        <div class="crop-item">
            <span class="insight-title">Mung Beans:</span> Prefers warm climates and well-drained soil. Tolerates drought conditions.
        </div>
        <div class="crop-item">
            <span class="insight-title">Blackgram:</span> Suitable for warm climates with moderate rainfall. Requires well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Lentil:</span> Thrives in cool climates with moderate rainfall. Prefers well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Pomegranate:</span> Prefers hot and dry climates. Requires well-drained soil and minimal water.
        </div>
        <div class="crop-item">
            <span class="insight-title">Banana:</span> Grows best in tropical climates with high humidity and ample water. Prefers well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Mango:</span> Thrives in tropical and subtropical climates. Requires warm temperatures and well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Grapes:</span> Prefers a warm, sunny climate with well-drained soil. Requires regular watering.
        </div>
        <div class="crop-item">
            <span class="insight-title">Watermelon:</span> Grows best in hot climates with plenty of sunlight. Requires well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Muskmelon:</span> Thrives in warm climates with ample sunlight. Prefers well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Apple:</span> Requires a temperate climate with cold winters. Prefers well-drained, fertile soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Orange:</span> Grows best in subtropical and tropical climates. Requires well-drained soil and plenty of water.
        </div>
        <div class="crop-item">
            <span class="insight-title">Papaya:</span> Thrives in tropical climates with high humidity. Requires well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Coconut:</span> Grows best in tropical climates with high humidity and ample rainfall. Requires sandy, well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Cotton:</span> Prefers hot, sunny climates with well-drained soil. Requires minimal rainfall.
        </div>
        <div class="crop-item">
            <span class="insight-title">Jute:</span> Grows in warm, humid climates with plenty of water. Requires well-drained soil.
        </div>
        <div class="crop-item">
            <span class="insight-title">Coffee:</span> Thrives in tropical climates with high humidity and well-drained soil. Requires moderate rainfall.
        </div>
    </div>
    """, unsafe_allow_html=True)
