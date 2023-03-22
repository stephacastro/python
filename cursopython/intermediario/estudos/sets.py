# Sets  - conjuntos em Python (tipo set)
# Sets sçao mútaveis porem só aceitam tipos imutaveis 
# sets são iteraveis (for, in, not in)

s1 = set() # set vazio
s2 = set('Luiz') # set iteravel // pode não garantir a ordem dos elementos
s3 = {'Luiz', 1,2,3} # set com dados

# sets são eficientes para remover valores duplicados de iteraveis 
# seus valores sempre serão unicos
s4 = {1,2,3,3,3,3,3,1}
print(s4)

l1 = [1,2,3,3,3,3,3,1]
s4 = set(l1)
print(s4)

for numero in s4:
    print(numero)

# métodos uteis // add, updade, clear, discard
s4.add(4)
s4.update('Olá')
s4.clear() # limpa o set
s4.discard('Olá') #elimina valor

print(s4)