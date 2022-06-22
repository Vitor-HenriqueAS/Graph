## Importações Para Requisição da API: https://docs.awesomeapi.com.br/api-de-moedas ##
## pip install requests (necessario ter instalado) ##
import requests
import json
import streamlit as st




def Cotacao():

     ## Realizando Requisição do Dolar ##
    requisicao_dolar = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao_dolar.json()                          
  
    valor_dolar = float(cotacao["USD"]['bid'])
    

    ## Realizando Requisição do Euro ##
    requisicao_euro = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')
    cotacao_eur = requisicao_euro.json()
   
    valor_euro = float(cotacao_eur["EUR"]['bid'])
    

    ## Realizando Requisição do Bitcoin ##
    requisicao_bit = requests.get('https://economia.awesomeapi.com.br/all/BTC-BRL')
    cotacao_bit = requisicao_bit.json()
    
    valor_bit = float(cotacao_bit["BTC"]['bid'])

    st.title('Cotações de Hoje')
    col1, col2, col3 = st.columns(3)
    col1.metric("Dolar", valor_dolar)
    col2.metric("Euro", valor_euro)
    col3.metric("Bitcoin", valor_bit)

