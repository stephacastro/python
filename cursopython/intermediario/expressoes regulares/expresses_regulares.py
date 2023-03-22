# expressões regulares identifica padrões 

import re # modulo para trabalhar com expressões regulares

endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 05181-100'

# criando um padrão // ? para o python entender que pode ter o hifen ou não
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

# simplificando o padrão // {quantidade} quantas vezes o conjunto pode aparecer no padrão 
padrao2 = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
padrao3 = re.compile("[0-9]{5}[-]?[0-9]{3}") # 0-9 indica que qualquer numero nesse intervalo é valido

# buscamdo o padrão definido em uma variavel 
busca = padrao3.search(endereco) # retornada MATCH caso o padrão for encontrado e NONE se não

if busca:
    cep = busca.group() # retorna o grupo de string encontrada no padrão
    print(cep)
    
else:
    print('Padrão não encontrado')