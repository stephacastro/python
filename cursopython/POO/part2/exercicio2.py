
class Carro():
    def __init__(self, modelo, marca, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor 

    def acelerar(self):
        return f'{self.modelo} Está acelerando...'
    
    def freiar(self):
        return f'{self.modelo} Está freiando...'

    def buzinar(self):
        return f'{self.modelo} BÍ BÍIII'
    

c1 = Carro('Fiesta', 'Ford', 2008, 'Preto')
print(c1.acelerar())
print(c1.freiar())
print(c1.buzinar())