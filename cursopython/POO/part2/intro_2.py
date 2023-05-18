class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome



p1 = Pessoa('Stephanie', 'Castro')
#p1.nome = 'Stephanie'

p2 = Pessoa('Manu', 'Brito')
#p2.nome = 'Manu'

print(p1.nome)
print(p2.nome)

print(p1.sobrenome)
print(p2.sobrenome)
