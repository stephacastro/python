"""
Crie funções que duplicam, triplicam e quadriplucam
o número recebido como parâmetro 
"""

# 1° solução

def duplicar(duplicar = 2):
    print(f'Multiplo de 2 é igual á',duplicar * 2)

def triplicar(triplicar = 3):
    print(f'Triplo de 3 é igual á',triplicar * 3)

def quadriplicar(quadriplicar = 4):
    print(f'Quadruplo de 4 é igual á',quadriplicar * 4)

duplicar()
triplicar()
quadriplicar()

print('\n')
print('***********************************************************************')
print('\n')

# 2° solulção 

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(f'Multiplo de 5 é igual á',duplicar(5))
print(f'Triplo de 100 é igual á',triplicar(100))
print(f'Quadruplo de 6 é igual á',quadriplicar(6))
