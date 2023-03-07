# Abstração: Capacidade de abstrair implementações
# Herança: Capacidade de herdar de outras classes
# Polimorfismo: Capacidade de uma
# implementação se comportar
# de maneira independente da forma do objeto

# Encapsulamento

class Conta:

    _tipo_de_conta = "corrente" # protegido / protected
    __id__interno = 456789 # Privado

    def __init__(self, cliente) -> None:
        self.cliente = cliente
        if self._tipo_de_conta == "corrente":
            self._saldo = 500

    def consultar(self):
        if self._saldo < 0:
            print("AVISO: Você está devendo...")
        return self._saldo

conta = Conta(cliente="Ayrton")
print(conta.consultar())
