"""
Faça um programa que verifique (usando if e else) se uma letra digitada
é “F” ou “M”. Conforme a letra escrever: F – Feminino, M- Masculino, Sexo inválido.
"""

sexo = input('Sexo [F/M]: ').upper()

if sexo == 'F':
    print(f'{sexo}-Feminino')
elif sexo == 'M':
    print(f'{sexo}-Masculino')
else:
    print('Sexo inválido')
