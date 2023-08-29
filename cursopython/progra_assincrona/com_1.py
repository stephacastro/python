import multiprocessing
import random

def ping(conn):
    conn.send('Testando')

def pong(conn):
    msg = conn.recv() # receber o dado enviado
    print(f'{msg}.....')

def main():                         # ambos irão enviar e receber 
    conn1, conn2, = multiprocessing.Pipe(True)

    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()