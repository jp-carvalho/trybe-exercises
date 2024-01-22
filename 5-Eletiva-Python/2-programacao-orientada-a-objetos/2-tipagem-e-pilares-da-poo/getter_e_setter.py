"""
from typing import Union


class Blender:
    def get_color(self) -> str:
        return self.__color.upper()

    def set_color(self, new_color: str) -> None:
        if new_color.lower() == "turquesa":
            raise ValueError("Não existe liquidificador turquesa")

        self.__color = new_color

    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: Union[float, int],
    ) -> None:
        # Observe que usamos o setter para já validarmos o primeiro valor
        self.set_color(color)
        self.price = price
        self.color = color
        self._power = power
        self._voltage = voltage
        self.__max_speed = 3


blender = Blender("Azul", 110, 127, 200)

# print(f"A cor atual é {blender.__color}")
# AttributeError: 'Blender' object has no attribute '__color'

print(f"A cor atual é {blender.get_color()}")
blender.set_color("Preto")
print(f"Após pintarmos, a nova cor é {blender.get_color()}")

"""

# ==========  EXEMPLO COM PROPERTY ======
from typing import Union


class Blender:
    AVALIABLE_COLORS = {"VERMELHO", "ROSA", "PRETO", "BRANCO"}

    # Getter
    @property
    def color(self) -> str:
        return self.__color.upper()

    @color.setter  # repare que é color.setter e não property.setter
    def color(self, new_color: str) -> None:
        if new_color.upper() not in self.AVALIABLE_COLORS:
            raise ValueError(f"A cor '{new_color}' não está disponível")

        self.__color = new_color

    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: Union[float, int],
    ) -> None:
        # Observe que usamos o setter para validar o primeiro valor:
        # usando o self.color, que chama o setter, e não self.__color
        # que manipula o atributo
        self.color = color

    # demais variáveis omitidas no exemplo


blender = Blender("Rosa", 110, 127, 200)

print(blender.color)
blender.color = "Vermelho"
print(blender.color)
