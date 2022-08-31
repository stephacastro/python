"""
Faça um programa que mostre as tabuadas dos números de 1 a 10 usando laços de repetição.
"""

for v1 in range(1, 11):
    print()
    for v2 in range(1, 11):
        resultado = v1 * v2
        print(f'{v1} x {v2} = {resultado}')

