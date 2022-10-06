"""
Crie uam função que receba 2 números. O primeiro é um valor e o segundo um percentual.
Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
"""

def percentual(n1, n2):
    return n1 + (n1 * n2 / 100)

percentual = percentual(100, 10)
print(percentual)
