import streamlit as st
import pandas as pd

st.title("🎈 Hamroz's Forecast")

st.write('Predict your apartment price')

with st.expander('Initial data'):
    st.write("**Raw Data**")
    df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
    st.write("**X**")
    x_raw = df.drop('species', axis=1)
    x_raw

    st.write("**Y**")
    y_raw = df.species
    y_raw

    df.columns

    with st.expander('Data Viz'):
        st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

    with st.sidebar:
        st.header('Input features')
        island = st.selectbox('island', ('Biscoe', 'Dream', 'Torgersen'))
        bill_length_mm = st.slider('Bill length (mm)', 32.1, 59.6, 43.9)
        bill_depth_mm = st.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
        flipper_length_mm = st.slider('flipper length (mm)', 172.0, 233.0, 201.0)
        body_mass_g = st.slider('Body mass (g)', 2700.0, 6300.0, 4207.0)
        gender = st.selectbox('Gender', ('male', 'female'))

    # Create a DataFrame for the input features
    data = {'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g,
            'sex': gender}
    input_df = pd.DataFrame(data, index=[0])
    input_penguins = pd.concat([input_df, x_raw], axis=0)
