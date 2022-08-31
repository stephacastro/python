usuario = input('Nome de usuário: ')
senha = input('Senha do usuário: ')

id_usuario = 'stecastro'
senha_usuario = '1234'

if id_usuario == usuario and senha_usuario == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')