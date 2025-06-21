import streamlit as st

# Page configuration
st.set_page_config(page_title="House Price Estimator", layout="centered")

# App Title
st.title("🏠 House Price Estimator")
st.markdown("Enter the house details below to get an estimated price.")

# Input Columns
col1, col2 = st.columns(2)

with col1:
    area = st.number_input("House Area (sq. ft)", min_value=200, max_value=10000, step=50, value=1000)
    washrooms = st.slider("Number of Washrooms", min_value=1, max_value=5, value=2)

with col2:
    bedrooms = st.slider("Number of Bedrooms", min_value=1, max_value=6, value=3)
    parking = st.selectbox("Parking Spaces", [0, 1, 2, 3], index=1)

# Price Calculation Button
if st.button("Calculate House Price"):
    # Custom rule-based formula
    price = (area * 6000) + (bedrooms * 1000000) + (washrooms * 700000) + (parking * 300000)
    
    st.success(f"🏡 **Estimated Price:** ₹ {price:,.2f}")
