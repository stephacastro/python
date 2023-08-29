import multiprocessing

def ping(queue):
    queue.put('Testando')

def pong(queue):
    msg = queue.get() # receber o dado enviado
    print(f'{msg} 123...')

def main():                         # ambos irão enviar e receber 
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()