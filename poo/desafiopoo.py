class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        pass

    def isAdult(self):
        pass


class Vendedor(Pessoa):
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.compras = []
