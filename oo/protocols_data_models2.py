# Protocols / Data Models
# Addible - __add__ / __radd__

print(1 .__add__(2))  # igual 1 + 2
print("Ayrton" + "Sato")
print([1, 2, 3] + [4, 5, 6])


class Cor:
    english_name = "color"
    icon = "◻️"

    def __str__(self):
        return f"{self.english_name} - {self.icon}"

    def __add__(self, other):
        mixtable = [
            ((Amarelo, Vermelho), Laranja),
            ((Azul, Amarelo), Verde),
            ((Vermelho, Azul), Violeta)
        ]
        for mix, result in mixtable:
            if isinstance(self, mix) and isinstance(other, mix):
                return result()


class Amarelo(Cor):
    english_name = "yellow"
    icon = "🟨"


class Azul(Cor):
    english_name = "blue"
    icon = "🟦"


class Vermelho(Cor):
    english_name = "red"
    icon = "🟥"


class Laranja(Cor):
    icon = "🟧"


class Verde(Cor):
    icon = "🟩"


class Violeta(Cor):
    icon = "🟪"


amarelo = Amarelo()
azul = Azul()
vermelho = Vermelho()

print(amarelo, azul, vermelho)
print("Cores secundárias")
print("Amarelo + Vermelho: ", amarelo + vermelho)
print("Azul + Amarelo: ", azul + amarelo)
print("Vermelho + Azul: ", vermelho + azul)
