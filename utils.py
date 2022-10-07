import prefect
import re
import os

def log(message) -> None:
    """Logs a message"""
    prefect.context.logger.info(f"\n{message}")

def limpaNumero(numero):
    numero =  (re.sub('[^0-9]+', '', numero))
    return format(int(numero[:-1]), ",").replace(",", "-") + numero[-1]

def criaCaminho(caminhoSaida):
    existe = os.path.exists(caminhoSaida)
    if not existe:
        os.makedirs(caminhoSaida)