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

try:
    temp = float(input("Temperatura: ").strip())
except ValueError:
    log.error("Temperatura inválida")
    sys.exit(1)
    
try:
    umidade = float(input("Umidade: ").strip())
except ValueError:
    log.error("Umidade inválida")
    sys.exit(1)

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