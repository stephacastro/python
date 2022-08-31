"""
For in
Iterando strings com for
função range(start=o, stop, step=1)
"""
# continue - pula para o proximo laço
# break - termina o laço


texto = 'Python'
nova_string = ''

for letra in texto:
    print(letra)

print()

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra
print(nova_string)

for numero in range(10):
    print(numero)

print()

for n in range(20,10,-1):
    print(n)

print()

for n in range(1, 11, 2):
    print(n)