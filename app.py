from chart import chart_nochurn_vs_nochurn, churn_by_variable, churn_by_variable_boxplot, churn_by_variable_kdeplot

import streamlit as st
import statistics  as sts
import pandas as pd
#import seaborn as sns
#import matplotlib.pyplot as plt
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
st.write('Trabalho desenvolvido utilizando a metodologia **OSEMN**, composta pelas etapas: **O**btain, **S**crub, **E**xplore, **M**odel e i**N**terpret. Essa metodologia é aplicada para solucionar problemas em ciência de dados, seguindo um conjunto de etapas recomendadas para o desenvolvimento da solução.')
st.write('#### Nesse projeto vamos analisar o dataset *Telco Customer Churn*')
st.write('**Churn**, ou taxa de cancelamento, é a medida da quantidade de clientes que deixam de utilizar um produto ou serviço em um período de tempo. É uma métrica usada para avaliar a fidelidade dos clientes e a saúde do negócio. Uma alta taxa de churn indica problemas como insatisfação dos clientes, concorrência acirrada ou falhas na oferta do produto. As empresas buscam reduzir o churn investindo em estratégias de retenção de clientes e melhorando a experiência do usuário.')

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
st.write('O eixo horizontal do gráfico apresenta as duas categorias: *Não ocorreu Churn* e *Ocorreu Churn*. O eixo vertical representa o número de clientes. Esse gráfico permite visualizar e comparar a quantidade de clientes que permaneceram versus aqueles que cancelaram seus serviços, fornecendo insights sobre a fidelidade e retenção dos clientes. Isso ajuda as empresas a entenderem melhor o impacto do churn em sua base de clientes e a tomar decisões estratégicas para reduzir a rotatividade e melhorar a retenção.')

# Gráfico: Análise de Churn por Variáveis
st.sidebar.markdown('## Análise de Churn por Variáveis')
option_variavel = ('gender', 'SeniorCitizen', 'Partner', 'Dependents')
categoria_churn_by_variable = st.sidebar.selectbox('Selecione o grupo para apresentar no gráfico', options = option_variavel)
st.write('## Análise de Churn por Variáveis')
st.write('Filtragem por: ' + ', '.join(option_variavel))
st.pyplot(churn_by_variable(dados, categoria_churn_by_variable, hue="Churn"))
st.write('Comparação da proporção de churn entre diferentes grupos formados pelas variáveis de: gender (gênero), SeniorCitizen (indicador de idoso), Partner (indicador de parceiro) e Dependents (indicador de dependentes).')

# Gráfico: Análise de Churn por Serviços inscritos
st.sidebar.markdown('### Análise de Churn por Serviços Inscritos')
option_servicos = ('PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies')
categoria_churn_by_service = st.sidebar.selectbox('Selecione o serviço para apresentar no gráfico', options = option_servicos)
st.write('## Análise de Churn por serviços Inscritos')
st.write('Filtragem por: ' + ', '.join(option_servicos))
st.pyplot(churn_by_variable(dados, categoria_churn_by_service, hue='Churn'))
st.write('Ocorrência de churn para diferentes serviços: PhoneService (serviço de telefone), MultipleLines (múltiplas linhas telefônicas), InternetService (serviço de internet), OnlineSecurity (segurança online), OnlineBackup (backup online), DeviceProtection (proteção de dispositivo), TechSupport (suporte técnico), StreamingTV (transmissão de TV) e StreamingMovies (transmissão de filmes).')

# Gráfico: Meses de Permanência
st.write('## Meses de permanência')
st.pyplot(churn_by_variable(dados, 'tenure', (40, 12), hue="Churn"))
st.write('Presença de churn em relação ao tempo de permanência dos clientes. Essa análise ajuda a identificar tendências sazonais ou oportunidades de melhoria na retenção de clientes ao longo do tempo, permitindo que as empresas ajustem suas estratégias para reduzir o churn e promover a fidelidade dos clientes.')

# Gráfico: Distribuição dos dados
st.sidebar.markdown('### Distribuição dos dados')
option_distribuicao = ('tenure', 'MonthlyCharges', 'TotalCharges')
categoria_churn_by_distribuicao = st.sidebar.selectbox('Selecione o período para apresentar no gráfico', options = option_distribuicao)
st.write('## Distribuição dos dados')
st.write('**Distribuição dos dados em relação a quantidade de meses, valor cobrado mensalmente e valor total cobrado**')
st.write('Filtragem por: ' + ', '.join(option_distribuicao))
st.pyplot(churn_by_variable_boxplot(dados, categoria_churn_by_distribuicao))
st.write('O eixo horizontal mostra os valores possíveis para cada variável, enquanto o eixo vertical representa a frequência ou a densidade dos valores. O gráfico permite visualizar como os dados estão distribuídos em cada uma das variáveis, destacando possíveis padrões, outliers ou características relevantes.')

st.sidebar.markdown('#### Mensal vs Total')
option_kdeplot = ('MonthlyCharges', 'TotalCharges')
categoria_kdeplot = st.sidebar.selectbox('Selecione o período para apresentar no gráfico', options = option_kdeplot)
st.write('#### Mensal vs Total')
st.write('Distribuição dos dados em relação a quantidade de meses, valor cobrado mensalmente e valor total cobrado')
st.write('Filtragem por: ' + ', '.join(option_kdeplot))
st.pyplot(churn_by_variable_kdeplot(dados, categoria_kdeplot))
st.write('O gráfico permite visualizar e comparar a distribuição das cobranças mensais e totais para os clientes que não tiveram churn e os que tiveram.')