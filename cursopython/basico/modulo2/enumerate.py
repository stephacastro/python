"""
Enumerate -  enumerar elementos da lista #list
"""
    # indice 0       1       2
lista = [['Ste', 'Manu', 'Ana'],  # indide 0
         ['Maria', 'Edu', 'João'],  # indide 1
         ['Fê', 'Isa', 'Tati']]  # indide 2

print(lista[1][2])


enumerada = enumerate(lista)
print(list(enumerada))  # transformando o objeto enumerate em lista (type cast)

