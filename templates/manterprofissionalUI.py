# a pasta template vai conter as páginas da aplicação
from views import ProfissionalView
import streamlit as st
import pandas as pd
import time


class ManterProfissionalUI:
    def main():
        st.header("Cadastro de Profissionais")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissionais = ProfissionalView.listar_profissional()
        if len(profissionais) == 0:
            st.write("Nenhum Profissional cadastrado")
        else:
            list_dic = []
            for obj in profissionais:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)


    def inserir():
        nome = st.text_input("Informe o nome:")
        especialidade = st.text_input("Informe a especialidade:")
        conselho = st.text_area("Dê um conselho:")

        if st.button("Inserir"):
            ProfissionalView.inserir_profissional(nome, especialidade, conselho)
            st.success("Profissional inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        profissionais = ProfissionalView.listar_profissional()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            opcao = st.selectbox("Selecione o profissional", profissionais)
            nome = st.text_input("Novo nome:", opcao.get_nome())
            especialidade = st.text_input("Nova especialidade:", opcao.get_especialidade())
            conselho = st.text_area("Novo conselho:", opcao.get_conselho())
            if st.button("Atualizar"):
                id = opcao.get_id()
                ProfissionalView.atualizar_profissional(id, nome, especialidade, conselho)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        profissionais = ProfissionalView.listar_profissional()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            opcao = st.selectbox("Selecione o profissional:", profissionais)
            if st.button("Excluir"):
                id = opcao.get_id()
                ProfissionalView.excluir_Profissional(id)
                st.success("Profissional excluído com sucesso")
                time.sleep(2)
                st.rerun()