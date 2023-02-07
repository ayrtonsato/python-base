#!/usr/bin/env python3
"""Calculadora infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Ayrton Hiroshi Sato"

import sys

args = sys.argv[1:]

valid_operations = ("sum", "sub", "mul", "div")
operation = ""
nums = []
result = 0

if not args:
    operation = input("operação: ")
    nums = [input("n1: "), input("n2: ")]
elif len(args) != 3:
    print("Número de argumentos inválidos")
    sys.exit(1)
else:
    operation = args[0]
    nums = [args[1], args[2]]

if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Número inválid {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

# TODO: Usar dict de funcoes
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    result = n1 / n2
else:
    print("Operação inválida")
    sys.exit(1)

print(f"O resultado é {result}")
