#!/usr/bin/env python3

import logging
import os

# BOILERPLATE
# TODO: usar função
# TODO: usar lib (loguru)
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
## nossa instância de logger
log = logging.Logger("logs.py", log_level)
# level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

"""
log.debug("Mensagem pro dev, qe, sysadmin")
log.info("Mensagem geral para usuarios")
log.warning("Aviso que nao causa erro")
log.error("Erro que afeta uma unica execução")
log.critical("Erro geral, ex: banco de dados sumiu")
"""


try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))
