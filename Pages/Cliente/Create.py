import streamlit as st
from Pages.Cadastro_Login.Cadastro import verifica_email
import controllers.ClienteController as ClienteController;
import models.Cliente as cliente;

def Create():

    st.title("Incluir Cliente")
    st.button("Atualizar")

    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Nome",max_chars=40,placeholder="Digite o nome do cliente aqui")
        input_age = st.number_input(label="Idade",min_value=1,format='%d',max_value=100)
        input_gender = st.selectbox("Gênero",("-","Feminino","Masculino","Outro"))
        input_state = st.selectbox("Estado",("-","AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO","EX"))
        input_telephone = st.text_input(label="Telefone",max_chars=11,placeholder="Digite seu Telefone aqui (Mínimo 9 digitos)")
        input_email = st.text_input(label='Email',max_chars=40,placeholder="Digite seu melhor email (example@gmail.com)")
        input_cpf = st.text_input(label="CPF",max_chars=11,placeholder="Digite seu CPF (sem simbolos)")

        input_button_submit = st.form_submit_button("Enviar")

    if(input_button_submit):
        if input_name == "" or input_age == "" or input_gender == "" or input_gender == "-"\
            or input_telephone == "" or input_email == "" or input_cpf == "" or input_state == "-":
            st.warning("Preencha todos os campos !")
            
        else:
            input_email = input_email.lower()
            verifica = verifica_email(input_email)

            #Telefone
            if len(input_telephone) < 9:
                st.warning("Obrigatório o Telefone ter 9 dígitos no mínimo, sem simbolos !")
            #Email
            elif verifica == False:
                st.warning('Email Inválido, obrigatório o "@"')
            #CPF
            elif len(input_cpf) < 9:
                st.warning("Obrigatório o CPF ter 11 dígitos, sem simbolos !")
            else:
                #Telefone
                if input_telephone.isnumeric():

                    #CPF
                    if input_cpf.isnumeric():

                        cliente.nome = input_name
                        cliente.idade = input_age
                        cliente.sexo = input_gender
                        cliente.estado = input_state
                        cliente.telefone = input_telephone
                        cliente.email = input_email
                        cliente.cpf = input_cpf

                        ClienteController.Incluir(cliente.Cliente(0,input_name,input_age,input_gender,input_state,input_telephone,input_email,input_cpf))
                        st.success("Cliente incluido com sucesso !")
                        input_name = ""
                        input_age = ""
                        input_gender = "-"
                        input_state = "-"
                        input_telephone = ""
                        input_email = ""
                        input_cpf = ""
                       
                    else:
                        st.warning("Obrigatório o CPF ser números, sem simbolos !")
                    
                else:
                    st.warning("Obrigatório o Telefone ser números, sem simbolos !")
