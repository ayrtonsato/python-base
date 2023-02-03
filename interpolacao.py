#!/usr/bin/env python3

template = """
Olá, %(nome)s

    Tem interesse em comprar %(produto)s?

    Este produto é ótimo para resolver
    %(texto)s

    Clique agora em %(link)s

    Apenas %(quantidade)d disponiveis!

    Preço promocional %(preco).2f
"""

clientes = ["Maria", "Joao", "Ayrton"]
produto = "caneta"
texto = "Escrever muito bem"
link = "https://canetaazul.com.br"
quantidade = 1
preco = 10.00

for cliente in clientes:
    print(
        template
        % {
            "nome": cliente,
            "produto": produto,
            "texto": texto,
            "link": link,
            "quantidade": quantidade,
            "preco": preco
        }
    )
