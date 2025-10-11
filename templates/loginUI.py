import streamlit as st
from views import ClienteView, ServicoView, HorarioView, ProfissionalView

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail:")
        senha = st.text_input("Informe a senha:", type="password")

        if st.button("Entrar"):
            cliente = ClienteView.autenticar_cliente(email, senha)
            if cliente == None:
                st.write("E-mail ou senha inválidos")
            else:
                st.session_state["id_usuario"] = cliente["id"]
                st.session_state["nome_usuario"] = cliente["nome"]
                st.rerun()

                