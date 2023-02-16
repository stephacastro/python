# Métodos em instâncias de classes em Python

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenone = sobrenome


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'O {self.nome} está acelerando...')


fiesta = Carro('Fiesta')
fiesta.acelerar()
Carro.acelerar(fiesta)
