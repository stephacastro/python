print('''
      ******* Valor unitário R$ 12,50 *******

      * Até 5 camisetas, desconto de 3%
      * Acima de 5 camisetas até 10 camisetas, desconto de 5%
      * Acima de 10 camisetas, desconto 7%    

      ''')

quantidade = int(input('Quantas camisetas: '))

preco_unitario = 12.50
preco_total = quantidade * preco_unitario

if quantidade <= 5:
    desconto = preco_total * 0.03
    print('Desconto de 3%')
elif quantidade <= 10:
    desconto = preco_total * 0.05
    print('Desconto de 5%')
else:
    desconto = preco_total * 0.07
    print('Desconto de 7%')

preco_com_desconto = preco_total - desconto

print(f'''
      Desconto aplicado: R${desconto:.2f}
      Preço original da sua compra: R${preco_total:.2f}
      Preço com desconto: R${preco_com_desconto:.2f}
      ''')