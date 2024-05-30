# tudo em python é um objeto

class Pessoa:
    # inicialização dos atributos da classe
    def __init__(self, nome:str, idade:int, peso:int, altura:float):
        self.nome = nome
        self.idade = idade 
        self.peso = peso 
        self.altura = altura 

    def meu_nome(self):
        return self.nome

    def apresentacao(self):
        print(f'Oi, meu nome é {self.nome}, eu tenho {self.idade} anos, prazer!')

    def calcula_imc(self):
        imc = self.peso ; (self.altura ** 2)
        print(f'Meu IMC é de {imc,2}')

pessoa1 = Pessoa('Stephanie', 26, 70, 1.67)
print(pessoa1.apresentacao())