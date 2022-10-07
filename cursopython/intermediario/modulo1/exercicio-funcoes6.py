"""
Crie uma função1 que recebe uma função2 como parÂmetro e retorne o 
valor da funçã2 executada. Faça a função1 executar duas funções que
recebem um número diferente de argumentos
"""

def nome(nome):
    return f'{nome}'

var1 = nome('Stephanie')

def saudacao(saudacao1, saudacao2):
    return f'{saudacao1}, {saudacao2}'

var2 = saudacao('Oi', 'Prazer em te conhecer')

def funcao_principal(*args):
    print(*args)

funcao_principal(var2, var1)