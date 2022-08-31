# iterar - passar sobre cada elemento da string

frase = 'o rato roeu a roupa do rei de roma' # Iterável
tamanho = len(frase)

contador = 0
nova_string = ''

usuario = input('Qual letra deseja colocar maiúscula: ')

# Iteração - Iterar = ato de percorrer cada elemento da string
while contador < tamanho:
    letra = frase[contador]
    if letra == usuario:
        nova_string += usuario.upper()
    else:
        nova_string += letra
    contador = contador + 1
print(nova_string)

