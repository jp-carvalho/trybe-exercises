class Employee:
    def calculate_salary(self) -> float:
        raise NotImplementedError(
            "Classes derivadas de Employee precisam implementar o cálculo de salário."
        )


class Analist(Employee):
    pass


a = Analist()
a.calculate_salary()
