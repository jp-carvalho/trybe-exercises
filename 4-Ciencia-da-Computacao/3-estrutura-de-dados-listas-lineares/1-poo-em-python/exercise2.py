from collections import Counter
from typing import List


class Estatistica:
    def __init__(self, numbers: List[int]) -> None:
        self.numbers = numbers

    def media(self) -> float:
        return sum(self.numbers) / len(self.numbers)

    def mediana(self) -> float:  # mediana = valor que está no centro
        numbers = sorted(self.numbers)
        # retorna index central do elemento (divide o length por 2)
        index = (
            len(numbers) // 2
        )  # divisão inteira sem resto ( ex: 10/3 = 3, ignorando q sobra 1)
        if len(numbers) % 2 == 0:
            return (numbers[index - 1] + numbers[index]) / 2

        return numbers[index]

    def moda(self) -> int:  # valor que mais se repete em uma lista de numeros
        number, _ = Counter(self.numbers).most_common()[0]
        return number
