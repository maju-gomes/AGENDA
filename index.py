# aqui terá a classe principal que acessa página em template

from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterServicoUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
import streamlit as st

class IndexUI:

    def menu_admin():            
        opcao = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if opcao == "Cadastro de Clientes": ManterClienteUI.main()
        if opcao == "Cadastro de Serviços": ManterServicoUI.main()
        if opcao == "Cadastro de Horários": ManterHorarioUI.main()
        if opcao == "Cadastro de Profissionais": ManterProfissionalUI.main()

    def sidebar():
        IndexUI.menu_admin()

    def main():
        IndexUI.sidebar()

IndexUI.main()