
nome = input('Qual o seu nome? ')

# ao invés disso
if nome:
    print(nome)
else:
    print('Você não digitou nada =(')

# use isto
print(nome or 'Você não digitou nada =(')

# para na primeira condição verdadeira
print(nome or None or False or 0 or 'Você não digitou nada =(')