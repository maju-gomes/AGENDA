from views import ProfissionalView
import streamlit as st

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        opcao = ProfissionalView.listar_id_profissional(st.session_state["id_usuario"])
        nome = st.text_input("Novo nome:", opcao.get_nome())
        especialidade = st.text_input("Nova especialidade:", opcao.get_especialidade())
        conselho = st.text_input("Novo conselho:", opcao.get_conselho())
        email = st.text_input("Novo e-mail:", opcao.get_email())
        senha = st.text_input("Nova senha:", type="password")

        if st.button("Atualizar"):
            id = opcao.get_id()
            ProfissionalView.atualizar_profissional(id, nome, especialidade, conselho, email, senha)
            st.sucess("Profissional atualizado com sucesso")

