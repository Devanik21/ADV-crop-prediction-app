import streamlit as st

def show_insights():
    st.title("Crop Insights")

    st.markdown("""
    Get detailed insights on the recommended crops.

    ### Example Insights:
    - **Wheat:** Suitable for temperate regions with moderate rainfall. Requires well-drained loamy soil.
    - **Rice:** Thrives in tropical climates with high humidity and rainfall. Prefers clayey soil.
    - **Maize:** Grows best in regions with warm temperatures and adequate rainfall. Needs fertile, well-drained soil.
    
    You can customize this section with more detailed insights based on the crops in your dataset.
    """)
