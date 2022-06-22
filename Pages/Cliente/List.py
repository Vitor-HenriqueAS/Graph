import streamlit as st;
import controllers.ClienteController as ClienteController

def List():
    st.title("Clientes")

    st.button("Regarregar página")

    colms = st.columns((1, 2, 1, 2, 1, 2, 2, 2, 1))
    campos = ['Nº', 'Nome', 'Idade', 'Sexo', 'Estado', 'Telefone', 'Email', 'CPF', 'Excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in (ClienteController.SelecionarTodos()):
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((1, 2, 1, 2, 1, 2, 2, 2, 1))
        col1.write(item.id)
        col2.write(item.nome)
        col3.write(item.idade)
        col4.write(item.sexo)
        col5.write(item.estado)
        col6.write(item.telefone)
        col7.write(item.email)
        col8.write(item.cpf)

        button_space_exluir = col9.empty()
        on_click_excluir = button_space_exluir.button("Excluir", 'btnExcluir' + str(item.id))

        if on_click_excluir:
            ClienteController.Excluir(item.id)
            st.success(f"{item.nome} Foi Excluido com Sucesso !")