from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def presentation(self):
        pass


class Student_person(Person):
    def __init__(self, name, age, registration):
        super().__init__(name, age)
        self.registration = registration

    def presentation(self):
        print(
            f"Olá, meu nome é {self.name} e eu sou um aluno com matricula {self.registration}."
        )


class Specialist_person(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def presentation(self):
        print(
            f"Olá, meu nome é {self.name} e eu sou um professor com salário de {self.salary:.2f}."
        )


Student = Student_person("João", 25, "123456")
Specialist = Specialist_person("Cristiano", 35, 1000.00)

Student.presentation()
Specialist.presentation()
