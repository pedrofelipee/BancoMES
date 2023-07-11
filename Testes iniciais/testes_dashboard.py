import streamlit as st


#Textos 
st.header("Minha dashboard")

import pandas as pd
import numpy as np


if st.button('MEU BOTÃO'):
    df = pd.DataFrame(
        np.random.randn(10, 3),
        columns=['Preço', 'Taxa de desocupação', 'Taxa inadiplencia',])

    st.bar_chart(df)

check = st.checkbox('Aceito')

if check:
     st.write('Marcado')