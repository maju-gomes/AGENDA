from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime

class ClienteView:
    def listar_cliente():
        cliente = ClienteDAO.listar()
        cliente.sort(key = lambda obj: obj.get_nome())
        return cliente
    
    def listar_id_cliente(id):
        return ClienteDAO.listar_id(id)
    
    def inserir_cliente(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    def atualizar_cliente(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    def excluir_cliente(id):
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)

    def autenticar_cliente(email, senha):
        for cliente in ClienteView.listar_cliente():
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return {"id": cliente.get_id(), "nome": cliente.get_nome()}
        return None
        
    def criar_cliente_admin():
        for cliente in ClienteView.listar_cliente():
            if cliente.get_email() == "admin": return
        # aqui deve ter algo de errado... o cadastro de admins 
        ClienteView.inserir_cliente("admin", "admin", "fone", "1234")

class ServicoView:
    def listar_servico():
        servico = ServicoDAO.listar()
        servico.sort(key = lambda obj: obj.get_descricao())
        return servico

    def listar_id_servico(id):
        return ServicoDAO.listar_id(id)

    def inserir_servico(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir_servico(servico)

    def atualizar_servico(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)

    def excluir_servico(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)
    
class HorarioView:
    def inserir_horario(data, confirmado, id_cliente, id_servico, id_profissional):
        obj = Horario(0, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorarioDAO.inserir(obj)

    def listar_horario():
        horario = HorarioDAO.listar()
        horario.sort(key = lambda obj: obj.get_data())
        return horario
    
    def atualizar_horario(id, data, confirmado, id_cliente, id_servico, id_profissional):
        obj = Horario(id, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(obj)

    def excluir_horario(id):
        obj = Horario(id, None)
        HorarioDAO.excluir()

    # aqui o método tem parâmetros
    def horario_agendar_horario(id_profissional):
        horario = []
        agora = datetime.now()
        for hora in HorarioView.listar_horario():
            if hora.get_data() >= agora and hora.get_confirmado() == False and hora.get_id_cliente() == None and hora.get_id_profissional():
                horario.append(hora)
        horario.sort(key = lambda hora: hora.get_data())
        return horario

class ProfissionalView:
    def listar_profissional():
        profissional = ProfissionalDAO.listar()
        profissional.sort(key = lambda obj: obj.get_nome())
        return profissional
    
    def listar_id_profissional(id):
        return ProfissionalDAO.listar_id(id)
    
    def inserir_profissional(nome, especialidade, conselho, email, senha):
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissional)

    def atualizar_profissional(id, nome, especialidade, conselho, email, senha):
        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar()
    
    def excluir_cliente(id):
        profissional = Profissional(id, "", "", "", "")
        ProfissionalDAO.excluir(profissional)

    def autenticar_profissional(email, senha):
        for profissional in ProfissionalDAO.listar():
            if profissional.get_email() == email and profissional.get_senha() == senha:
                return {"id": profissional.get_id(), "nome": profissional.get_nome()}
        return None