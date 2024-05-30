class Pessoa:
    def __init__(self, nome:str, idade:int,  peso:int, altura:float) -> None:
        self.nome = nome
        self.idade = idade 
        self.peso = peso 
        self.altura = altura

    def calcula_imc(self):
        imc = self.peso / (self.altura ** self.altura)
        print(f'O seu IMC é : {imc:.2f}')


pessoa = Pessoa("Stephanie", 26, 70, 1.67)
print(pessoa.nome)

pessoa.calcula_imc()