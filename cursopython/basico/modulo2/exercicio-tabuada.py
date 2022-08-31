"""
Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.
"""

while True:
    tabuada = int(input('Digite o número da tabuada que deseja: '))
    for valor in range(1, 11):
        resultado = valor * tabuada
        print(f'{tabuada} x {valor} = {resultado}')
        