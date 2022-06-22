import streamlit as st
import controllers.ClienteController as ClienteController
import Pages.Cadastro_Login.Cadastro as cadastro
import models.Cliente as cliente;

nome_ant = ""
idade_ant = 0
sexo_ant = ""
estado_ant = ""
telefone_ant = ""
email_ant = ""
cpf_ant = ""

def Edit():

    global nome_ant
    global idade_ant
    global sexo_ant
    global estado_ant
    global telefone_ant
    global email_ant
    global cpf_ant

    st.title("Alterar")

    cliente_id = st.number_input(label="Digite o ID do cliente",min_value=0,format="%d",step=1)
    on_click_procura = st.button("Procurar", key="procurar_id_cliente")

    if on_click_procura:
        try:
            ClienteController.SelecionaID(cliente_id)

            nome_ant = ClienteController.x[0][1]
            idade_ant = int(ClienteController.x[0][2])

            sexo_ant = ClienteController.x[0][3]
            st.session_state.input_sexo = sexo_ant
            estado_ant = ClienteController.x[0][4]
            st.session_state.input_estado = estado_ant

            email_ant = ClienteController.x[0][5]
            telefone_ant = ClienteController.x[0][6]
            cpf_ant = ClienteController.x[0][7]

        except IndexError:
            st.warning("O Cliente não foi encontrado !")

    with st.form(key="alterar_cliente"):
        nome_alt = st.text_input(label="Altere o nome",max_chars=40,value=nome_ant,key="input_nome",placeholder="Digite o nome aqui")
        idade_alt = st.number_input(label="Altere a idade",max_value=100,value=idade_ant)
        sexo_alt = st.selectbox("Gênero",("Feminino","Masculino","Outro"),key="input_sexo")
        estado_alt = st.selectbox("Estado",("AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","EX"),key="input_estado")
        telefone_alt = st.text_input(label="Telefone",max_chars=11,value=telefone_ant,placeholder="Digite o Telefone (Mínimo 9 digitos)")
        email_alt = st.text_input(label='Email',max_chars=40,value=email_ant,placeholder="Digite o Email (example@gmail.com)")
        cpf_alt = st.text_input(label="CPF",max_chars=11,value=cpf_ant,placeholder="Obrigatório 11 digitos")
        input_button_edit = st.form_submit_button("Confirmar Alteração")

        if input_button_edit:

            verificado = cadastro.verifica_email(email_alt)

            if nome_alt == "" or telefone_alt == "" or email_alt == "" or cpf_alt == "":
                st.warning("Preencha todos os campos !")
                
            else:
                if len(telefone_alt) < 9 or verificado == False or len(cpf_alt) < 11 or idade_alt < 1:
                    st.warning("Campos Inválidos !")

                else:
                    ClienteController.Alterar(cliente.Cliente(cliente_id, nome_alt, idade_alt, sexo_alt, \
                        estado_alt, telefone_alt, email_alt, cpf_alt))
                        
                    st.success(f"ID : {cliente_id} | {nome_alt} Alterado com Sucesso !")

            

