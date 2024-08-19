from loguru import logger
import requests

# Seu Customer Token do Loggly
CUSTOMER_TOKEN = "7ced1e71-c5a8-4343-9183-18d07579696a"

# URL do Loggly para o envio dos logs
LOGGLY_URL = f"https://logs-01.loggly.com/inputs/{CUSTOMER_TOKEN}/tag/python/"

# Função para enviar logs para o Loggly
def send_to_loggly(message):
    try:
        # A mensagem já é formatada pelo Loguru, então só enviamos o JSON
        requests.post(LOGGLY_URL, json={"message": message})
    except Exception as e:
        logger.error(f"Falha ao enviar log para Loggly: {e}")

# Configurando o Loguru para enviar logs para o Loggly
logger.add(lambda msg: send_to_loggly(msg), format="{message}", level="INFO")

# Exemplo de uso
logger.info("Este é um log de informação enviado para o Loggly.")
logger.warning("Este é um aviso enviado para o Loggly.")
logger.error("Este é um erro enviado para o Loggly.")