import pandas as pd
import altair as alt
import streamlit as st
import controllers.EstoqueController as EstoqueController




def Graph():
    alimentos_Bebidas = 0
    beleza_Saude = 0
    eletro = 0
    esporte = 0
    moveis = 0
    acessorios = 0
    brinquedos = 0
    moda = 0

    for item in (EstoqueController.SelecionarTodos()):
        if item.categoria == "Alimentos e Bebidas":
            alimentos_Bebidas = alimentos_Bebidas + item.quantidade

        if item.categoria == "Beleza e Saúde":
            beleza_Saude = beleza_Saude + item.quantidade

        if item.categoria == "Eletrônicos e Eletrodoméstico":
            eletro = eletro + item.quantidade

        if item.categoria == "Esporte":
            esporte = esporte + item.quantidade
        
        if item.categoria == "Moveis":
            moveis = moveis + item.quantidade
        
        if item.categoria == "Acessórios":
            acessorios = acessorios + item.quantidade
        
        if item.categoria == "Brinquedos":
            brinquedos = brinquedos + item.quantidade

        if item.categoria == "Moda":
            moda = moda + item.quantidade
    
    st.title("Gráfico de Categoria dos Produtos")
    
    source = pd.DataFrame({'Categoria': ['Alimentos e Bebidas', 'Beleza e Saúde', 'Eletrônicos e Eletrodoméstico','Esporte',\
        'Moveis','Acessórios',"Brinquedos","Moda"],
                           'Quantidade': [alimentos_Bebidas,beleza_Saude, eletro, esporte, moveis, acessorios, brinquedos, moda]})

    estoque = alt.Chart(source).mark_bar().encode(
        x='Categoria',
        y='Quantidade',
        color='Categoria',
       
    )

    st.altair_chart(estoque, use_container_width=True)

   
    

   