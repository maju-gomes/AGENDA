# a pasta template vai conter as páginas da aplicação
from views import ClienteView
import streamlit as st
import pandas as pd
import time


class ManterClienteUI:
    def main():
        st.header("Cadastro de Clientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterClienteUI.listar()
        with tab2: ManterClienteUI.inserir()
        with tab3: ManterClienteUI.atualizar()
        with tab4: ManterClienteUI.excluir()

    def listar():
        clientes = ClienteView.listar_cliente()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            list_dic = []
            for obj in clientes:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)


    def inserir():
        nome = st.text_input("Informe o nome:")
        email = st.text_input("Informe o e-mail:")
        fone = st.text_input("Informe o telefone:")
        senha = st.text_input("Informe a senha:", type="password")

        if st.button("Inserir"):
            ClienteView.inserir_cliente(nome, email, fone, senha)
            st.success("Cliente inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        clientes = ClienteView.listar_cliente()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            opcao = st.selectbox("Selecione o cliente", clientes)
            nome = st.text_input("Novo nome:", opcao.get_nome())
            email = st.text_input("Novo e-mail:", opcao.get_email())
            fone = st.text_input("Novo telefone:", opcao.get_fone())
            senha = st.text_input("Nova senha:", opcao.get_senha(), type="password")
            if st.button("Atualizar"):
                id = opcao.get_id()
                ClienteView.atualizar_cliente(id, nome, email, fone, senha)
                st.success("Cliente atualizado com sucesso")

    def excluir():
        clientes = ClienteView.listar_cliente()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            opcao = st.selectbox("Selecione o cliente:", clientes)
            if st.button("Excluir"):
                id = opcao.get_id()
                ClienteView.excluir_cliente(id)
                st.success("Cliente excluído com sucesso")