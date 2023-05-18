# Classe é o molde (geralmente sem dados)
# Instância da classe (objeto) - Tem dados
# Uma classe pode gerar várias instâncias
# Na classe o self é a própria instância

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)   
Carro.acelerar(fusca)  

celta = Carro('Celta')
print(celta.nome)  
celta.acelerar()