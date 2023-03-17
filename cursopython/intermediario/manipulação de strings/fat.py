url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
#url = ""

if url == "":
    raise ValueError('URL vazia') # aponta erro pro usuario

# separa base e parametro
indice_inte = url.find('?')
url_base = url[:indice_inte]
url_par = url[:indice_inte+1:]
print(url_par)

# Busca o valor de um parâmetro
par_busca = 'quantidade'
indice_par = url_par.find(par_busca)
indice_valor = indice_par + len(par_busca) + 1
indice_comercial = url_par.find('&', indice_valor)

if indice_comercial == -1:
    valor = url_par[indice_valor:]
else:
    valor = url_par[indice_valor:indice_comercial]

print(valor)