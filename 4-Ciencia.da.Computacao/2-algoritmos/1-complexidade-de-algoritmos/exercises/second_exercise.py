import random


def random_averages(n):
    list_of_averages = []

    for _ in range(
        100
    ):  # O underline serve para ignorar os numeros passados, assim não são armazenados em nenhum lugar
        average = 0
        for _ in range(n):
            average += random.randrange(
                1, n
            )  # gera numeros aleatórios entre 1 e N
        average = average / n
        list_of_averages.append(average)
    return list_of_averages
