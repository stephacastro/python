print('====================== Exercicio 1 ======================')

while True:
    nota = float(input('Digite uma nota de zero a dez: '))

    if 0<= nota <= 10:
        print(f'Nota válida: {nota}')
        break
    else:
        print('Valor inválido. Por favor, digite uma nota entre zero e dez')


print('\n====================== Exercicio 2 ======================')

while True:
    usuario = int(input('Digite um número para saber a tabuada: '))

    if 0<= usuario <=10:
        tabuada1 = usuario * 1
        tabuada2 = usuario * 2
        tabuada3 = usuario * 3
        tabuada4 = usuario * 4
        tabuada5 = usuario * 5
        tabuada6 = usuario * 6
        tabuada7 = usuario * 7
        tabuada8 = usuario * 8
        tabuada9 = usuario * 9
        tabuada10 = usuario * 10

        print(f'''A tabuada do {usuario}\n
            {usuario} x 1 = {tabuada1}\n
            {usuario} x 2 = {tabuada2}\n
            {usuario} x 3 = {tabuada3}\n
            {usuario} x 4 = {tabuada4}\n
            {usuario} x 5 = {tabuada5}\n
            {usuario} x 6 = {tabuada6}\n
            {usuario} x 7 = {tabuada7}\n
            {usuario} x 8 = {tabuada8}\n
            {usuario} x 9 = {tabuada9}\n
            {usuario} x 10 = {tabuada10}\n''')
    else:
        break
        




