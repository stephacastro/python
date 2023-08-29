import datetime as dt
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor 

def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} cores(s)...')

    inicio = dt.datetime.now()

    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for core in range(1, qtd_cores + 1):
            ini = 50_000_000 * (core - 1) / qtd_cores 
            fim = 50_000_000 * core / qtd_cores
            print(f'Core {core} processando de {ini} até {fim}...')
            executor.submit(computar, inicio=ini, fim=fim)

    tempo = dt.datetime.now() - inicio

    print(f"Terminou em {tempo.total_seconds():2f} segundos.")

def computar(fim, inicio=1):
    posicao = inicio
    fator = 1000 * 1000
    while posicao < fim:
        posicao += 1
        math.sqrt((posicao - fator) * (posicao - fator))

if __name__ == '__main__':
    main()

""" Terminou em 5.424263 segundos. """

""" Terminou em 1.609534 segundos """