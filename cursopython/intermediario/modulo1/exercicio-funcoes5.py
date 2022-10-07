"""
Crie uma função1 de recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""

def func1():
    return 'Hello World'

var = func1()

def func2(arg):
    print(arg)

func2(var)