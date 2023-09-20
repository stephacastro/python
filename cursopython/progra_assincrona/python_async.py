# Para tarefas que exigem muito processamento de CPU como essa de contagem de cores 
# a progra assin não é a ideal e sim multiprocessing 
# Progra assin é indicada em tarefas que fazem leitura de dados, banco de dados, acessando api e etc...

import datetime 
import math
import asyncio

def main():
    print('Realizando o processamento matemático de forma assincrona...')

    el = asyncio.get_event_loop()

    inicio = datetime.datetime.now()

    el.run_until_complete(computar(inicio=1, fim=50_000_000))

    tempo = datetime.datetime.now() - inicio
    
    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')

async def computar(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))

if __name__ == '__main__':
    main()

"""
Terminou em 8.44 segundos.
"""