# Lucas Gadonski e Cristian Domingues

import os
from loguru import logger
import requests

log_filename = 'app.log'
log_format = '%(asctime)s - %(levelname)s - %(message)s'


#Customer Token do Loggly
CUSTOMER_TOKEN = "7ced1e71-c5a8-4343-9183-18d07579696a"

# URL do Loggly para o envio dos logs
LOGGLY_URL = f"https://logs-01.loggly.com/inputs/{CUSTOMER_TOKEN}/tag/python/"

# Função para enviar logs para o Loggly
def send_to_loggly(message):
    try:
        requests.post(LOGGLY_URL, json={"message": message})
    except Exception as e:
        logger.error(f"Falha ao enviar log para Loggly: {e}")

# Configurando o Loguru para enviar logs para o Loggly
logger.add(lambda msg: send_to_loggly(msg), format="{message}")

logger.debug('Este é um log de debug, util para diagnósticos detalhados.')
logger.info('A aplicação iniciou com sucesso.')

try:
    x = 10 / 2
    logger.info(f'Operação realizada com sucesso, resultado: {x}')
    
    if x > 4:
        logger.warning('O resultado e maior que o esperado, verifique os dados de entrada.')
    
    y = 10 / 0 
except ZeroDivisionError as e:
    logger.error(f'Ocorreu um erro: {e}')

try:
    data = None
    if data is None:
        raise ValueError('Os dados não foram carregados corretamente!')
except ValueError as e:
    logger.critical(f'Erro crítico: {e}')


#Salvando Logs no arquivo app.log
if os.path.exists(log_filename):
    print(f"Logs foram salvos em '{log_filename}'.")
else:
    print("Erro ao criar o arquivo de log.")