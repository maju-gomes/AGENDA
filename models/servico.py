import json

class Servico:
    def __init__(self, id, descricao, valor):
        self.__id = id
        self.__descricao = descricao
        self.__valor = valor

    # SETS E GETS
    def set_id(self, id):
        self.__id = id
    def set_descricao(self, descricao):
        self.__descricao = descricao
    def set_valor(self, valor):
        self.__valor = valor

    def get_id(self): 
        return self.__id
    def get_descricao(self):
        return self.__descricao
    def get_valor(self):
        return self.__valor
    # FIM DOS SETS E GETS

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor}"

    # JSON
    def to_json(self):
        dicionario = {"id":self.__id, "descricao":self.__descricao, "valor":self.__valor}
        return dicionario

    # por que @staticmethod? pesquisar...
    @staticmethod
    def from_json(dicionario):
        return Servico(dicionario["id"], dicionario["descricao"], dicionario["valor"])
        

class ServicoDAO:
    __objetos = []

    @classmethod
    def abrir(cls):
        # por que encapsular esse?
        cls.__objetos = []
        try:
            with open("servico.json", mode="r") as arquivo:
                lista_dicionario = json.load(arquivo)
                for dicionario in lista_dicionario:
                    objeto = Servico.from_json(dicionario)
                    cls.__objetos.append(objeto)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servico.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Servico.to_json)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0

        for servico in cls.__objetos:
            if servico.get_id() >= id:
                id = servico.get_id()
        
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
    
    # ajustar
    @classmethod
    def atualizar(cls, obj):
        servico = cls.listar_id(obj.get_id())
        if servico != None:
            cls.__objetos.remove(servico)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        servico = cls.listar_id(obj.get_id())
        if servico != None:
            cls.__objetos.remove(servico)
            cls.salvar()