from functools import cache
from dataclasses import dataclass


# @cache
def fibonacci(n):
    if n <= 1:
        print("ativou")
        return n
    else:
        print("ativou")
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


@dataclass
class Person:
    name: str
    lastname: str


flavio = Person("Flávio", "Silva")
carlos = Person("Carlos", "Junior")

print(f"{flavio} e {carlos} possuem uma representação")
print(flavio != carlos)
