#!/usr/bin/env python3

nome = "Ayrton"

print("{:^11}".format(nome)) # 11 espaços para cada lado
print("{:>11}".format(nome)) # 11 espaços para esquerda
print("{:<11}".format(nome)) # 11 espaços para direita

msg = """Olá, {nome}!
Você é o player n {num:03d}
E você tem {ponto:.3f} pontos
"""

print(msg.format(nome=nome, num=2, ponto=299.0))

print(f"Olá, {nome}") # um syntax sugar para o str.format()

print("\N{panda face}") # imprime um emoji de um panda pelo nome
print("\U0001F372") # imprime um prato pelo código UNICODE
