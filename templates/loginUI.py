import streamlit as st
from views import ClienteView, ServicoView, HorarioView, ProfissionalView

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail:")
        senha = st.text_input("Informe a senha:", type="password")
        if st.button("Entrar"):
            cliente = ClienteView.autenticar_cliente(email, senha)
            profissional = ProfissionalView.autenticar_profissional(email, senha)

            if cliente:
                st.session_state["tipo_usuario"] = "cliente"
                st.session_state["id_usuario"] = cliente["id"]
                st.session_state["nome_usuario"] = cliente["nome"]
                st.rerun()
            elif profissional:
                st.session_state["tipo_usuario"] = "profissional"
                st.session_state["id_usuario"] = profissional["id"]
                st.session_state["nome_usuario"] = profissional["nome"]
                st.rerun()
            else:
                st.error("E-mail ou senha inválidos")

                