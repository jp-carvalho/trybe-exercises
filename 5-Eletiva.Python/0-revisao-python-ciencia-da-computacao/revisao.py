# # definir constantes
# minha_variavel = "Oi, eu sou uma variável"


# # Condições
# age = 20

# if age >= 18:
#     print("You are an adult.")
# else:
#     print("You are a minor")


# # Loopings
# for i in range(5):
#     print("Iterarion", i)


# # Funções
# def greet(name):
#     return "Hello, " + name + "!"

# greeting = greet('Alice')
# print(greeting)


# O que são listas em Python
lista = [1,2,3,4]
lista_2 = list()
lista_2.append(2)
lista_nomes = ['JP'] * 5
lista_nomes_2 = ['JP'] * len(lista)
o = 5 * 'o'

print('===== LISTA =====')
print(lista)
print(lista_2)
print(lista_nomes)
print(lista_nomes_2)
print(o)


# Acessar elementos em uma lista
print('===== ACESSAR ELEMENTOS LISTA =====')
print(lista[2])

# O que é um dicionário (parecido com objeto em JS)
dicionario = {
    "name": "JP",
    "age": 39,
}

# Acessar elementos de um dicionário
print('===== ACESSAR ELEMENTOS DO DICIONARIO =====')
print(dicionario['name'])

# O que são Tuplas - São listas que não podem ser alteradas
tupla = ("JP", "39")

print('===== TUPLAS =====')
print(tupla)

# Como acessar algum item
print(tupla[0])


# Estruturas mais complexas:
# Lista de dicionário
lista_dict = [
    {"name": "Juão", "age": 39},
    {"name": "Afonso", "age": 19},
    { "name": "Marina", "age": 21}
]

dicionario_teste = lista_dict[0]

print('===== ACESSAR ELEMENTOS DA LISTA DE DICIONARIOS =====')
print(lista_dict[0])
print(lista_dict[0]["name"])

# confere se tem a chave name na posição 0
if "name" in dicionario_teste:
    print('Achei name')
    print(dicionario_teste['name'])

# outro modo para: confere se tem a chave age na posição 0
if dicionario_teste["age"]:
    print('Achei age')


# Lista de tuplas
lista_tuplas = [
    ("JP", "sad123"),
    ("Ana", "dsa456"),
    ("Tobias", "qwe123"),
    ("Marta", "ewq654"),
    ("Robertinho", "cde159"),
]

# Acesse um elemento na lista de tuplas
print('===== ACESSAR ELEMENTOS DA LISTA DE TUPLAS =====')
print(lista_tuplas[0])

# faz um for pela posição, no caso name é onde estão os nomes e password onde estão as senhas em cada tupla ("name", "password")
for name, password in lista_tuplas:
    print("name:", name)
    print("pass:", password)

# Criando ambiente virtual (no terminal):
'''
python3 -m venv .venv
source .venv/bin/activate
'''
