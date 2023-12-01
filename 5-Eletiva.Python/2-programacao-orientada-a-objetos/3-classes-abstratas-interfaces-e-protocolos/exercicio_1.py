from abc import ABC, abstractmethod


class Person(ABC):
    @abstractmethod
    def print_role(self) -> None:
        pass


class Seller(Person):
    def print_role(self) -> None:
        print("Meu cargo é de vendedor.")


class Manager(Person):
    def print_role(self) -> None:
        print("Meu cargo é de gerente")


seller = Seller()
seller.print_role()

manager = Manager()
manager.print_role()
