# itens iguais ou de valor maior


def good_pairs(numbers):
    answer = 0
    i = 0
    size = len(numbers)
    # inicia um loop for que itera sobre os elementos da lista numbers de 0 a size - 1.
    for i in range(size):
        # inicia um loop for que itera sobre os elementos da lista numbers do índice i + 1 ao índice size - 1. Isso garante que nenhum par de elementos seja verificado duas vezes.
        for j in range(i + 1, size):
            if numbers[i] == numbers[j]:
                answer += 1
    return answer
