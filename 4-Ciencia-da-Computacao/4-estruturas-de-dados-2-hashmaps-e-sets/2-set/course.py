class Conjunto:
    def __init__(self):
        self.set = [False] * 1001
        self.last_element = 0

    def add(self, item):
        if not self.set[item]:
            self.set[item] = True
        if item > self.last_element:
            self.last_element = item

    def __str__(self):
        string = "{"

        for index, is_in_set in enumerate(self.set):
            if is_in_set:
                string += str(index)
                if index < self.last_element:
                    string += ", "

        string += "}"
        return string

    def __contains__(self, item):
        return self.set[item]

    def union(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] or conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def intersection(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] and conjunto_b.set[index]:
                new_conjunto.add(index)

        return new_conjunto

    def difference(self, conjunto_b):
        new_conjunto = Conjunto()

        for index in range(1001):
            if self.set[index] and not conjunto_b.set[index]:
                new_conjunto.add(index)
        return new_conjunto

    def issubset(self, conjunto_b):
        for index in range(1001):
            if self.set[index] and not conjunto_b.set[index]:
                return False
        return True

    def issuperset(self, conjunto_b):
        for index in range(1001):
            if conjunto_b.set[index] and not self.set[index]:
                return False
        return True


if __name__ == "__main__":
    conj = Conjunto()
    for i in [0, 10, 100, 1000]:
        conj.add(i)
    print(conj)
    print(1 in conj)
    print(0 in conj)

    conj2 = Conjunto()
    for i in [1, 2, 3]:
        conj2.add(i)
    print(conj2)

    conj3 = Conjunto()
    for i in [7, 2, 10]:
        conj3.add(i)
    print(conj3)

    conj4 = Conjunto()
    print(conj4)

    # Union
    conj5 = Conjunto()
    for i in range(1, 11):
        conj5.add(i)

    conj6 = Conjunto()
    for i in range(10, 21):
        conj6.add(i)

    conj7 = conj5.union(conj6)
    print(conj7)

    # Intersection
    conj8 = Conjunto()
    for i in [1, 2, 3]:
        conj8.add(i)

    conj9 = Conjunto()
    for i in [7, 2, 10]:
        conj9.add(i)

    conj10 = conj8.intersection(conj9)
    print(conj10)

    # difference, issubset, issuperset
    conj1 = Conjunto()
    for i in [1, 2, 3]:
        conj1.add1

    conj2 = Conjunto()
    for i in [7, 2, 10]:
        conj2.add(i)

    conj3 = Conjunto()
    conj4 = conj1.union(conj2)

    print(conj1.issubset(conj4))
    print(conj4.issuperset(conj1))
    print(conj3.issubset(conj4))

    # EXERCICIO 7
    conj_estudantes = Conjunto()
    conj_lista1 = Conjunto()
    conj_lista2 = Conjunto()

    estudantes = [1, 2, 3, 4, 5, 6, 7]
    lista1_entregues = [1, 4, 7, 3]
    lista2_entregues = [3, 1, 6]

    for elem in estudantes:
        conj_estudantes.add(elem)

    for elem in lista1_entregues:
        conj_lista1.add(elem)

    for elem in lista2_entregues:
        conj_lista2.add(elem)

    print("Não entregaram a lista 1:", conj_estudantes.difference(conj_lista1))
    print("Já entregaram as 2 listas:", conj_lista1.intersection(conj_lista2))
    print(
        "Quem já entregou pelo menos uma lista:",
        conj_lista1.union(conj_lista2),
    )
    print(
        "Quem não entregou nenhuma:",
        conj_estudantes.difference(conj_lista1.union(conj_lista2)),
    )


# Exercício 8
def get_repeated(nums):
    seen_before = set()
    repeated = set()

    for num in nums:
        # se já foi adicionado no seen_before, adiciona no repeated
        if num in seen_before:
            repeated.add(num)
        else:
            # se não foi visto, adiciona no seen_before
            seen_before.add(num)

    return repeated


if __name__ == "__main__":
    nums = [1, 6, 3, 9, 6, 6, 3, -1, 4, 5, 7, 1]
    print(f"Repetidos: {get_repeated(nums)}")


# Exercício 9
def get_seven(nums):
    seen_before = set()
    lucky_rolls = []
    for roll in rolls:
        # checa se 7 menos o numero da iteração está em seen before, caso esteja, quer dizer que a soma é 7. Adiciona no lucky_rolls e depois apaga o numero utilizado da seen before
        if 7 - roll in seen_before:
            lucky_rolls.append((7 - roll, roll))
            seen_before.discard(7 - roll)
        else:
            seen_before.add()

    return lucky_rolls


if __name__ == "__main__":
    rolls = [5, 2, 1, 3, 2, 6, 1, 4, 2, 6, 2, 1, 1]

    print(get_seven(rolls))
