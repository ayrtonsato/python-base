# Abstração: Capacidade de abstrair implementações
# Herança: Capacidade de herdar de outras classes
# Polimorfismo: Capacidade de uma
# implementação se comportar
# de maneira independente da forma do objeto

# Encapsulamento: Capacidade de esconder/proteger
# atributos dentro da classe, publico, protegidas, privadas
from abc import ABC


class Conta(ABC):
    def __init__(self, cliente) -> None:
        self.cliente = cliente
        self._saldo = 500


class ContaCorrente(Conta):
    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo...")
        return self._saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, value):
        self._saldo += value


conta = ContaCorrente(cliente="Ayrton")
print(conta.consultar())
print(conta.saldo)
conta.saldo = 100
print(conta.saldo)
