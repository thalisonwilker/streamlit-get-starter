import streamlit as st
import pandas as pd
import numpy as np
import pandas as pd
from io import StringIO

st.title('Visualizador de CSV')

uploaded_file = st.file_uploader("Choose a file",type=["csv"], help="Carregue aqui o arquivo CSV")
if uploaded_file is not None:
    lines = uploaded_file.readlines()

    header = [ n.lower() for n in lines[:1][0].decode('latin-1').split(";") ]

    data = []

    for line in lines[1:50]:
        data.append(set( [ data for data in line.decode('latin-1').split(";") ] ))

    st.table(pd.DataFrame(data,columns=header))