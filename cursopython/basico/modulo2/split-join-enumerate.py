"""
split, join, enumerate em Python
split - dividir uma string (str)
join - juntar uma lista (str)
enumerate - enumerar elementos da lista (list) / objetos iteraveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."

# split - dividir uma string e gerar uma lista
# split(' ') separados pelo espaço
lista1 = string.split(' ')
lista2 = string.split(',') # separados pela virgula

# iterando na lista
for valor in lista1:
    print(valor)

# contando palavras
for valor in lista1:
    print(f' A palavra {valor} aparaceu {lista1.count(valor)}x na frase.')


palavra = ''
contagem = 0

for valor in lista1:
    qtd_vezes = lista1.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

for valor in lista2:
    print(valor.strip().capitalize())
    # strip - remove espaços no começo e no fim
    # capitalize - transforma a primeira letra em maiuscula


string2 = 'O Brasil é penta.'
lista = string2.split(' ')
string3 = ','.join(lista) # juntando e separando por virgula

print(string2)
print(lista)
print(string3)


string2 = 'O Brasil é penta.'
lista = string2.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])


# listas aninhadas - lista dentro de listas
lista = [[1, 2], [3, 4], [5, 6]]

for valor in lista:
    print(valor[0], valor[1])

