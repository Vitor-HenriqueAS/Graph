import streamlit as st
import controllers.EstoqueController as EstoqueController;
import models.Estoque as estoque;

def Create():

    st.title("Incluir Produto")

    with st.form(key="include_produto"):

        input_nome = st.text_input(label="Nome",max_chars=20,placeholder="Digite o nome do produto aqui")
        input_marca = st.text_input(label="Marca do Produto",max_chars=20,placeholder="Digite a marca do produto aqui")
        input_categoria = st.selectbox("Categoria do Produto", ['Alimentos e Bebidas', 'Beleza e Saúde', 'Eletrônicos e Eletrodoméstico', \
        'Esporte','Moveis','Acessórios',"Brinquedos","Moda"])
        input_valor = st.number_input(label="Valor do Produto",min_value=0.05,format='%f',step=0.50)
        input_qtd = st.number_input(label="Quantidade",min_value=1,format='%d',max_value=100,step=1)

        input_button_submit = st.form_submit_button("Enviar")

        if(input_button_submit):
            if input_nome == "" or input_marca == "" or input_categoria == "" or input_valor == "-"\
                or input_qtd == "":

                st.warning("Preencha todos os campos !")
            else:
                estoque.nome = input_nome
                estoque.marca = input_marca
                estoque.categoria = input_categoria
                estoque.valor = input_valor
                estoque.quantidade = input_qtd

                EstoqueController.Incluir(estoque.Estoque(0,input_nome,input_marca,input_categoria,input_valor,input_qtd))
                st.success(f"Produto {input_nome} inserido com sucesso !")
                
            #Ana vendeu Leite dd/mm/yyyy