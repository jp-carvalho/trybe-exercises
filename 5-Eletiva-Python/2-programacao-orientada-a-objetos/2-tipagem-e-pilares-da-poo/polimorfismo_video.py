class Animal:
    def se_mover(self):
        return f"O animal está se movendo"


class Gato(Animal):
    def se_mover(self):
        movimento = super().se_mover()
        return f"{movimento} numa velocidade incrível"


class Golfinho(Animal):
    def se_mover(self):
        movimento = super().se_mover()
        return f"{movimento} dentro dos oceanos"


class Morcego(Animal):
    def se_mover(self):
        movimento = super().se_mover()
        return f"{movimento} na escuridão da noite"


animal = Animal()
gato = Gato()
golfinho = Golfinho()
morcego = Morcego()

print(animal.se_mover())
print(gato.se_mover())
print(golfinho.se_mover())
print(morcego.se_mover())
