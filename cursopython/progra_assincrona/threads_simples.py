import threading  # passo 1
import time 

def main(): 
    th = threading.Thread(target=contar, args=('elefante', 10)) # passo 2

    th.start() # adiciona a thread na pool de theads prontas para execução   # passo 3
    
    print('Podemos fazer outras coisas no programa enquanto a thread vai executando...')
    print('Hello World ' * 2)

    th.join() # avisa para ficar aguardando aqui até a thread terminar a execução   # passo 4

    print("Pronto!!")

def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)

if __name__ == '__main__':
    main()