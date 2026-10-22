import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados
car_data = pd.read_csv('vehicles.csv')

# Título e cabeçalho da aplicação
st.header('Painel de Análise de Anúncios de Veículos')
st.write('Explore a distribuição de quilometragem e a relação entre preço e condição dos veículos.')

# Caixa de seleção para criar o Histograma
build_histogram = st.checkbox('Criar histograma de quilometragem (odômetro)')

if build_histogram:
    st.write('Gerando histograma para a quilometragem dos veículos...')
    fig_hist = px.histogram(car_data, x="odometer", title="Distribuição do Odômetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Caixa de seleção para criar o Gráfico de Dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão (Preço vs. Odômetro)')

if build_scatter:
    st.write('Gerando gráfico de dispersão entre preço e odômetro por condição...')
    fig_scatter = px.scatter(
        car_data, 
        x="odometer", 
        y="price", 
        color="condition", 
        title="Preço vs. Odômetro por Condição do Veículo"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)