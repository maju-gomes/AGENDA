import json

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.__id = id
        self.__nome = nome
        self.__especialidade = especialidade
        self.__conselho = conselho
        self.__email = email
        self.__senha = senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__especialidade} - {self.__conselho} - {self.__email}"
    
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade
    def set_conselho(self, conselho):
        self.__conselho = conselho
    def set_email(self, email):
        self.__email = email
    def set_senha(self, senha):
        self.__senha = senha

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_especialidade(self):
        return self.__especialidade
    def get_conselho(self):
        return self.__conselho
    def get_senha(self):
        return self.__senha
    def get_email(self):
        return self.__email
    
    def to_json(self):
        dic = {"id": self.__id, "nome": self.__nome, "especialidade": self.__especialidade, "conselho": self.__conselho, "email": self.__email, "senha": self.__senha}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"], dic["conselho"], dic["email"], dic["senha"])
    
class ProfissionalDAO:
    __objetos = []

    # abrir e salvar são os métodos mais importantes?
    @classmethod
    def abrir(cls):
        # por que encapsular esse?
        cls.__objetos = []
        try:
            with open("profissional.json", mode="r") as arquivo:
                lista_dicionario = json.load(arquivo)
                for dicionario in lista_dicionario:
                    objeto = Profissional.from_json(dicionario)
                    cls.__objetos.append(objeto)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissional.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Profissional.to_json)


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0

        for profissional in cls.__objetos:
            if profissional.get_id() > id:
                id = profissional.get_id()

        obj.set_id(id + 1)

        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        try:
            with open("profissional.json") as arquivo:
                lista = json.load(arquivo)
        except FileNotFoundError:
            lista = []
        return [Profissional(**profissional) for profissional in lista]

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        profissional = cls.listar_id(obj.get_id())
        if profissional != None:
            cls.__objetos.remove(profissional)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        profissional = cls.listar_id(obj.get_id())
        if profissional != None:
            cls.__objetos.remove(profissional)
            cls.salvar()

    @classmethod
    def autenticar(cls, email, senha):
        for profissional in ProfissionalDAO.listar():
            if profissional.get_email() == email and profissional.get_senha() == senha:
                return profissional
        return None


    
