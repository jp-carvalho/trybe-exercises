class Rectangle:
    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> int:
        return self.base * self.height

    def calculate_perimeter(self) -> int:
        return 2 * (self.base + self.height)


rectangle = Rectangle(5, 10)
print("Área: ", rectangle.calculate_area())
print("Perímetro: ", rectangle.calculate_perimeter())
