import streamlit as st
import pandas as pd
import numpy as np

#Textos 
st.markdown("<h1 style='text-align: center;font-size:30px ;color: white;'>Dashboard Manutentção - Duraplast</h1>", unsafe_allow_html=True)


r1col1, r1col2, r1col3, r1col4 = st.columns(4)

with r1col1:
   st.metric(label="Quantidade de paradas", value="70 °F", delta="1.2 °F")

with r1col2:
   st.metric(label="Nº de maquinas quebradas", value="70 °F", delta="1.2 °F")

with r1col3:
   st.metric(label="Disponibilidade", value="70 °F", delta="1.2 °F")

with r1col4:
   st.metric(label="Confiabilidade", value="70 °F", delta="1.2 °F")


options = st.multiselect(
     'Cor favorita',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['x', 'Verde'])


st.write('Você selecionou:', options)

