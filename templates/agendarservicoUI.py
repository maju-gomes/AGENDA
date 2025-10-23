import streamlit as st
from views import ClienteView, ServicoView, HorarioView, ProfissionalView
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profissionais = ProfissionalView.listar_profissional()
        if len(profissionais) == 0:
            st.write("Nenhum profissional cadastrado")
        else:
            profissional = st.selectbox("Informe o profissional", profissionais)
            # aqui o método recebe argumento
            horarios = HorarioView.horario_agendar_horario(profissional.get_id())
        if len(horarios) == 0:
            st.write("Nenhum horário disponível")
        else:
            horario = st.selectbox("Informe o horário", horarios)
            servicos = ServicoView.listar_servico()
            servico = st.selectbox("Informe o serviço", servicos)
            if st.button("Agendar"):
                HorarioView.atualizar_horario(horario.get_id(), horario.get_data(), False, st.session_state["id_usuario"], servico.get_id(), profissional.get_id())
                st.success("Horário agendado com sucesso")
                time.sleep(2)
                st.rerun()

