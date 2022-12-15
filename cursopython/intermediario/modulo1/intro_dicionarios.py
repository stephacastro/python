"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo chave e valor
Chaves podem ser consideradas como o índice e podem ser de tipos imutáveis
o valor pode ser de qualquer tipo, incluindo outro dicionário
Lista e dicionários são mutáveis
"""

pessoa = {
    'nome': 'Stephanie',
    'sobrenome': 'Castro',
    'idade': 25,
    'altura': 1.67,
    'endereco': [{'rua': 'Ministro Aníbal Freire', 'numero': 75}]
}

print(pessoa, type(pessoa))
print('\n')

# acessando um indice do dicionario
print(pessoa['nome'])


print('\n')

# criando um dicionário com classe 
# obs - não é muito usado
fruta = dict(nome='Manga')
print(fruta, type(fruta))


nome = {}
nome['nome'] = 'Stephanie'
print(nome)


# apagando uma chave
time = {}
time['time1'] = 'Corintians'
time['time2'] = 'Barcelona'

del time['time1']
print(time)

if time.get('time') is None:
    print('Não existe')
else:
    print(time['time'])
