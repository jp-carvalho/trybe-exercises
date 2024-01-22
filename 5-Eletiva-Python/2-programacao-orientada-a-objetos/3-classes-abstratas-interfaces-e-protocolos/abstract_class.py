from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def name(self) -> None:
        pass


class Seller(Person):
    def __init__(self, your_name: str) -> None:
        self.your_name = your_name

    def name(self) -> None:
        print(f"Seu nome é {self.your_name}")


# ======= COM SUPER ======================


class X(ABC):
    @abstractmethod
    def example(self) -> None:
        print("Classe-base abstrata")


class Y(X):
    def example(self) -> None:
        super().example()
        print("Subclasse")


z = Y()
z.example()


# ======= @property =================


class TestClass(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name
