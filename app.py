import logging
import os

# Criação e configuração do logger
log_filename = 'app.log'
log_format = '%(asctime)s - %(levelname)s - %(message)s'

# Configuração básica do logger
logging.basicConfig(
    filename=log_filename,
    level=logging.DEBUG,  # Define o nível mínimo de log a ser registrado
    format=log_format
)

# Criação de um logger
logger = logging.getLogger()

# Função principal simulando algumas operações e gerando logs
def main():
    logger.debug('Este é um log de debug, util para diagnósticos detalhados.')
    logger.info('A aplicação iniciou com sucesso.')
    
    try:
        # Simulação de uma operação
        x = 10 / 2
        logger.info(f'Operação realizada com sucesso, resultado: {x}')
        
        # Simulação de uma operação que gera um warning
        if x > 4:
            logger.warning('O resultado e maior que o esperado, verifique os dados de entrada.')
        
        # Simulação de uma operação que gera um erro
        y = 10 / 0  # Isso gerará uma exceção
    except ZeroDivisionError as e:
        logger.error(f'Ocorreu um erro: {e}')
    
    try:
        # Simulação de um erro crítico
        data = None
        if data is None:
            raise ValueError('Os dados não foram carregados corretamente!')
    except ValueError as e:
        logger.critical(f'Erro crítico: {e}')

# Execução da função principal
if __name__ == '__main__':
    main()

# Verificação da existência do arquivo de log
if os.path.exists(log_filename):
    print(f"Logs foram salvos em '{log_filename}'.")
else:
    print("Erro ao criar o arquivo de log.")
