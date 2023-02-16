"""Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

cor = 'preto'
circunferencia = 70
material = 'coro'
cor2 = 'Azul'

class Bola:
    def __init__(self):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material 

    def trocarCor(self):
        self.cor2

    def mostrarCor(self):
        print(f'A cor {cor} mudou para {cor2}')

Bola.mostrarCor(cor, cor2)

