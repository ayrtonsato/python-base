#!/usr/bin/env python3
"""Alarme de temperatura
Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

temp maior que 30 e temp vezes 3 for maior ou igual a umidade:

    "ALERTA!!! 🥵♒ Perigo de calor úmido"

temp entre 10 e 30: "😀 Normal"

temp entre 0 e 10: "🥶 Frio"

temp <0: "ALERTA!!! ⛄ Frio Extremo."

ex:

python3 temp.py 
temperatura: 30
umidade: 90
... 
"ALERTA!!! 🥵 Perigo calor extremo"
"""
import sys
import logging

log = logging.Logger("alerta")

def ask_for(field: str) -> float:
    """
        Asks for a field
        and return the value prompted by the user
        as a float value.
    """
    try:
        field = float(input(field + ": ").strip())
        return field
    except ValueError:
        log.error(field + " inválida")
        sys.exit(1)    

temp = ask_for("Temperatura")
umidade = ask_for("Umidade")

if temp > 45:
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temp * 3 >= umidade:
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0:
    print("🥶 Frio")
elif temp < 0:
  	print("ALERTA!!! ⛄ Frio Extremo.")