#!/usr/bin/env python3
"""
Faça um programa de terminal que exibe ao usuário uma listas dos quartos
disponíveis para alugar e o preço de cada quarto, esta informação está
disponível em um arquivo de texto separado por vírgulas
`quartos.txt`
# codigo, nome, preco
1,Suite Master,500
2,Quarto Familia,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
e a quantidade de dias e no final exibe o valor estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservas.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
mensagem informando que já está reservado.
"""
import sys
import logging

log = logging.Logger(__name__)

ocupados = {}
try:
    for line in open("reservas.txt"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": int(dias)
        }
except FileNotFoundError:
    log.error("reservas.txt não existe")
    sys.exit(1)


nome = input("Nome: ")

quartos = {}
try:
    for line in open("quartos.txt"):
        codigo, nome_quarto, preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome_quarto,
            "preco": float(preco), # TODO: Decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    log.error("Arquivo não existe")
    sys.exit(1)
    
if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(1)

for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = dados["preco"]
    disponivel = "❌" if not dados["disponivel"] else "👍🏻"
    # TODO: substituir casa decimal com vírgula
    print(f"{codigo} - {nome_quarto} - R${preco:.2f} - {disponivel}")

try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado.")
        sys.exit(1)
    dias = int(input("Dias: ").strip())
except ValueError:
    log.error("Digite um número válido")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe.")

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = preco_quarto * dias

# print(",".join([nome, str(num_quarto), str(dias)])) # opção válida também
with open("reservas.txt", "a") as file_:
    file_.write(f"{nome},{num_quarto},{dias}\n")

print(f"{nome}, você escolheu o quarto {nome_quarto} e vai custar: R${total:.2f}")

"""
name = input("Nome: ")
try:
    room_number = int(input("Número do quarto: ").strip())
    if quartos[room_number]
    days = int(input("Dias: ").strip())
except ValueError:
    log.error("Digite um número válido")
    sys.exit(1)
"""

