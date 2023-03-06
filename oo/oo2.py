# Frutaria

class Fruit:
    """Represent a fruit"""
    def __init__(self, name, color) -> None:
        self.name = name
        self.color = color

apple = Fruit("Apple", "Red")
print(apple.name, apple.color)


banana = Fruit("Banana", "Yellow")
print(banana.name, banana.color)
