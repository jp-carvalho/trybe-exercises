def shuffle(items):
    answer = []
    # calcula metade do comprimento da lista e armazena
    div_cards_by_two = len(items) // 2
    # itera sobre os elementos da lista items de 0 a div_cards_by_two - 1.
    for offset in range(div_cards_by_two):
        # adiciona os elementos da lista items do índice offset ao índice len(items) - 1 à lista answer, com um intervalo de div_cards_by_two. Isso garante que cada elemento da lista items seja adicionado à lista answer uma vez.
        answer.extend(items[offset::div_cards_by_two])
    return answer
