import pandas as pd
import altair as alt
import streamlit as st
import controllers.ClienteController as ClienteController

def Graph():

    # Grafico do Sexo dos Clientes

    f = 0
    m = 0
    o = 0

    menorIdade = 0
    maiorIdade = 0
    idoso = 0

    ac = 0
    al = 0
    ap = 0
    am = 0
    ba = 0
    ce = 0
    df = 0
    es = 0
    go = 0
    ma = 0
    mt = 0
    ms = 0
    mg = 0
    pa = 0
    pb = 0
    pr = 0
    pe = 0
    pi = 0
    rj = 0
    rn = 0
    rs = 0
    ro = 0
    rr = 0
    sc = 0
    sp = 0
    se = 0
    to = 0
    ex = 0

    for item in (ClienteController.SelecionarTodos()):
        if item.sexo == "Feminino":
            f = f + 1

        if item.sexo == "Masculino":
            m = m + 1

        if item.sexo == "Outro":
            o = o + 1

    st.title("Gráfico dos Clientes")
    st.header("Gênero")

    source = pd.DataFrame({'Gênero': ['Homens', 'Mulheres', 'Outro'],
                           'Quantidade': [m, f, o]})

    sexo_cliente = alt.Chart(source).mark_bar().encode(
        x='Gênero',
        y='Quantidade',
        color='Gênero',
    )

    st.altair_chart(sexo_cliente, use_container_width=True)

    #Grafico de Idade dos Clientes

    for item in (ClienteController.SelecionarTodos()):
        if item.idade < 18:
            menorIdade = menorIdade + 1

        if item.idade > 17 and item.idade < 60:
            maiorIdade = maiorIdade + 1

        if item.idade > 59:
            idoso = idoso + 1

    st.header("Idade")

    source = pd.DataFrame({'Idade': ['Menor de 18 anos', 'Maior de 18 anos', 'Maior de 60 anos'],
                           'Quantidade': [menorIdade, maiorIdade, idoso]})

    idade_cliente = alt.Chart(source).mark_bar().encode(
        x='Idade',
        y='Quantidade',
        color='Idade',
    )

    st.altair_chart(idade_cliente, use_container_width=True)

    #Grafico de Localização dos Clientes
    
    for item in (ClienteController.SelecionarTodos()):

        if item.estado == "AC":
            ac = ac + 1
        if item.estado == "AL":
            al = al + 1
        if item.estado == "AP":
            ap = ap + 1
        if item.estado == "AM":
            am = am + 1
        if item.estado == "BA":
            ba = ba + 1
        if item.estado == "CE":
            ce = ce + 1
        if item.estado == "DF":
            df = df + 1
        if item.estado == "ES":
            es = es + 1
        if item.estado == "GO":
            go = go + 1
        if item.estado == "MA":
            ma = ma + 1
        if item.estado == "MT":
            mt = mt + 1
        if item.estado == "MS":
            ms = ms + 1
        if item.estado == "MG":
            mg = mg + 1
        if item.estado == "PA":
            pa = pa + 1
        if item.estado == "PB":
            pb = pb + 1
        if item.estado == "PR":
            pr = pr + 1
        if item.estado == "PE":
            pe = pe + 1
        if item.estado == "PI":
            pi = pi + 1
        if item.estado == "RJ":
            rj = rj + 1
        if item.estado == "RN":
            rn = rn + 1
        if item.estado == "RS":
            rs = rs + 1
        if item.estado == "RO":
            ro = ro + 1
        if item.estado == "RR":
            rr = rr + 1
        if item.estado == "SC":
            sc = sc + 1
        if item.estado == "SP":
            sp = sp + 1
        if item.estado == "SE":
            se = se + 1
        if item.estado == "TO":
            to = to + 1
        if item.estado == "EX":
            ex = ex + 1

    st.header("Estados")

    source = pd.DataFrame({'Estados': ["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT", \
                                        "MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO", \
                                        "RR","SC","SP","SE","TO","EX"],
                           'Quantidade': [ac,al,ap,am,ba,ce,df,es,go,ma,mt,ms,mg,pa,pb,pr,pe, \
                                            pi,rj,rn,rs,ro,rr,sc,sp,se,to,ex]})

    
    estado_grafico = alt.Chart(source).mark_bar().encode(
        x='Estados',
        y='Quantidade',
        color='Estados',
    )

    st.altair_chart(estado_grafico, use_container_width=True)
