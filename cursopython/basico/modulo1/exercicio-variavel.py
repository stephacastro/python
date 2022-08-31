"""
Criar variaveis para nome (str), idade (int),
altura (float) e peso (float) de uma pessoa
criar variável com o ano atual (int)
Obter o ano de nascimento da pessoa baseado na idade e no ano atual
obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
exibir um texto com todos os valores na tela usando f-strings (com as chaves)
"""

nome = 'Stephanie'
idade = 25
altura = 1.68
peso = 69.90
ano = 2022
nascimento = ano - idade
imc = peso / altura ** 2

print(f'{nome} tem {idade} anos e tem {altura} de altura.')
print(f'{nome} pesa {peso}kg e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
