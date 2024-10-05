
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

  with st.expander('Data Viz'):
      st.scatter_chart(data=df, x='bill_length_mn', y='body_mass_g', color='species')
