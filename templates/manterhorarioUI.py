import streamlit as st
import pandas as pd
from views import HorarioView, ClienteView, ServicoView, ProfissionalView
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1: ManterHorarioUI.listar()
        with tab2: ManterHorarioUI.inserir()
        with tab3: ManterHorarioUI.atualizar()
        with tab4: ManterHorarioUI.excluir()

    def listar():
        horarios = HorarioView.listar_horario()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dicionario = []
            for obj in horarios:
                cliente = ClienteView.listar_id_cliente(obj.get_id_cliente())
                servico = ServicoView.listar_id_servico(obj.get_id_servico())
                profissional = ProfissionalView.listar_id_profissional(obj.get_id_profissional())

                if cliente != None:
                    cliente = cliente.get_nome()
                if servico != None:
                    servico = servico.get_descricao()
                if profissional != None:
                    profissional = profissional.get_nome()

                dicionario.append({"id": obj.get_id(), "data": obj.get_data(),
                "confirmado": obj.get_confirmado(), "cliente": cliente, 
                "servico": servico, "profissional": profissional})

            df = pd.DataFrame(dicionario)
            st.dataframe(df)

    def inserir():
        clientes = ClienteView.listar_cliente()
        servicos = ServicoView.listar_servico()
        profissionais = ProfissionalView.listar_profissional()

        data = st.text_input("Informe a data e o horário do serviço", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        cliente = st.selectbox("Informe o cliente:", clientes, index=None)
        servico = st.selectbox("Informe o serviço:", servicos, index=None)
        profissional = st.selectbox("Informe o profissional:", profissionais, index=None)


        # Talvez haja erro aqqq
        if st.button("Inserir"):
            id_cliente = None
            id_servico = None
            id_profissional = None
            if cliente != None:
                id_cliente = cliente.get_id()
            if servico != None:
                id_servico = servico.get_id()
            if profissional != None:
                id_profissional = profissional.get_id()
            
            HorarioView.inserir_horario(datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
            st.success("Horário inserido com sucesso")

            time.sleep(2)
            st.rerun()

    def atualizar():
        horarios = HorarioView.listar_horario()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")       
        else:
            clientes = ClienteView.listar_cliente()
            servicos = ServicoView.listar_servico()
            profissionais = ProfissionalView.listar_profissional()
            opcao = st.selectbox("Atualização de Horários", horarios)
            data = st.text_input("Informe a nova data e horário do serviço",
                opcao.get_data().strftime("%d/%m/%Y %H:%M"))
            confirmado = st.checkbox("Nova confirmação", opcao.get_confirmado())

            if opcao.get_id_cliente() in [0, None]:
                id_cliente = None
            else:
                id_cliente = opcao.get_id_cliente()
            if opcao.get_id_servico() in [0, None]:
                id_servico = None
            else:
                id_servico = opcao.get_id_servico()
            if opcao.get_id_profissional() in [0, None]:
                id_profissional = None
            else:
                id_profissional = opcao.get_id_profissional()
        
            #id_servico...
            cliente = st.selectbox("Informe o novo cliente:", clientes, next((i for i, c in enumerate(clientes) if c.get_id() == id_cliente), None))
            servico = st.selectbox("Informe o novo serviço:", servicos, next((i for i, s in enumerate(servicos) if s.get_id() == id_servico),  None))
            profissional = st.selectbox("Informe o novo profissional:", profissionais, next((i for i, p in enumerate(profissionais) if p.get_id() == id_profissional), None))
            if st.button("Atualizar"):
                id_cliente = None
                id_servico = None
                id_profissional = None
                if cliente != None:
                    id_cliente = cliente.get_id()
                if servico != None:
                    id_servico = servico.get_id()
                if profissional != None:
                    id_profissional = profissional.get_id()
                HorarioView.atualizar_horario(opcao.get_id(), datetime.strptime(data, "%d/%m/%Y %H:%M"), confirmado, id_cliente, id_servico, id_profissional)
                st.success("Horário atualizado com sucesso")


    def excluir():
        horarios = HorarioView.listar_horario()
        if len(horarios) == 0: 
            st.write("Nenhum horário cadastrado")
        else:
            opcao = st.selectbox("Exclusão de horários", horarios)
            if st.button("Excluir"):
                HorarioView.excluir_horario(opcao.get_id())
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()


    def listar_horarios_cliente(id_cliente):
        horarios = HorarioView.listar_horario()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dicionario = []
            for obj in horarios:
                if obj.id_cliente() == id_cliente:
                    cliente = ClienteView.listar_id_cliente(obj.get_id_cliente())
                    servico = ServicoView.listar_id_servico(obj.get_id_servico())
                    profissional = ProfissionalView.listar_id_profissional(obj.get_id_profissional())

                    if cliente != None:
                        cliente = cliente.get_nome()
                    if servico != None:
                        servico = servico.get_descricao()
                    if profissional != None:
                        profissional = profissional.get_nome()

                    dicionario.append({"id": obj.get_id(), "data": obj.get_data(),
                "confirmado": obj.get_confirmado(), "cliente": cliente, 
                "servico": servico, "profissional": profissional})

            df = pd.DataFrame(dicionario)
            st.dataframe(df)