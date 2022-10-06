"""
Uma loja tem tem uma política de descontos de acordo com o valor da compra do cliente. 
Os descontos começam acima dos R$500. 
A cada 100 reais acima dos R$500,00 o cliente ganha 1% de desconto cumulativo até 25%. 
"""

valorcompra = 500

for i in range(1,26):
    porcentagem = valorcompra * (1-(i/100))
    print(f'Valor da compra {valorcompra}, porcentagem de desconto {i}%, valor final R${porcentagem}')
    valorcompra = valorcompra + 100