import streamlit as st
from views import ClienteView, ServicoView, HorarioView, ProfissionalView
import time

class PerfilClienteUI:
    def main():
        st.header("Meus dados")
        opcao = ClienteView.listar_id_cliente(st.session_state["id_usuario"])
        nome = st.text_input("Informe o novo nome:", opcao.get_nome())
        email = st.text_input("Informe o novo e-mail:", opcao.get_email())
        fone = st.text_input("Informe o novo telefone:", opcao.get_fone())
        senha = st.text_input("Informe a nova senha:", opcao.get_senha(), type="password")

        if st.button("Atualizar"):
            id = opcao.get_id()
            ClienteView.atualizar_cliente(id, nome, email, fone, senha)
            st.success("Cliente atualizado com sucesso")
