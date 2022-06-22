import streamlit as st
import models.LoginCad as cadastro
import controllers.LoginCadController as LoginCad


verificado = False

def Login():
    global verificado
    
    st.title('Login')

    with st.form(key='login'):
        email = st.text_input(label='Digite seu Email')
        password = st.text_input(label='Digite sua Senha', type='password')
        button_submit = st.form_submit_button('Entrar')


    if button_submit:
        
        if email == "" or password == "":
            st.warning("Preencha Todos os Campos!")
        else:
            cadastro.email = email
            cadastro.senha = password

            LoginCad.login(cadastro)
            if LoginCad.login(cadastro) == True:
                verificado = True
            else:
                st.warning("Login invalido!")
                
    return verificado