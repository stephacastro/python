"""
Fizz Buzz -  Se o parâmetro da função for divisível por 2, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz.
Se o parâmetroda função for divisível por 5 e por 3, retorne FizzBuzz,
caso contrário, retorne o número enviado.
"""

def fizzbuzz(numero):
    if numero % 5 == 0 and numero % 3 == 0:
        return 'FizzBuzz'
    if numero % 5 == 0:
        return 'Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    else:
        return numero

fizzbuzz = fizzbuzz(75)
print(fizzbuzz)
