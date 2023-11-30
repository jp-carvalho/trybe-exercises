class Animal:
    def __init__(self, nome: str, raca: str, pelagem: str) -> None:
        self.nome = nome
        self.raca = raca
        self.pelagem = pelagem

    def banho(self):
        pass

    def tosa(self):
        pass

    def unhas(self):
        pass


class Gato(Animal):
    def __init__(self, nome, raca, pelagem) -> None:
        super().__init__(nome, raca, pelagem)

    def banho(self):
        print(f"Dando banho no gato {self.nome}")

    def tosa(self):
        print(f"Tosando o gato {self.nome}")

    def unhas(self):
        print(f"Cortando as unhas do gato {self.nome}")


gato1 = Gato("Fedido", "SRD", "Longo")
gato1.banho()
gato1.tosa()
gato1.unhas()
