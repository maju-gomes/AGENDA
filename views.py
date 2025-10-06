from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO

class ClienteView:
    def listar_cliente():
        return ClienteDAO.listar()
    
    def listar_id_cliente(id):
        return ClienteDAO.listar_id(id)
    
    # para adicionar um cliente são obrigatórios os parâmetros
    def inserir_cliente(nome, email, fone):
        cliente = Cliente(0, nome, email, fone)
        ClienteDAO.inserir(cliente)
    
    def atualizar_cliente(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        ClienteDAO.atualizar(cliente)

    def excluir_cliente(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

class ServicoView:
    def listar_servico():
        return ServicoDAO.listar()
    
    def listar_id_servico(id):
        return ServicoDAO.listar_id(id)
    
    # para adicionar um cliente são obrigatórios os parâmetros
    def inserir_servico(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    
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
        return HorarioDAO.listar()
    
    def atualizar_horario(id, data, confirmado, id_cliente, id_servico, id_profissional):
        obj = Horario(id, data)
        obj.set_confirmado(confirmado)
        obj.set_id_cliente(id_cliente)
        obj.set_id_servico(id_servico)
        obj.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(obj)

    def excluir_horario(id):
        obj = Horario(id, None)
        HorarioDAO.excluir(obj)


class ProfissionalView:
    def listar_profissional():
        return ProfissionalDAO.listar()
    
    def listar_id_profissional(id):
        return ProfissionalDAO.listar_id(id)
    
    # para adicionar um cliente são obrigatórios os parâmetros
    def inserir_profissional(nome, especialidade, conselho):
        profissional = Profissional(0, nome, especialidade, conselho)
        ProfissionalDAO.inserir(profissional)
    
    def atualizar_profissional(id, nome, especialidade, conselho):
        profissional = Profissional(id, nome, especialidade, conselho)
        ProfissionalDAO.atualizar(profissional)

    def excluir_cliente(id):
        profissional = Cliente(id, "", "", "")
        ProfissionalDAO.excluir(profissional)