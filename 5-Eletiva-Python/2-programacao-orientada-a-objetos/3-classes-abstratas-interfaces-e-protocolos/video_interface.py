from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def nome(self):
        pass

    @abstractmethod
    def isade(self):
        pass

    @abstractmethod
    def sexo(self):
        pass

    @abstractmethod
    def altura(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, altura):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.altura = altura

    def nome(self):
        return self.nome

    def idade(self):
        return self.idade

    def sexo(self):
        return self.sexo

    def altura(self):
        return self.altura
