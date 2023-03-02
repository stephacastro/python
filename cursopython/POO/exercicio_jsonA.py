import json

arq = 'arq.json'

class Pessoa: 
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Stephanie', 25)
p2 = Pessoa('Manu', 7)
p3 = Pessoa('Ana', 46)
bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
    with open(arq, 'w') as arquivo:
        print('Fazendo DUMP')
        json.dump(bd, arquivo, ensure_ascii=False, indent=2)