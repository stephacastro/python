"""
Exemplos Válidos:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos não Válidos:
    https://bytebank/cambio
    https://bytebank.naoexiste/cambio
    ht://bytebank.naoexiste/cambio
"""

# https://www.bytebank.com.br/cambio

import re 

url = 'www.bytebank.com.br/cambio'

# utilizando () para o python entender que precisa ser exatamente o que esta dentro do ()
# utilizando o [] o python entende que pode ser qualquer coisa que for encontrado dentro do []
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

match = padrao_url.match(url) # identidica o padrao exato

if not match:
    raise ValueError('A URL não é válida')
else:
    print('A URL é Válida')
