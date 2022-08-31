"""
Listas em python
Fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
# lista = [1, 2, 3, 4]
# lista2 = ['a', 'b', 'c', 'd', 'e', 10]
# lista3 = ['ste', 21]
#
# #acessando o valor a
# print(lista2[0])
# #acessando o ultimo valor
# print(lista2[-1])
#
# print(lista3)
#
# #modificando o valor de um indice na lista
# lista[3] = 'alterado'
# print(lista)
#
# #fateamento em listas
# print(lista[::2])
# print(lista2[:3])
# print(lista2[2:])
# print(lista2[-1])


# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l2)
# # extend extende valores de outra lista
# l1.extend(l2)
#
# #append add um novo valor no final da lista
# l2.append('ste')
#
# #insert add um valor no lugar que você que na lista
# l2.insert(0, ['castro'])
# print(l2)
#
# # pop deleta um elemento do final da lista
# l2.pop()
# print(l2)

# descobrindo o tipo dos elementos com o for
l2 = ['string', True, 10, 10.0]
for elemento in l2:
    print(f'O tipo do elemento é {type(elemento)} e o seu valor é {elemento}')
