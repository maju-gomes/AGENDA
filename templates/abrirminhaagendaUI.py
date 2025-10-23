from views import ClienteView, ServicoView, HorarioView, ProfissionalView
import streamlit as st
from datetime import datetime, timedelta

class AbrirMinhaAgendaUI:
    def main():
        st.header("Abrir Minha Agenda")

        d = st.text_input("Informe a data (dd/mm/aaaa)")
        h_i = st.text_input("Informe o horário de início (HH:MM)")
        h_f = st.text_input("Informe o horário final (HH:MM)")
        i_h = st.text_input("Informe o intervalo entre os horários (min)")

        if st.button("Abrir agenda"):
            try:
                data = datetime.strptime(d, "%d/%m/%Y")
                horario_inicial = datetime.strptime(h_i, "%H:%M")
                horario_final = datetime.strptime(h_f, "%H:%M")
                intervalo_horarios = int(i_h)

                horarios = []
                atual = horario_inicial
                while atual <= horario_final:
                    horarios.append(atual.strptime("HH:MM"))
                    atual += timedelta(minutes=intervalo_horarios)
                
                st.success("Horários cadastrados com sucesso")

            except:
                st.error("Verifique se os dados foram preenchidos corretamente")