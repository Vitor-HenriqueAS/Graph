import streamlit as st
import controllers.EstoqueController as EstoqueController
import models.Estoque as estoque;

nome_ant = ""
marca_ant = ""
categoria_ant = ""
valor_ant = 0.00
qtd_ant = 0

def Edit():

    global nome_ant
    global marca_ant
    global categoria_ant
    global valor_ant
    global qtd_ant

    st.title("Alterar Produto")

    produto_id = st.number_input(label="Digite o ID do produto",min_value=0,format="%d",step=1)
    on_click_procura = st.button("Procurar", key="procurar_id_produto")

    if on_click_procura:
        try:
            EstoqueController.SelecionaID(produto_id)
            nome_ant = EstoqueController.x[0][1]
            marca_ant = EstoqueController.x[0][2]
            categoria_ant = EstoqueController.x[0][3]
            valor_ant = float(EstoqueController.x[0][4])
            qtd_ant = int(EstoqueController.x[0][5])

        except IndexError:
            st.warning("O Produto não foi encontrado !")

    with st.form(key="alterar_produto"):
        nome_alt = st.text_input(label="Nome",max_chars=20,placeholder="Digite o nome do produto aqui",value=nome_ant)
        marca_alt = st.text_input(label="Marca do Produto",max_chars=20,placeholder="Digite a marca do produto aqui",value=marca_ant)
        categoria_alt = st.text_input(label="Categoria do Produto",max_chars=40,placeholder="Digite a categoria do produto aqui",value=categoria_ant)
        valor_alt = st.number_input(label="Valor do Produto",value=valor_ant)
        qtd_alt = st.number_input(label="Quantidade",max_value=100,value=qtd_ant)
        input_button_edit = st.form_submit_button("Confirmar Alteração")

        if input_button_edit:

            if nome_alt == "" or marca_alt == "" or categoria_alt == "" or valor_alt == "" or qtd_alt == "":
                st.warning("Preencha todos os campos !")
                
            else:
                if valor_alt < 0 or qtd_alt < 0 or len(str(valor_alt)) > 10:
                    st.warning("Campos Inválidos")
                else:
                    EstoqueController.Alterar(estoque.Estoque(produto_id, nome_alt, marca_alt, \
                        categoria_alt, valor_alt, qtd_alt))
                        
                    st.success(f"ID : {produto_id} | {nome_alt} Alterado com Sucesso !")