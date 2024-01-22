from typing import Protocol


class CalculatePerimeter(Protocol):
    def calculate_perimeter(self) -> str:
        pass


class Square(CalculatePerimeter):
    def __init__(self, side: int) -> None:
        self.side = side

    def calculate_perimeter(self) -> str:
        return f"O perímetro do quadrado é de {self.side * 4} cm"


class Triangle(CalculatePerimeter):
    def __init__(self, side1: int, side2: int, side3: int) -> None:
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self) -> str:
        return (
            f"O perímetro do triângulo é de {self.side1 + self.side2 + self.side3} cm"
        )


square = Square(5)
print(square.calculate_perimeter())

triangle = Triangle(5, 5, 5)
print(triangle.calculate_perimeter())
