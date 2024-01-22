class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def description(self) -> None:
        pass

    def price(self) -> None:
        pass


class Book(Product):
    def __init__(self, name: str, author: str, price: float) -> None:
        super().__init__(name, price)
        self.author = author

    def description(self) -> str:
        return f"{self.name} por {self.author}"

    def price(self) -> float:
        return self.price


class DVD(Product):
    def __init__(self, name: str, direction: str, price: float) -> None:
        super().__init__(name, price)
        self.direction = direction

    def description(self) -> str:
        return f"{self.name} dirigido por {self.direction}"

    def price(self) -> float:
        return self.price


def print_details(product: Product) -> None:
    print(f"Descrição: {product.description()}")
    print(f"Preço: {product.price()}")


products = [
    Book("O Senhor dos Anéis", "J.R.R. Tolkien", 29.99),
    DVD("O Poderoso Chefão", "Francis Ford Coppola", 19.99),
]

for product in products:
    print_details(product)
