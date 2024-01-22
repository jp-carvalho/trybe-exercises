class SerVivo:
    def __init__(self):
        self.idade = 0

    def faz_aniversário(self):
        self.idade += 1


class Animal(SerVivo):
    def __init__(self, especie: str, cor: str):
        super().__init__()
        self.especie = especie
        self.cor = cor

    def comer(self, comida: str):
        return f"O animal da especie {self.especie} está comendo {comida}"


class Cachorro(Animal):
    def __init__(self, cor: str, rabo_branco: bool, num_de_patas: int):
        # o super pede os parametros da classe pai
        super().__init__("Cachorro", cor)
        # adicionado os parametros da classe filha
        self.rabo_branco = rabo_branco
        self.num_de_patas = num_de_patas

    def latir(self):
        return "Au au!!!"


pacoca = Cachorro("Malhado", True, 4)
print(pacoca.latir())
print(pacoca.comer("ração"))
print(pacoca.idade)
pacoca.faz_aniversário()
print(pacoca.idade)
