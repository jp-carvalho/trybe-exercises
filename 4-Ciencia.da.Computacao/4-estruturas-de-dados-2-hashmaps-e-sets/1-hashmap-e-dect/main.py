# arquivo responsável por imprimir resultados (videos_example.py)

# EXERCÍCIO 01
# ENDEREÇO ABAIXO NÃO FUNCIONA POR CAUSA DO NOME DA PASTA
from 1-hashmap-e-dect.videos_examples import count

nums = [3, 2, 5, 4, 1, 2, 3, 1, 3, 4, 1]

print(count(nums))


# EXERCÍCIO 02
from 1-hashmap-e-dect.videos_examples import screening

text = ['Ana', 'ama', 'Joao', 'que', 'ama', 'Jose', 'mais', 'Jose', 'nao', 'ama', 'Ana']

for key, value in screening(text).items():
    print(f"{key}: {value}")


# EXERCÍCIO 03
from 1-hashmap-e-dect.videos_examples import intersection

listA = [1, 2, 3, 4, 5, 6]
listB = [4, 5, 6, 7, 8, 9]

print(intersection(listA, listB))