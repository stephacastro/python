# POO

class Conta:
    # __init__ (função contrutor) me permiti criar a funcionalidade inicial da classe
    # self - acessa as propriedades de uma instância
    def __init__(self, numero, titular, saldo, limite):
        print(f"Construindo um objeto... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def deposita(self, valor):
        self.__saldo += valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def saca(self, valor):
        self.__saldo -= valor
    
    @property
    def saldo(self):
        return self.__saldo
    
    def set_limite(self):
        return self.__limite

conta = Conta(152, 'Stephanie', 173.5, 1000.0)
conta2 = Conta(176, 'Manu', 90.0, 2000.0)

# chamando o objeto e acessando a função encapsulado
conta._Conta__saldo

# chamando o objeto e acessando a função 
conta2.extrato()

conta.saldo()