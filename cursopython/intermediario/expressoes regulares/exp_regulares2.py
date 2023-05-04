import re 

padrao = '[0-9][a-z][0-9]'
texto = '123 1a2 1cc aa1'

resposta = re.search(padrao, texto)
print(resposta.group())

padrao_email = '\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}'
texto_email = 'jshdyaush stephanie@gmail.com.br ahsuahus'

resposta2 = re.search(padrao_email, texto_email)
print(resposta2.group())