import pandas as pd
import plotly.express as px
import streamlit as st

base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, "vehicles_us.csv")

car_data = pd.read_csv("vehicles_us.csv") # leer los datos
st.header('Anuncios de venta de coches')

build_histogram = st.checkbox('Construir histograma') # crear un botón
     
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

build_dispersion = st.checkbox("Construir gráfico de dispersión ") # crear un botón

if build_dispersion: # al hacer clic en el botón
    # escribir el mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear el gráfico de dispersión
    fig_d = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotli interactivo
    st.plotly_chart(fig_d, use_container_width=True)