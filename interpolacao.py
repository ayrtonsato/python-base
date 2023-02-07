#!/usr/bin/env python3
__version__ = "0.1.1"

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("informe o nome do arquivo de emails")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes = []
for line in open(filepath):
    name, email = line.split(",")
    # TODO: substituir por envio de email
    print(f"Enviando email para: {email}")
    print(
        open(templatepath).read()
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "https://canetaazul.com.br",
            "quantidade": 1,
            "preco": 10.00,
        }
    )
    print("-" * 50)
