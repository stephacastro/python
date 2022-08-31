'''
Formatando valores com modificadores
:s - texto (strings)
:d - inteiros (int)
:f numero de ponto flutuante (float)
:.(numero)f - quantiade de casas decimais (float) :.2f
:(caractere)(> ou < ou ^)(quantidade)(tipo - s, d- ou f)
> - esquerda
< - direita
^ - centro
'''

num1 = 10
num2 = 3
div = num1 / num2
print('{:.2f}'.format(div))

nome = 'Ste'
sobrenome = 'Castro'
num = 45
print(f'{nome:s}')
print(f'{num:d}')
print('{n:@^40}'.format(n=nome))
# acessando por indice
print('{1:@^40}'.format(nome, sobrenome))

print(nome.upper()) # tudo maiusculo
print(nome.lower()) # tudo minusculo
print(nome.title()) # primeiras letras maiusculas

num3 = 1
print(f'{num3:0<10}')
print(f'{num3:0>10}')
print(f'{num3:0^10}')

print(f'{num3:2f}')