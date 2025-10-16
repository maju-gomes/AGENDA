import streamlit as st
import pandas as pd
from views import ClienteView, ServicoView, HorarioView, ProfissionalView

class HorarioClienteUI:
    def listar_horarios_cliente(id_cliente):
        horarios = HorarioView.listar_horario()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dicionario = []
            for obj in horarios:
                if obj.get_id_cliente() == id_cliente:
                    cliente = ClienteView.listar_id_cliente(obj.get_id_cliente())
                    servico = ServicoView.listar_id_servico(obj.get_id_servico())
                    profissional = ProfissionalView.listar_id_profissional(obj.get_id_profissional())

                    if cliente != None:
                        cliente = cliente.get_nome()
                    if servico != None:
                        servico = servico.get_descricao()
                    if profissional != None:
                        profissional = profissional.get_nome()

                    dicionario.append({"id": obj.get_id(), "data": obj.get_data(), "confirmado": obj.get_confirmado(), 
                                   "cliente": cliente, "servico": servico, "profissional": profissional})

            df = pd.DataFrame(dicionario)
            st.dataframe(df)