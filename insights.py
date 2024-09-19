import streamlit as st

def show_insights():
    st.title("🌾 Crop Insights")

    st.markdown("""
    Welcome to the Crop Insights section! Here you will find detailed information on various crops, including their optimal growing conditions and requirements. This will help you make informed decisions about which crops to grow based on your region's climate and soil conditions.
    """, unsafe_allow_html=True)
    
    # Define crop insights with additional information
    crops = {
        "Wheat": {
            "Description": "Suitable for temperate regions with moderate rainfall. Requires well-drained loamy soil.",
            "Best Planting Season": "Autumn or early spring",
            "Common Issues": "Susceptible to rust diseases and aphid infestations."
        },
        "Rice": {
            "Description": "Thrives in tropical climates with high humidity and rainfall. Prefers clayey soil.",
            "Best Planting Season": "Late spring to early summer",
            "Common Issues": "Prone to pests like rice weevils and diseases like blast."
        },
        "Maize": {
            "Description": "Grows best in regions with warm temperatures and adequate rainfall. Needs fertile, well-drained soil.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Can suffer from corn borers and rootworms."
        },
        "Chickpea": {
            "Description": "Grows well in dry regions and requires well-drained soil. Prefers a warm climate.",
            "Best Planting Season": "Autumn to early winter",
            "Common Issues": "Vulnerable to fungal diseases and aphid infestations."
        },
        "Kidney Beans": {
            "Description": "Thrives in well-drained, fertile soil with moderate rainfall. Prefers a warm climate.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Can be affected by bean beetles and blight."
        },
        "Pigeon Peas": {
            "Description": "Suited for tropical and subtropical climates. Requires well-drained soil and moderate rainfall.",
            "Best Planting Season": "Rainy season",
            "Common Issues": "Susceptible to pests like pod borers and root rot."
        },
        "Moth Beans": {
            "Description": "Grows in arid and semi-arid regions. Requires well-drained soil and moderate rainfall.",
            "Best Planting Season": "Monsoon season",
            "Common Issues": "Can be affected by pod fly and rust."
        },
        "Mung Beans": {
            "Description": "Prefers warm climates and well-drained soil. Tolerates drought conditions.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Vulnerable to aphids and bacterial diseases."
        },
        "Blackgram": {
            "Description": "Suitable for warm climates with moderate rainfall. Requires well-drained soil.",
            "Best Planting Season": "Rainy season",
            "Common Issues": "Can suffer from pests like gram caterpillars and diseases like blight."
        },
        "Lentil": {
            "Description": "Thrives in cool climates with moderate rainfall. Prefers well-drained soil.",
            "Best Planting Season": "Early spring to late summer",
            "Common Issues": "Prone to fungal diseases and aphid infestations."
        },
        "Pomegranate": {
            "Description": "Prefers hot and dry climates. Requires well-drained soil and minimal water.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Susceptible to pests like pomegranate butterflies and fungal diseases."
        },
        "Banana": {
            "Description": "Grows best in tropical climates with high humidity and ample water. Prefers well-drained soil.",
            "Best Planting Season": "Year-round",
            "Common Issues": "Can be affected by Panama disease and banana weevils."
        },
        "Mango": {
            "Description": "Thrives in tropical and subtropical climates. Requires warm temperatures and well-drained soil.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Prone to mango fruit fly and anthracnose."
        },
        "Grapes": {
            "Description": "Prefers a warm, sunny climate with well-drained soil. Requires regular watering.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Susceptible to powdery mildew and grapevine pests."
        },
        "Watermelon": {
            "Description": "Grows best in hot climates with plenty of sunlight. Requires well-drained soil.",
            "Best Planting Season": "Late spring to early summer",
            "Common Issues": "Can suffer from downy mildew and watermelon rind problems."
        },
        "Muskmelon": {
            "Description": "Thrives in warm climates with ample sunlight. Prefers well-drained soil.",
            "Best Planting Season": "Spring to early summer",
            "Common Issues": "Prone to fungal diseases and pests like melon flies."
        },
        "Apple": {
            "Description": "Requires a temperate climate with cold winters. Prefers well-drained, fertile soil.",
            "Best Planting Season": "Late autumn to early spring",
            "Common Issues": "Susceptible to apple scab and codling moth."
        },
        "Orange": {
            "Description": "Grows best in subtropical and tropical climates. Requires well-drained soil and plenty of water.",
            "Best Planting Season": "Spring to summer",
            "Common Issues": "Can be affected by citrus greening and pests like aphids."
        },
        "Papaya": {
            "Description": "Thrives in tropical climates with high humidity. Requires well-drained soil.",
            "Best Planting Season": "Year-round",
            "Common Issues": "Prone to papaya ringspot virus and pests like whiteflies."
        },
        "Coconut": {
            "Description": "Grows best in tropical climates with high humidity and ample rainfall. Requires sandy, well-drained soil.",
            "Best Planting Season": "Year-round",
            "Common Issues": "Susceptible to coconut beetles and diseases like cadang-cadang."
        },
        "Cotton": {
            "Description": "Prefers hot, sunny climates with well-drained soil. Requires minimal rainfall.",
            "Best Planting Season": "Spring to summer",
            "Common Issues": "Can suffer from cotton bollworms and wilt diseases."
        },
        "Jute": {
            "Description": "Grows in warm, humid climates with plenty of water. Requires well-drained soil.",
            "Best Planting Season": "Rainy season",
            "Common Issues": "Prone to jute mallow and root rot."
        },
        "Coffee": {
            "Description": "Thrives in tropical climates with high humidity and well-drained soil. Requires moderate rainfall.",
            "Best Planting Season": "Year-round",
            "Common Issues": "Susceptible to coffee rust and pests like coffee berry borer."
        }
    }

    # Display insights in an interactive format
    for crop, details in crops.items():
        with st.expander(crop, expanded=False):
            st.write(f"**Description:** {details['Description']}")
            st.write(f"**Best Planting Season:** {details['Best Planting Season']}")
            st.write(f"**Common Issues:** {details['Common Issues']}")

    # Add a summary or additional information section
    st.markdown("""
    ### Summary:
    Understanding the specific requirements for each crop can help optimize agricultural practices and ensure better yields. Choose the crop that best fits your local conditions and soil type for optimal results.
    """, unsafe_allow_html=True)
