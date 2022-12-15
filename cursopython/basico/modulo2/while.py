
"""
While
Utilizado para realizar ações enquanto uma condição for verdadeira
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        # pula para o proximo laço
        #continue
        # finaliza o loop
        break
    print(x)
    x = x + 1

print('Acabou!')

x = 0 #coluna

while x < 10:
    y = 0  # linha
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x = x + 1

print('Acabou!')

while True:
    print()
    num1 = input('Digite um número: ')
    num2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    sair = input('Deseja sair? [s]im ou [n]ão: ')

    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número.')
        continue
    num1 = int(num1)
    num2 = int(num2)
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '**':
        print(num1 ** num2)
    else:
        print('Operador Inválido!')