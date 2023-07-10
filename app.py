from chart import chart_nochurn_vs_nochurn, churn_by_variable, churn_by_variable_boxplot, churn_by_variable_kdeplot

import streamlit as st
import statistics  as sts
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


file = 'WA_Fn-UseC_-Telco-Customer-Churn.csv'
dados = pd.read_csv(file)

# Scrub
dados['SeniorCitizen'] = dados['SeniorCitizen'].astype(str)
dados['TotalCharges'] = dados['TotalCharges'].replace(' ', np.nan)
dados['TotalCharges'] = dados['TotalCharges'].astype(float)

mediana = sts.median(dados['TotalCharges'])
dados['TotalCharges'].fillna(mediana, inplace=True)


st.title('Trabalho Final – OSEMN\n')
st.write('Nesse projeto vamos analisar o dataset Telco Costumer Churn')

# função para selecionar a quantidade de linhas do dataframe

def mostra_qntd_linhas(dataframe):

    qntd_linhas = st.sidebar.slider('Selecione a quantidade de linhas que deseja mostrar na tabela', min_value = 1, max_value = len(dataframe), step = 1)

    st.write(dataframe.head(qntd_linhas).style.format(subset = ['MonthlyCharges'], formatter="{:.2f}"))

option_sexo = list(dados['gender'].unique())
option_sexo.append('Qualquer')

# Checkbox: Mostrar tabela

checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostrar_tabela:

    st.sidebar.markdown('## Filtro para a tabela')
    sexo = st.sidebar.selectbox('Selecione o sexo para apresentar na tabela', options = option_sexo)

    if sexo != 'Qualquer':
        df_sexo = dados.query('gender == @sexo')
        mostra_qntd_linhas(df_sexo)      
    else:
        mostra_qntd_linhas(dados)


# Gráfico: Não Ocorreu Churn vs Ocorreu

st.write('## Não ocorreu Churn x Ocorreu Churn')
chart_nochurn_vs_nochurn(dados)

st.sidebar.markdown('## Análise de Churn por Variáveis')
option_variavel = ('gender', 'SeniorCitizen', 'Partner', 'Dependents')
categoria_churn_by_variable = st.sidebar.selectbox('Selecione a variável para apresentar no gráfico', options = option_variavel)
st.write('## Análise de Churn por Variáveis')
st.write('Filtragem por: ' + ', '.join(option_variavel))
st.pyplot(churn_by_variable(dados, categoria_churn_by_variable))

st.sidebar.markdown('### Análise de Churn por Serviços inscritos')
option_servicos = ('PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies')
categoria_churn_by_service = st.sidebar.selectbox('Selecione a variável para apresentar no gráfico', options = option_servicos)
st.write('## Análise de Churn por serviços inscritos')
st.write('Filtragem por: ' + ', '.join(option_servicos))
st.pyplot(churn_by_variable(dados, categoria_churn_by_service))

st.write('## Meses de permanência')
st.pyplot(churn_by_variable(dados, 'tenure'))

st.sidebar.markdown('### Distribuição dos dados')
option_distribuicao = ('tenure', 'MonthlyCharges', 'TotalCharges')
categoria_churn_by_distribuicao = st.sidebar.selectbox('Selecione a variável para apresentar no gráfico', options = option_distribuicao)
st.write('## Distribuição dos dados')
st.write('**Distribuição dos dados em relação a quantidade de meses, valor cobrado mensalmente e valor total cobrado**')
st.write('Filtragem por: ' + ', '.join(option_distribuicao))
st.pyplot(churn_by_variable_boxplot(dados, categoria_churn_by_distribuicao))

st.sidebar.markdown('#### Mensal vs Total')
option_kdeplot = ('MonthlyCharges', 'TotalCharges')
categoria_kdeplot = st.sidebar.selectbox('Selecione a variável para apresentar no gráfico', options = option_kdeplot)
st.write('#### Mensal vs Total')
st.write('Distribuição dos dados em relação a quantidade de meses, valor cobrado mensalmente e valor total cobrado')
st.write('Filtragem por: ' + ', '.join(option_kdeplot))
st.pyplot(churn_by_variable_kdeplot(dados, categoria_kdeplot))