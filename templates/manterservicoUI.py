from views import ServicoView
import streamlit as st
import pandas as pd
import time


class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterServicoUI.listar()
        with tab2: ManterServicoUI.inserir()
        with tab3: ManterServicoUI.atualizar()
        with tab4: ManterServicoUI.excluir()

    def listar():
        servico = ServicoView.listar_servico()
        if len(servico) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            list_dic = []
            for obj in servico:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df)


    def inserir():
        descricao = st.text_input("Informe a descrição:")
        valor = st.text_input("Informe o valor:")

        if st.button("Inserir"):
            ServicoView.inserir_servico(descricao, valor)
            st.success("Serviço inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        servico = ServicoView.listar_servico()
        if len(servico) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            opcao = st.selectbox("Selecione o serviço que deseja atualizar:", servico)
            descricao = st.text_input("Nova descrição:", opcao.get_descricao())
            valor = st.text_input("Novo valor:", opcao.get_valor())
            if st.button("Atualizar"):
                id = opcao.get_id()
                ServicoView.atualizar_servico(id, descricao, valor)
                st.success("Serviço atualizado com sucesso")

    def excluir():
        servico = ServicoView.listar_servico()
        if len(servico) == 0:
            st.write("Nenhum serviço cadastrado")
        else:
            opcao = st.selectbox("Selecione on serviço que deseja excluir", servico)
            if st.button("Excluir"):
                id = opcao.get_id()
                ServicoView.excluir_servico(id)
                st.success("Serviço excluído com sucesso")

    