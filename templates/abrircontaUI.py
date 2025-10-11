import streamlit as st
from views import ClienteView, ServicoView, HorarioView, ProfissionalView
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        senha = st.text_input("Infrome a senha:", type="password")

        if st.button("Criar conta"):
            ClienteView.inserir_cliente(nome, email, fone, senha)
            st.success("Conta criada com sucesso")
            time.sleep(2)
            st.rerun()