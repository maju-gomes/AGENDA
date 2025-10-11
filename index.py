# aqui terá a classe principal que acessa página em template

from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from views import ClienteView, ServicoView, HorarioView, ProfissionalView
import streamlit as st

class IndexUI:

    def menu_visitante():
        opcao = st.sidebar.selectbox("Menu", ["Entrar no Sitema", "Abrir Conta"])
        if opcao == "Entrar no Sitema":
            LoginUI.main()
        if opcao == "Abrir Conta":
            AbrirContaUI.main()

    def menu_cliente():
        opcao = st.sidebar.selectbox("Menu", ["Meus Dados"])
        if opcao == "Meus Dados":
            PerfilClienteUI.main()

    def menu_admin():            
        opcao = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if opcao == "Cadastro de Clientes": ManterClienteUI.main()
        if opcao == "Cadastro de Serviços": ManterServicoUI.main()
        if opcao == "Cadastro de Horários": ManterHorarioUI.main()
        if opcao == "Cadastro de Profissionais": ManterProfissionalUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["id_usuario"]
            del st.session_state["nome_usuario"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["nome_usuario"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["nome_usuario"] + "!")
            if admin:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

    def main():
        # verifica a existência do usuário admin
        ClienteView.criar_cliente_admin()
        # monta o sidebar
        IndexUI.sidebar()

IndexUI.main()