
print('')
print('****** Responda com [S] para SIM ou [N] para NÃO ******\n\n')

pergunta1 = input('Telefonou para a vítima?\n').upper()
pergunta2 = input('Esteve no local do crime?\n').upper()
pergunta3 = input('Mora perto da vítima?\n').upper()
pergunta4 = input('Devia para a vítima?\n').upper()
pergunta5 = input('Já trabalhou com a vítima?\n').upper()

lista = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]

suspeita = 2
cumplice1 = 3 
cumplice = 4
assassino = 5

ocorrencias = lista.count('S')

if ocorrencias == suspeita:
    print('Suspeita!')
elif ocorrencias == cumplice:
    print('Cúmplice!')
elif ocorrencias == cumplice1:
    print('Cúmplice!')
elif ocorrencias == assassino:
    print('Assassino!')
else:
    print('Inocente!')