from typing import Union


class Blender:
    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: Union[float, int],
    ) -> None:
        self.price = price
        self.color = color
        self._power = power
        self._voltage = voltage
        self.__max_speed = 3
        self.turn_off()

    def turn_on(self, speed: int) -> None:
        self.__is_on = True
        self.speed = speed if speed <= self.__max_speed else self.__max_speed

    def turn_off(self) -> None:
        self.__is_on = False
        self.__speed = 0

    def is_on(self) -> bool:
        return self.__is_on
