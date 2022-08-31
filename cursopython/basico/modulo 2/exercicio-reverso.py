"""
Faça um programa que leia três valores (A, B, C) e mostre-os na ordem lida.
Em seguida, mostre-os em ordem crescente e decrescente.
"""

letra = 'A, B, C'

while letra == 'A, B, C':
    print(letra)
    print('')
    print(f'{letra} esta em ordem Crescente')
    if letra == 'A, B, C':
        print(f'{letra[::-1]} esta em ordem Decrescente')
    letra = 'D, E, F'
    