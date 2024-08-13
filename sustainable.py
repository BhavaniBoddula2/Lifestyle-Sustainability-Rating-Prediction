
import streamlit as st
import pickle
import pandas as pd

model=pickle.load(open(r"lifestyle.pkl","rb"))

#Set up the title of the app
st.image("innomatics logo.jpg", width=300)
st.title("Lifestyle Sustainability Rating")
st.image("sustainable2.jpg", width=550)

#Define numerical and categorical features
numerical_features = ['Age', 'HomeSize', "MonthlyElectricityConsumption", "MonthlyWaterConsumption"]  # Replace with actual numerical feature names
categorical_features = {
    'EnvironmentalAwareness':[1,2,3,4,5],
    'Location': ['Urban', 'Suburban', 'Rural'], 
    'DietType': ['Mostly Plant-Based', 'Balanced', 'Mostly Animal-Based'],
    'LocalFoodFrequency': ['Often', 'Sometimes', 'Rarely', 'Always'],
    'TransportationMode': ['Car', 'Bike', 'Public Transit', 'Walk'],
    'EnergySource': ['Renewable', 'Non-Renewable', 'Mixed'],
    'HomeType': ['Apartment', 'House', 'Other'],
    'ClothingFrequency': ['Rarely', 'Sometimes', 'Often', 'Always'],
    'SustainableBrands': [ True, False],
    'CommunityInvolvement':  ['Low', 'Moderate', 'High'],
    'Gender': ['Female', 'Male', 'Non-Binary', 'Prefer not to say'],
    'UsingPlasticProducts': ['Never', 'Rarely', 'Sometimes', 'Often'],
    'DisposalMethods': ['Recycling', 'Composting', 'Landfill','Combination'],
    'PhysicalActivities': ['Low', 'Moderate', 'High']
}

#Collect user input for numerical features
input_data = {}
for feature in numerical_features:
    input_data[feature] = st.number_input(f'Enter value for {feature}')

#Collect user input for categorical features using dropdowns
for feature, options in categorical_features.items():
    input_data[feature] = st.selectbox(f'Select {feature}', options)

#Convert input data to DataFrame
input_df = pd.DataFrame([input_data])

#Predict
if st.button('Predict'):
    prediction = model.predict(input_df)
    st.write(f'Prediction: {prediction[0]}')
    if prediction == 5:
        st.write("Five Star Rating")
        st.image("5-star.png")
    elif prediction == 4:
        st.write("Four Star Rating")
        st.image("4-stars.png")
    elif prediction == 3:
        st.write("Three Star Rating")
        st.image("3-star.jpg")
    elif prediction == 2:
        st.write("Two Star Rating")
        st.image("2-star.webp")
    else:
        st.write("One Star Rating")
        st.image("one-star.jpg")