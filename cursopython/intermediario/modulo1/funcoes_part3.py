"""
Funções (def) - *args **kwargs
"""

# None = nenhum valor 
# Os argumentos devem seguir um padrão, quando o padrão for alterado
# da alteração em diante deve se seguir o novo padrão


def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1, a2, a3, a4, a5, nome, a6)

var = func(1,2,3,4,5, nome='Stephanie', a6='6')


# *n faz o empacotamento/desempacotamento de valores
# sep=',' - é um separador

# args é um empacotamento de valores que por padrão são tuplas
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1,2,3,4,5)


# transformando o empacotamento padrão de args(tupla) por lista
def func(*args):
    args = list(args)
    args [0] = 20 # alterando o valor da posição 0 por 20
    print(args)

func(1,2,3,4,5)

# percorando os valores da func com for
def func(*args):
    for v in args:
        print(v)
   
func(1,2,3,4,5)   


# **kwargs = são argumentos com palavras chaves
def func(*args, **kwargs):
    for v in args:
        print(v)
        print(kwargs=['nome'])
   
func(1,2,3,4,5, nome='Stephanie')  


# utulizando o get para kwargs - se o argumento não existir
# não para o programada, retorna None
# melhor usar get quando não sabemos se o argumento existe

def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade') # passando um parametro 

    if idade is not None: # fazendo a checagem do argumento
        print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome='Stephanie', idade='25') # desempacotando as listas e nomenando os argumentos 'chave'