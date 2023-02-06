#!/usr/bin/env python3
"""Cadastro de produto
"""
__version__ = "0.1.0"

from pprint import pprint

produto = {
    "nome": "Caneta",
    "cor": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "em_estoque": True,
    "codigo": 45678,
    "codebar": None,
}

cliente = {
    "nome": "Ayrton"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}


total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)
