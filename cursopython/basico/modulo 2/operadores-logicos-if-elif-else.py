"""
operadores logicos
and, or, not
in e not in
"""

nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))

idade_menor = 20
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} não pode pegar o empréstimo.')