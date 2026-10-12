import streamlit as st
import pandas as pd
import joblib

# Saved model load karein
model = joblib.load('real_estate_model.pkl')

st.title("🏡 Karachi Real Estate Price Prediction App")
st.write("Aap apni property ki details darj karein taake estimated price pata chal sakay.")

# User se inputs lena
district = st.selectbox('District', ['Karachi South', 'Karachi East', 'Karachi Central', 'Karachi West', 'Malir', 'Korangi'])
town = st.text_input('Town Municipal Committee', 'Gulshan-e-Iqbal')
area = st.text_input('Area Locality', 'Block 4')
size_sqyd = st.number_input('Property Size (Sq Yd)', min_value=50, max_value=2000, value=240)
bedrooms = st.slider('Bedrooms', 1, 6, 3)
bathrooms = st.slider('Bathrooms', 1, 6, 3)
total_floors = st.selectbox('Total Floors', [1, 2, 3, 4])
property_age = st.slider('Property Age (Years)', 0, 30, 5)
road_size = st.selectbox('Road Size (Ft)', [20, 30, 40, 60, 80])
environment = st.selectbox('Environment Quality', ['Low', 'Medium', 'High'])
water = st.selectbox('Water Availability', ['Municipal', 'Tanker', 'Both'])
gas = st.selectbox('Gas Availability', ['Yes', 'No'])
mosque = st.selectbox('Mosque Nearby', ['Yes', 'No'])
market = st.selectbox('Commercial Market Nearby', ['Yes', 'No'])
hospital = st.selectbox('Hospital Within 2km', ['Yes', 'No'])
university = st.selectbox('University Within 5km', ['Yes', 'No'])
park = st.selectbox('Park Nearby', ['Yes', 'No'])
security = st.selectbox('Security Level', ['Low', 'Medium', 'High'])
flooding = st.selectbox('Monsoon Flooding History', ['Yes', 'No'])

# Prediction Button
if st.button('Predict Price'):
    input_data = pd.DataFrame({
        'District': [district],
        'Town_Municipal_Committee': [town],
        'Area_Locality': [area],
        'Property_Size_SqYd': [size_sqyd],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Total_Floors': [total_floors],
        'Property_Age_Years': [property_age],
        'Road_Size_Ft': [road_size],
        'Environment_Quality': [environment],
        'Water_Availability': [water],
        'Gas_Availability': [gas],
        'Mosque_Nearby': [mosque],
        'Commercial_Market_Nearby': [market],
        'Hospital_Within_2km': [hospital],
        'University_Within_5km': [university],
        'Park_Nearby': [park],
        'Security_Level': [security],
        'Monsoon_Flooding_History': [flooding]
    })
    
    predicted_price = model.predict(input_data)[0]
    st.success(f"Estimated Property Price: PKR {predicted_price:,.2f}")
