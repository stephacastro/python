"""
Operadores Relacionais
== - igual a
> - maior que
>= - maior que ou igual a
< - menor que
<= - menor que ou igual a
!= - diferente de
"""
#n1 = 2
#n2 = 2
#exp = n1 == n2
#print(exp)
#n3 = 3
#n4 = 2
#exp2 = n3 > n4
#print(exp2)

nome = input('Qual é o seu nome? ')
idade = int(input('Qual a sua idade? '))

if idade <= 18:
    print(f'{nome} pode pegar um empréstimo.')
elif idade > 30:
    print(f'{nome} passou da idade para pegar um empréstimo')
else:
    print(f'{nome} não pode pegar um empréstimo.')