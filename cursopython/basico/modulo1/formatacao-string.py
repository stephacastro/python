nome = 'Stephanie'
idade  = 24
altura = 1.68
peso = 70
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de udade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))