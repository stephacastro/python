# abstraindo de fato

from concurrent.futures.thread import ThreadPoolExecutor as Executor
#from concurrent.futures.process import ProcessPoolExecutor as Executor

import time 

def processar():       # imprime mesmo que a tarefa esteja em execução
    print('[', end='', flush=True)
    for _ in range(1,11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)

    return 42

if __name__ == '__main__':
    with  Executor() as executor:
        future = executor.submit(processar)

    print(f'\nO retorno foi: {future.result()}')