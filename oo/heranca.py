# Herança + Abstração
from abc import ABC

# super classe
class Fruit(ABC): # Classe abstrata / base
    kingdom = "vegetalia"

    def __init__(self, colors) -> None:
        self.colors = colors

class Food(ABC):
    price = 4.5

class Radioactive(ABC):
    power = 100

# derivadas (sub classes)
class Apple(Fruit): # herança em classe material
    image = "🍎"

minha_maca = Apple(colors=["green", "white"])
print(minha_maca.colors)
print(minha_maca.image)

class Watermelon(Fruit, Food, Radioactive): # Mixins
    image = "🍉"

minha_melancia = Watermelon(["green", "red", "black"])
print(minha_melancia.colors)
