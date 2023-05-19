# Salve a classe em Json
# Salve os dados da sua classe em Json
# Crie novamente as instâncias da classe com os dados salvos
# Faça em arquivos separados 

import json

caminho_arq = 'exercicio1.json'

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

p1 = Pessoa('Manu', 7)
p2 = Pessoa('Stephanie', 26)
p3 = Pessoa('Katarina', 53)

bd = [vars(p1), vars(p2), p3.__dict__]

with open(caminho_arq, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
    

