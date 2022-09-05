"""
Uma loja deseja cadastrar 5 clientes e verificar se o faturamento da loja foi superior a loja B (faturamento = 54000).
Se o faturamento atingir esse valor mostre na tela uma mensagem contendo em quanto foi superado o faturamento.
"""
contador = 0
lojab = 54000


while contador < 5:
    cliente = input('Nome: ')
    nota = float(input('Total gasto: '))
    contador = contador + 1
    

    if contador == 5:
        total = nota + nota + nota + nota + nota 
        print(f'Os 5 clientes cadastrados totalizaram um lucro de R${total:.2f}')
        print('')
        if total > lojab:
            diferenca = total - lojab
            print(f'O faturamento foi superior a loja B somando R${total:.2f}')
            print('')
            print(f'A diferença foi de R${diferenca:.2f} Parabéns!!')
        else:
            print(f'O faturamento de R${total:.2f} foi inferior a loja B')
