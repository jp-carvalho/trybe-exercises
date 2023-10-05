from multiset import Multiset

print(Multiset())
print(Multiset("aeiou"))
print(Multiset({"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}))

conjunto_consoantes = set("qwrty")
print("conjunto: ", conjunto_consoantes)

conjunto_alfabeto = Multiset("aeiou") + conjunto_consoantes
print("Novo conjunto: ", conjunto_alfabeto)
print(type(conjunto_alfabeto))

# Frozensets podem ser entendiudas como sets imutáveis.
vogais = ("a", "e", "i", "o", "u")

conjunto_congelado = frozenset(vogais)
print("O conjunto congelado é:", conjunto_congelado)
print("O conjunto vazio é assim:", frozenset())
