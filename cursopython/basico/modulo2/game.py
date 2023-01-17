""" Jogo da forca """

import random

def jogar():
    imprime_boasvindas()
    palavra_secreta = carrega_palavra()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
   
# Condições para o jogo acontecer   
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)


    while(not enforcou and not acertou):

        chute = input('Qual letra? ').strip().upper()
        

        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:                                         
                if(chute == letra):
                    letras_acertadas[index] = letra    
                index = index + 1

        else:
            erros = erros + 1    

        enforcou = erros == 6 
        acertou = "_" not in letras_acertadas      
        print(letras_acertadas)

    if (acertou):
        print('Parabéns, Você ganhou!!!')
    else:
        print(f'Você perdeu! a palavra é {palavra_secreta}')
    
    print('Fim do Jogo')

def imprime_boasvindas():
    print('*'*40)
    print('*** Bem vindo ao Jogo da Forca! ***')
    print('*'*40)

def carrega_palavra():
    caminho = r'C:\python\cursopython\basico\modulo2'
    arquivo = open(f"{caminho}\palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta 

def inicializa_letras_acertadas(palavra_secreta):   
    return ["_" for letra in palavra_secreta]
    
jogar()