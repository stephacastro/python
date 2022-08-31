"""
For - else
startswith() - checa se um valor da string comeã com determinada letra
lower() =  converte letra minisculo para maisculo
"""
variavel = ['Stephanie', 'Manu', 'Ana']

for valor in variavel:
    if valor.startswith('S'):
        print('Começa com S', valor)
    else:
        print('Não começa com S', valor)


for valor in variavel:
    print(valor)
    if valor.lower().startswith('s'):
        break
else:
    print('Não existe uma palavra que começa com S.')


for valor in variavel:
    if valor.lower().startswith('s'):
        continue
    print(valor)
