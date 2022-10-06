"""
funções - def 
"""

# criando a função
def funcao():
    print('Hello World')

# chamando a função
funcao()

# função com parametro
def funcao1(msg):
    print(msg)

# chamando a função e definindo o valor do parametro
funcao1('Mensagem')

# função com parametro
def saudacao(msg, nome):
    print(msg, nome)

# chamando a função e definindo o valor do parametro
saudacao('Olá', 'Stephanie')
saudacao('Olá', 'Manu')

# função com parametro e ja colocando valores
def saudacao(msg='Olá', nome='usuário'):
    print(msg, nome)

# chamando a função
saudacao()