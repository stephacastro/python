"""
While / else
Contadores
Acumuladores - acrescentar a cada laço
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador = contador + 1
else:
    print('Acabou')
