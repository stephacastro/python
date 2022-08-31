"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)
idade = int(input('Qual sua idade: '))
salario = float(input('Qual o seu salário: '))
sexo = input("Sexo? 'F' ou 'M': ")
estado_civil = input("Estado Civil 's', 'c', 'v', 'd': ")

if tamanho_nome > 3:
    print('Nome válido!')
elif idade < 150:
    print('Idade válido!')

