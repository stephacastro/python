
class Pessoa:
    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod # posso chamar a classe sem chamae self
    def metodo_classe(cls):
        print('Hello World')
    
    @classmethod 
    def criar_50(cls, nome):
        return cls(nome, 50)


p1 = Pessoa('Stephanie', 25)
p2 = Pessoa.criar_50('Maria')
print(Pessoa.ano)
Pessoa.metodo_classe()

print(p2.nome, p2.idade)
