
import streamlit as st
import controllers.EstoqueController as EstoqueController


def List():
    st.title("Tabela de Produtos")

    st.button("Regarregar página")

    colms = st.columns((1, 2, 2, 2, 1, 1, 1))
    campos = ['Nº', 'Nome', 'Marca', 'Categoria', 'Valor', 'Qtd', 'Excluir']
    for col, campo_nome in zip(colms, campos):
        col.write(campo_nome)

    for item in (EstoqueController.SelecionarTodos()):
        col1, col2, col3, col4, col5, col6, col7 = st.columns((1, 2, 2, 2, 1, 1, 1))
        col1.write(item.id)
        col2.write(item.nome)
        col3.write(item.marca)
        col4.write(item.categoria)
        col5.write("R$ "+item.valor)
        col6.write(item.quantidade)

        button_space_exluir = col7.empty()
        on_click_excluir = button_space_exluir.button("Excluir", 'btnExcluir' + str(item.id))

        if on_click_excluir:
            EstoqueController.Excluir(item.id)
            st.success(f"{item.nome} Foi Excluido com Sucesso !")