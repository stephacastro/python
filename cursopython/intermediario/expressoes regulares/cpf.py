import re 

texto = 'Stephanie de Castro, 25, 768.726.957-87'

padrao = re.compile('[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}')

busca = padrao.search(texto)

if busca:
    cpf = busca.group()
    print(cpf)
else:
    print('Não existe este padrão')