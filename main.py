# Recursos Utilizados : streamlit , streamlit_option_menu, streamlit_autorefresh
# pip install streamlit
# pip install streamlit-option-menu
# pip install streamlit-autorefresh


import streamlit as st;
from streamlit_autorefresh import st_autorefresh
from PIL import Image
import time

#Login e Cadastro
import Pages.Cadastro_Login.Login as login
import Pages.Cadastro_Login.Cadastro as cadastro
from streamlit_option_menu import option_menu

#Cliente
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente
import Pages.Cliente.Edit as PageEditCliente
import Pages.Cliente.Graph as PageGraphCliente

#Estoque
import Pages.Estoque.Create as PageCreateEstoque
import Pages.Estoque.List as PageListEstoque
import Pages.Estoque.Edit as PageEditEstoque
import Pages.Estoque.Graph as PageGraphEstoque

#Cotacao
import Pages.cotacao as PageCotacao

with open("./style/Main.css") as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)


verificado = login.verificado
try: 
    if verificado == False:

        col1, col2, col3 = st.columns([1,4,1])
        
        with col2:
            selected = option_menu(
                    menu_title = "Entrar",
                    options = ["Login","Cadastro"],
                    icons = ["box-arrow-in-right","person-plus"],
                    orientation = "horizontal"
                )

            if selected == "Login":
                login.Login()
                verificado = login.verificado

            if selected == "Cadastro":
                cadastro.Cadastro()



    if verificado:
        count = st_autorefresh(interval=2000, limit=2, key="contador")
        if count > 0:
            with st.sidebar:
                selected = option_menu(
                    menu_title = "Menu",
                    options = ["Home","Clientes","Estoque"],
                    menu_icon = "list",
                    icons = ["house","person-circle","archive"]
                    )

            if selected == 'Clientes':
                if st.sidebar.button("Visualizar Gráficos dos Clientes"):
                    with open("./style/grafico_cliente.css") as f:
                        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
                    PageGraphCliente.Graph()
                else:
                    #Controle de Clientes
                    selected = option_menu(
                    menu_title = "Controle de Clientes",
                    options = ["Incluir","Consultar","Atualizar"],
                    menu_icon = "person-circle",
                    icons = ["person-plus","card-list","arrow-down-up"],
                    orientation = "horizontal"
                    )
                    if selected == "Incluir":
                        PageCreateCliente.Create()
                    if selected == "Consultar":
                        PageListCliente.List()
                    if selected == "Atualizar":
                        PageEditCliente.Edit()

            elif selected == 'Estoque':
                if st.sidebar.button("Visualizar Gráficos do Estoque"):
                    with open("./style/grafico_estoque.css") as f:
                        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)

                    PageGraphEstoque.Graph()

                else:
                    #Controle de Estoque
                    selected = option_menu(
                    menu_title = "Controle de Estoque",
                    options = ["Incluir","Consultar","Atualizar"],
                    menu_icon = "archive",
                    icons = ["box-seam","card-list","arrow-down-up"],
                    orientation = "horizontal"
                    )

                    if selected == 'Incluir':
                        PageCreateEstoque.Create()
                    if selected == 'Consultar':
                        PageListEstoque.List()
                    if selected == 'Atualizar':
                        PageEditEstoque.Edit()

            else:
                if st.sidebar.button("Visualizar Cotações"):
                    with open("./style/cotacao.css") as f:
                        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)
                    PageCotacao.Cotacao()
                else:    
                    image = Image.open('image.png')
                    st.image(image, width=150)
                    st.title("Software Graph")
                    st.subheader("Tudo começa através de um click")
        else:
            with col2:
                with st.spinner('Aguarde...'):
                    time.sleep(2)
except NameError:
       with st.spinner('Aguarde...'):
            time.sleep(1)
              
                    
            


