class MonthlyExpense:
    def __init__(
        self,
        internet: float,
        grocery: float,
        power: float,
        water: float,
        rent: float,
    ) -> None:
        self.internet = internet
        self.grocery = grocery
        self._power = power
        self._water = water
        self.__rent = rent

    def get_power(self) -> float:
        return self._power

    def set_power(self, new_power: float) -> float:
        self._power = new_power

    def get_water(self) -> float:
        return self._water

    def set_water(self, new_water: float) -> float:
        self._water = new_water
