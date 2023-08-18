import datetime as dt
import math

def main():
    inicio = dt.datetime.now()

    computar(fim=50_000_000)

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


""" Terminou em 7.681054 segundos. """