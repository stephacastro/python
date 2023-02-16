# POO

class Conta:
    # __init__ (função contrutor) me permiti criar a funcionalidade inicial da classe
    # self - acessa as propriedades de uma instância
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo um objeto... {self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    def extrato(self):
        print(f'Saldo de {self.saldo} do titular {self.titular}')

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor


conta = Conta(152, 'Stephanie', 173.5, 1000.0)
conta2 = Conta(176, 'Manu', 90.0, 2000.0)

# chamando o objeto e acessando a função
conta.extrato()