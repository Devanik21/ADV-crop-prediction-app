import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("Crop_recommendation.csv")

def show_comparison():
    st.title("Crop Comparison")

    st.subheader("Select Crops to Compare")
    crops = df['label'].unique()
    crop1 = st.selectbox("Select Crop 1", crops)
    crop2 = st.selectbox("Select Crop 2", crops)

    if crop1 == crop2:
        st.warning("Please select two different crops for comparison.")
        return

    st.subheader(f"Comparison of {crop1} and {crop2}")
    
    comparison_df = df[df['label'].isin([crop1, crop2])]
    
    # Display descriptive statistics for the selected crops
    st.write("### Descriptive Statistics")
    st.write(comparison_df.groupby('label').describe())

    # Example of additional information and comparisons
    st.write("### Detailed Comparison")
    
    # Example values for conditions; replace with actual data if available
    conditions = {
        crop1: {
            'Optimal Temperature (°C)': 25,  # Replace with actual value
            'Optimal Rainfall (mm)': 800,    # Replace with actual value
            'Optimal Soil pH': 6.5           # Replace with actual value
        },
        crop2: {
            'Optimal Temperature (°C)': 20,  # Replace with actual value
            'Optimal Rainfall (mm)': 600,    # Replace with actual value
            'Optimal Soil pH': 7.0           # Replace with actual value
        }
    }

    st.markdown(f"""
    - **{crop1}:**
      - Optimal Temperature: {conditions[crop1]['Optimal Temperature (°C)']} °C
      - Optimal Rainfall: {conditions[crop1]['Optimal Rainfall (mm)']} mm
      - Optimal Soil pH: {conditions[crop1]['Optimal Soil pH']}

    - **{crop2}:**
      - Optimal Temperature: {conditions[crop2]['Optimal Temperature (°C)']} °C
      - Optimal Rainfall: {conditions[crop2]['Optimal Rainfall (mm)']} mm
      - Optimal Soil pH: {conditions[crop2]['Optimal Soil pH']}
    """)

    # Plotting if needed
    st.write("### Feature Comparison")
    fig, ax = plt.subplots()
    for crop in [crop1, crop2]:
        subset = df[df['label'] == crop]
        ax.hist(subset['temperature'], alpha=0.5, label=crop)
    ax.set_xlabel('Temperature (°C)')
    ax.set_ylabel('Frequency')
    ax.set_title('Temperature Distribution')
    ax.legend(loc='best')
    st.pyplot(fig)
