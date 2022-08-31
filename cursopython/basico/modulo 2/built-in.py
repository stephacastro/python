"""
Prevendo erros
# isnumeric - isdigit  - isdecimal
# chega numeros e se podem ser transformados em int
"""
num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

# solução 1 utilizando o isdigit para fazer a checagem
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não pode converter os números para realizar contas.')

# outra solução para fazer a checagem sem dar erro no programa
# try - execute esse e se der erro
#except - execute esse
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('ERROR')
