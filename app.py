# Lucas Gadonski e Cristian Domingues

import logging
import os

log_filename = 'app.log'
log_format = '%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG, 
    format=log_format
)

logger = logging.getLogger()

def main():
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

if __name__ == '__main__':
    main()

if os.path.exists(log_filename):
    print(f"Logs foram salvos em '{log_filename}'.")
else:
    print("Erro ao criar o arquivo de log.")
