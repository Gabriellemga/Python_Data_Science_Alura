# Imports
import streamlit as st
import json
from prophet.serialize import model_from_json
import pandas as pd
from prophet.plot import plot_plotly

# Carregando o modelo Prophet salvo
def load_model():
    with open('modelo_O3_prophet.json', 'r') as file_in:
        modelo = model_from_json(json.load(file_in))
        return modelo

modelo = load_model()

# Adicionando textos ao layout do Streamlit
st.title('Previsão de Níveis de Ozônio (O3) Utilizando a Biblioteca Prophet')

st.caption('''Este projeto utiliza a biblioteca Prophet para prever os níveis de ozônio em ug/m3. O modelo
           criado foi treinado com dados até o dia 05/05/2023 e possui um erro de previsão (RMSE - Erro Quadrático Médio) igual a 17.43 nos dados de teste.
           O usuário pode inserir o número de dias para os quais deseja a previsão, e o modelo gerará um gráfico
           interativo contendo as estimativas baseadas em dados históricos de concentração de O3.
           Além disso, uma tabela será exibida com os valores estimados para cada dia.''')

st.subheader('Insira o número de dias para previsão:')

# Recebendo o número de dias do usuário
dias = st.number_input('', min_value=1, value=1, step=1)

# Inicializando o estado da sessão
if 'previsao_feita' not in st.session_state:
    st.session_state['previsao_feita'] = False
    st.session_state['dados_previsao'] = None

# Criando o botão de previsão e geração de resultados
if st.button('Prever'):
    st.session_state.previsao_feita = True
    futuro = modelo.make_future_dataframe(periods=dias, freq='D')
    previsao = modelo.predict(futuro)
    st.session_state['dados_previsao'] = previsao

if st.session_state.previsao_feita:
    fig = plot_plotly(modelo, st.session_state['dados_previsao'])
    # Definindo o fundo do gráfico como branco e ajustando a cor do texto para preto para melhor visibilidade
    fig.update_layout({
        'plot_bgcolor': 'rgba(255, 255, 255, 1)',  # Define o fundo da área do gráfico como branco
        'paper_bgcolor': 'rgba(255, 255, 255, 1)', # Define o fundo externo ao gráfico como branco
        'title': {'text': "Previsão de Ozônio", 'font': {'color': 'black'}},
        'xaxis': {'title': 'Data', 'title_font': {'color': 'black'}, 'tickfont': {'color': 'black'}},
        'yaxis': {'title': 'Nível de Ozônio (O3 μg/m3)', 'title_font': {'color': 'black'}, 'tickfont': {'color': 'black'}}
    })
    st.plotly_chart(fig)
    
    # Preparando a tabela de previsões
    previsao = st.session_state['dados_previsao']
    tabela_previsao = previsao[['ds', 'yhat']].tail(dias)
    tabela_previsao.columns = ['Data (Dia/Mês/Ano)', 'O3 (ug/m3)']
    tabela_previsao['Data (Dia/Mês/Ano)'] = tabela_previsao['Data (Dia/Mês/Ano)'].dt.strftime('%d-%m-%Y')
    tabela_previsao['O3 (ug/m3)'] = tabela_previsao['O3 (ug/m3)'].round(2)
    tabela_previsao.reset_index(drop=True, inplace=True)
    st.write('Tabela contendo as previsões de ozônio (ug/m3) para os próximos {} dias:'.format(dias))
    st.dataframe(tabela_previsao, height=300)

    # Permitindo o download da tabela
    csv = tabela_previsao.to_csv(index=False)
    st.download_button(label='Baixar tabela como csv', data=csv, file_name='previsao_ozonio.csv', mime='text/csv')




