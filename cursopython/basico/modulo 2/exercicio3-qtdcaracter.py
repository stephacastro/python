"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"
se tiver entre 5 e 6 letras escreva "Seu nome é normal", maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Qual o seu primeiro nome? ')
qtd = len(nome)

if len(nome) <= 4:
    print(f'Seu nome é curto, possui {qtd} letras.')
elif len(nome) >= 5 and len(nome) <= 6:
    print(f'Seu nome é normal, possui {qtd} letras.')
else:
    print(f'Seu nome é muito grande, possui {qtd} letras.')
