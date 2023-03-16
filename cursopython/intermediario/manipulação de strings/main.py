url = 'https://bytebank.com/cambio?moedaOrigem=real'


#fateamento
print(url[0:19])

print(url[20::])

find = url.find('?')
print(url[find::])
print(url[:find])


url = "https://www.curso.com.br/curso?curso=python"
indice_curso = url.find("curso")
indice_valor = indice_curso + len("curso") + 1
valor = url[indice_valor:]
print(valor)