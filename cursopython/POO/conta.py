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


conta = Conta(152, 'Stephanie', 173.5, 1000.0)
conta2 = Conta(672, 'Mario', 73.0, 1000.0)
conta3 = Conta(3, "Manu", 0.0, 2000.0)

print(conta.titular, conta.saldo)