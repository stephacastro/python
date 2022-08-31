"""
Faça um programa que pergunte a hora ao usuario e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
nome = input('Qual o seu nome: ')
hora = input('Digite um horário (0-23): ')

if hora.isdigit():
    hora = int(hora)
    if hora < 0 or hora > 23:
        print('Digite um horário entre 0 e 23.')
    if hora < 12:
        print(f'Bom dia {nome}')
    elif hora < 17:
        print(f'Boa tarde {nome}')
    else:
        print(f'Boa noite {nome}')
else:
    print('Por favor, digite um horário entre 0 e 23.')
