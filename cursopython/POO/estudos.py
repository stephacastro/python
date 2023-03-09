
class Caneta:
    def __init__(self, cor):
        self.cor = cor

    @property
    def cor(self):
        return self.cor_tinta
    
caneta = Caneta('Azul')
print(caneta.cor)