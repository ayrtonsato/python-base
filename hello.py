#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da língua configurada no ambiente,
o programa exibe a mensagem correspondente.

Como usar:
Tenha a variável LANG devidademente configurada, ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
# metadados de um script python
# não é mandatório mas é um padrão adotado pela comunidade
# Dunder = double underscore __
__version__ = "0.1.2"
__author__ = "Ayrton Hiroshi Sato"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]

language_msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour Monde!",
}

print(language_msg.get(current_language, "Hello, World!"))
