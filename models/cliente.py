# a pasta models tem entidades e DAOs
import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__senha = senha

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"
    
    # SETS E GETS
    def set_id(self, id): 
        self.__id = id
    def set_nome(self, nome): 
        self.__nome = nome
    def set_email(self, email): 
        self.__email = email
    def set_fone(self, fone): 
        self.__fone = fone
    def set_senha(self, senha)
        self.__senha = senha

    def get_id(self):
        return self.__id
    def get_nome(self): 
        return self.__nome
    def get_email(self): 
        return self.__email
    def get_fone(self): 
        return self.__fone
    def get_senha(self):
        return self.__senha
    # FIM DOS SETS E GETS

    # JSON
    def to_json(self):
        dic = {"id":self.__id, "nome":self.__nome, "email":self.__email, "fone":self.__fone, "senha": self.__senha}
        return dic

    # por que @staticmethod? pesquisar...
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

# CRUD
class ClienteDAO:
    # talvez de problema no underliine (adicionei oto agr)
    __objetos = []

    # abrir e salvar são os métodos mais importantes?
    @classmethod
    def abrir(cls):
        # por que encapsular esse?
        cls.__objetos = []
        try:
            with open("cliente.json", mode="r") as arquivo:
                lista_dicionario = json.load(arquivo)
                for dicionario in lista_dicionario:
                    objeto = Cliente.from_json(dicionario)
                    cls.__objetos.append(objeto)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("cliente.json", mode="w") as arquivo:
            json.dump(cls.__objetos, arquivo, default = Cliente.to_json)


    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0

        for cliente in cls.__objetos:
            if cliente.get_id() > id:
                id = cliente.get_id()

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
    def atualizar(cls, obj):
        cliente = cls.listar_id(obj.get_id())
        if cliente != None:
            cls.__objetos.remove(cliente)
            cls.__objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cliente = cls.listar_id(obj.get_id())
        if cliente != None:
            cls.__objetos.remove(cliente)
            cls.salvar()

    
