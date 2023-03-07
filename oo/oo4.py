# Carrinho de compras
from decimal import Decimal
from dataclasses import dataclass

produto = "Caneta"
valor = Decimal(4.5)
quantidade = 5
cliente_especial = True


def calcula_total(valor: Decimal, quantidade: int) -> Decimal:
    """Calcula valor total"""
    return valor * quantidade  # __mul__


if cliente_especial:
    valor = Decimal(4.3)
total = calcula_total(valor, quantidade)

print("Tipo: ", type(total))
print(f"O total é R${total:.2f}")


@dataclass
class Pessoa:
    pk: str
    name: str
    points: int


dados = Pessoa(pk="jo@do.com", name="Joe", points=10)
print(dados.name)
