import timeit


# # Função de busca linear em uma lista
# def busca_linear(lista, alvo):
#     for i, item in enumerate(lista):
#         if item == alvo:
#             return i
#     return -1


# # Lista de exemplo
# lista_linear = list(range(1, 10001))
# alvo_linear = 5000

# # Cria um Timer para medir o tempo de execução da busca linear
# tempo_linear = timeit.Timer(lambda: busca_linear(lista_linear, alvo_linear))

# # Executa a busca linear e imprime o tempo médio de execução em milissegundos
# tempo_medio_linear = tempo_linear.timeit(number=1000)  # Executa 1000 vezes
# print(f"Tempo médio da busca linear: {tempo_medio_linear * 1000:.6f} ms")


# # Função de busca binária em uma lista ordenada
# def busca_binaria(lista, alvo):
#     inicio = 0
#     fim = len(lista) - 1

#     while inicio <= fim:
#         meio = (inicio + fim) // 2
#         if lista[meio] == alvo:
#             return meio
#         elif lista[meio] < alvo:
#             inicio = meio + 1
#         else:
#             fim = meio - 1

#     return -1


# # Lista de exemplo (deve estar ordenada para a busca binária)
# lista_binaria = list(range(1, 10001))
# alvo_binario = 5000

# # Cria um Timer para medir o tempo de execução da busca binária
# tempo_binario = timeit.Timer(
#     lambda: busca_binaria(lista_binaria, alvo_binario)
# )

# # Executa a busca binária e imprime o tempo médio de execução em milissegundos
# tempo_medio_binario = tempo_binario.timeit(number=1000)  # Executa 1000 vezes
# print(f"Tempo médio da busca binária: {tempo_medio_binario * 1000:.6f} ms")


def BuscaLinear(lista, elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return elemento


def BuscaBinaria(lista, alvo):
    primeiro = 0
    ultimo = len(lista) - 1
    index = -1
    while (primeiro <= ultimo) and (index == -1):
        meio = (primeiro + ultimo) // 2
        if lista[meio] == alvo:
            index = meio
        else:
            if alvo < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio - 1
    return index


lista_mil = list(range(1, 1001))


alvo_mil = lista_mil[-1] * 0.9


print(
    ">>> Tempo de execução LINEAR em 1000 elementos"
    + str(timeit(lambda: BuscaLinear(lista_mil, alvo_mil), number=1))
)
print(
    ">>> Tempo de execução BINÁRIA em 1000 elementos"
    + str(timeit(lambda: BuscaBinaria(lista_mil, alvo_mil), number=1))
)
