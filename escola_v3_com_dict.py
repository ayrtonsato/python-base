#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala
que frenquentam cada uma das atividades.
"""
__version__ = "0.1.1"
__author__ = "Ayrton Hiroshi Sato"

# Dados
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

atividades = {
    "Inglês": ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "Música": ["Erik", "Carlos", "Maria"],
    "Dança": ["Gustavo", "Sofia", "Joana", "Antonio"]
}

# Listar alunos em cada atividade por sala
for nome_atividade, alunos in atividades.items():
    print(f"Alunos da atividade {nome_atividade}\n")

    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(sala1) & set(alunos)
    atividade_sala2 = set(sala2) & set(alunos)

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)
    print()
    print("#" * 50)

