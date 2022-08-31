"""
Faça um programa para a leitura de duas notas parciais de um aluno.

A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Reprovado” se a média for menor de do que sete;
"""

n1 = int(input('1° nota: '))
n2 = int(input('2° nota: '))

media = (n1 + n2) / 2
print(media)

if media == 10:
    print('Aprovado com Distinção.')
elif media >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')

