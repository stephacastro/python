"""
len - contagem de caracteres entre outras coisas
len não faz contagem de numeros int e float
"""
usuario = input('Digite seu usuario: ')
qtd_usuario = len(usuario)

if qtd_usuario < 6:
    print('Você precisa digitar pelo menos 6 caracteres.')
else:
    print('Você foi cadastrado no sistema.')

print(f'A quantidade de caracteres digitado foi {len(usuario)}')
