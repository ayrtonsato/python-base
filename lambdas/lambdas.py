def transforma_em_maiusculo(texto):
    return texto.upper()


def transforma_em_minusculo(texto):
    return texto.lower()


def divide_por_2(numero):
    return numero // 2


def faz_algo(valor, funcao):
    print(f"Aplicando a {funcao} em {valor}")
    return funcao(valor)


# lambda
print(faz_algo(10, lambda numero: numero * 3))
print("-" * 50)

names = [
    "Giovani", "Bruno", "Joao", "Bernardo", "Gabriel", "Marcia",
]

print(sorted(names, key=len))
# usando lambda
print(sorted(names, key=lambda name: name.count("i")))
print(list(filter(lambda name: name[0].lower() == "b", names)))
print("-" * 50)

# Calculadora

operacao = input("Operação [sum, mul, div, sub]: ")
n1 = input("n1: ").strip()
n2 = input("n2: ").strip()

operacoes = {
    "sum": lambda a, b: a + b,
    "sub": lambda a, b: a - b,
    "mul": lambda a, b: a * b,
    "div": lambda a, b: a / b,
}

resultado = operacoes[operacao](int(n1), int(n2))
print(f"O resultado é : {resultado}")