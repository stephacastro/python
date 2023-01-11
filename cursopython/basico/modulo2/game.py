""" Jogo da forca """

def jogar():
    print('*'*40)
    print('*** Bem vindo ao Jogo da Forca! ***')
    print('*'*40)

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input('Qual letra? ').strip()

        index = 0

        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print(f"Encontrei a letra {chute} na posição {index}")
            
            index = index + 1


        print('jogando...')




    print('Fim do Jogo')

if (__name__ == "__main__"):
    jogar()
