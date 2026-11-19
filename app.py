import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Análisis de vehículos usados')

# Histograma
hist_button = st.checkbox('Mostrar histograma del odómetro')

if hist_button:
    fig = px.histogram(
        car_data,
        x='odometer',
        title='Distribución del odómetro'
    )

    st.plotly_chart(fig)

# Scatter plot
scatter_button = st.checkbox(
    'Mostrar gráfico de dispersión precio vs odómetro'
)

if scatter_button:
    fig = px.scatter(
        car_data,
        x='odometer',
        y='price',
        title='Precio vs odómetro'
    )

    st.plotly_chart(fig)