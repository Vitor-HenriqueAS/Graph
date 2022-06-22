import streamlit as st;
import models.LoginCad as cadastro
import controllers.LoginCadController as LoginCad



def verifica_email(email_cliente):
    letras = [chr(x) for x in range(ord('a'), ord('z') + 1)]
    numeros = [chr(x) for x in range(ord('1'), ord('9') + 1)]
    ponto_traço = [chr(x) for x in range(ord('-'), ord('.') + 1)]
    underline = [chr(x) for x in range(ord('_'), ord('`'))]
    #SIMBOLOS PERMITIDOS
    simbolos = [i for i in email_cliente if i not in letras and i not in numeros \
                and  i not in ponto_traço and i not in underline]
    if simbolos == ['@']:
        return True
    else:
        return False

def Cadastro():
    st.title('Cadastro')

    with st.form(key='cadastro'):
        name_cadastro = st.text_input(label='Nome',max_chars=40,placeholder='Digite seu nome aqui')
        telephone_cadastro = st.text_input(label="Telefone",max_chars=9,placeholder="Digite seu Telefone aqui (obrigatório 9 dígitos)")
        email_cadastro = st.text_input(label='Email',max_chars=40,placeholder="Digite seu melhor email (example@gmail.com)")
        cpf_cadastro = st.text_input(label="CPF",max_chars=11,placeholder="Digite seu CPF (sem simbolos)")
        password_cadastro = st.text_input(label='Senha', type='password',placeholder="Digite sua senha aqui (mínimo 4 dígitos)")
        button_submit_cadastro = st.form_submit_button('Cadastrar')

        if button_submit_cadastro:
            if name_cadastro == "" or telephone_cadastro == "" or email_cadastro == "" \
                or cpf_cadastro == "" or password_cadastro == "" :

                st.warning("Preencha Todos os Campos!")

            else:
                email_cadastro = email_cadastro.lower()
                verificado = verifica_email(email_cadastro)

                #Telefone
                if len(telephone_cadastro) < 9:
                    st.warning("Obrigatório o Telefone ter 9 dígitos, sem simbolos !")
                #E-mail
                elif verificado == False:
                    st.warning('Email Inválido, obrigatório o "@"')
                #CPF
                elif  len(cpf_cadastro) < 11:
                    st.warning("Obrigatório o CPF ter 11 dígitos, sem simbolos !")
                
                #Senha
                elif  len(password_cadastro) < 4:
                    st.warning("Obrigatório a Senha ter no mínimo 4 digitos !")
                
                else:
                    #Telefone
                    if telephone_cadastro.isnumeric():
                        
                        #CPF
                        if cpf_cadastro.isnumeric():
                            cadastro.nome = name_cadastro
                            cadastro.telefone = telephone_cadastro
                            cadastro.email = email_cadastro
                            cadastro.cpf = cpf_cadastro
                            cadastro.senha = password_cadastro

                            LoginCad.incluir(cadastro)
                            st.success("Usuario cadastrado com sucesso!")
                        else:
                            st.warning("Obrigatório o CPF ser números, sem simbolos !")
                    
                    else:
                        st.warning("Obrigatório o Telefone ser números, sem simbolos !")