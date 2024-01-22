from typing import Union


class HomeAppliance:
    def __init__(
        self, color: str, power: int, voltage: int, price: Union[float, int]
    ) -> None:
        self.color = color
        self.price = price
        self.power = power
        self.voltage = voltage
        self.max_speed = 3

        # Inicia os valores de `speed` e `is_on`
        # chamando o método `turn_off` direto no construtor
        self.turn_off()

    def turn_on(self, speed: int) -> None:
        self.is_on = True
        self.speed = speed if speed <= self.max_speed else self.max_speed

    def turn_off(self) -> None:
        self.is_on = False
        self.speed = 0


class Blender(HomeAppliance):
    pass


class Person:
    def __init__(self, name: str, account_balance: float) -> None:
        self.name = name
        self.account_balance = account_balance
        self.blender: Blender | None = None

    def buy_blender(self, blender: Blender) -> None:
        if blender.price <= self.account_balance:
            self.account_balance -= blender.price
            self.blender = blender


person = Person("Jacquin", 1000.0)
red_blender = Blender("red", 1000, 220, 350.0)
person.buy_blender(red_blender)
