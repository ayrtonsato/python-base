# Protocols / Data Models
# Printable

class Cor:
    english_name = "color"
    icon = "◻️"

    def __str__(self):
        return f"{self.english_name} - {self.icon}"


class Amarelo(Cor):
    english_name = "yellow"
    icon = "🟨"


class Azul(Cor):
    english_name = "blue"
    icon = "🟦"


class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"


print("Cores primárias")
print(Amarelo())  # yellow - 🟨
print(Azul())  # blue - 🟦
print(Vermelho())  # red - 🟥
