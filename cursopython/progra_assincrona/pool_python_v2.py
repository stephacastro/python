import multiprocessing

def calcular(dado):
    return dado ** 2

def imprimir_nome_processo():              # pegando o nome do processo
    print(f'Iniciando o processo com nome {multiprocessing.current_process().name}')

def main():
    tamanho_pool = multiprocessing.cpu_count() * 2

    print(f'Tamanho da Pool {tamanho_pool}')
                                                        # para cada processo criado será executado a funçao imprimir_nome_processo
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close() #  pode executar / não há mais nenhuma execução para mapear 
    pool.join()

if __name__ == '__main__':
    main()