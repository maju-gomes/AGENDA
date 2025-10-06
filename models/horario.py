from datetime import datetime
import json

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_cliente(0)
        self.set_id_servico(0)
        self.set_id_profissional(0)
        

    def set_id(self, id):
        self.__id = id
    def set_data(self, data):
        self.__data = data
    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado
    def set_id_cliente(self, id_cliente):
        self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico):
        self.__id_servico = id_servico
    def set_id_profissional(self, id_profissonal):
        self.__id_profissional = id_profissonal

    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data
    def get_confirmado(self):
        return self.__confirmado
    def get_id_cliente(self):
        return self.__id_cliente
    def get_id_servico(self):
        return self.__id_servico
    def get_id_profissional(self):
        return self.__id_profissional
    

    def to_json(self):
        dicionario = {"id": self.__id, "data": self.__data.strftime("%d/%m/%Y %H:%M"), "confirmado": self.__confirmado, "id_cliente": self.__id_cliente, "id_servico": self.__id_servico, "id_profissional": self.__id_profissional}
        return dicionario

    @staticmethod
    def from_json(dicionario):
        horario = Horario(dicionario["id"], datetime.strptime(dicionario["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dicionario["confirmado"])
        horario.set_id_cliente(dicionario["id_cliente"])
        horario.set_id_servico(dicionario["id_servico"])
        horario.set_id_profissional(dicionario["id_profissional"])
        return horario
    
    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"

class HorarioDAO:
    __objetos = []

    # operações realizadas com arquivo json
    @classmethod
    def abrir(cls):
        cls.__objetos = []

        try:
            with open("horario.json", mode="r") as arquivo:
                lista_dicionario = json.load(arquivo)
                for dicionario in lista_dicionario:
                    objeto = Horario.from_json(dicionario)
                    cls.__objetos.append(objeto)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horario.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Horario.to_json)
    # fim das operações realizadas com json

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for horario in cls.__objetos:
            if horario.get_id() > id:
                id = horario.get_id()

        obj.set_id(id + 1)
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id: 
                return obj
        return None

    @classmethod
    def atualizar(cls, horario):
        obj = cls.listar_id(horario.get_id())
        if horario != None:
            cls.__objetos.remove(obj)
            cls.__objetos.append(horario)
            cls.salvar()

    @classmethod
    def excluir(cls, horario):
        obj = cls.listar_id(horario.get_id())
        if obj != None:
            cls.__objetos.remove(obj)
            cls.salvar()

