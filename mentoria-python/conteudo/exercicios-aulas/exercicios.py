
class Pessoa:
    def __init__(self, nome:str) -> None:
        self.nome = nome

    def saudacao(self):
        print(f'Olá {self.nome}, seja bem vinda!')

saudacao = Pessoa('Stephanie')
print(Pessoa.saudacao)