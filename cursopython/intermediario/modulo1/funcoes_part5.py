"""
Higher Order Functions -  Funções que podem receber e/ou retornar outras funções
Funções de primeira classe 
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(executa(saudacao, 'Boa noite', 'Stephanie'))

