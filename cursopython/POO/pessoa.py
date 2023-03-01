# atributo de classes

class Pessoa:
    ano_atual = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        return Pessoa.ano_atual - self.idade 
    

p1 = Pessoa('Stephanie', 25)

print(Pessoa.ano_atual)
print(p1.ano_nascimento())