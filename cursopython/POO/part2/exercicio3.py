
class Conta():
    def __init__(self, nome, conta, saldo=0):
        self.nome = nome
        self.conta = conta
        self.saldo = saldo
    
    def extrato(self):
        return f'***** EXTRATO ***** \nTITULAR: {self.nome} \nCONTA: {self.conta} \nSALDO DISPONÍVEL: R${self.saldo}'

    def AlterarNome(self):
        return self.nome

    def deposita(self, valor):
        self.saldo += valor
        return 'Depositando...'

    def saca(self, valor):
        self.saldo -= valor
        return 'Sacando...'

    def saldofinal(self):
        if self.saldo < 0:
             return f'SUA CONTA DE N° {self.conta} ESTÁ NEGATIVA... R${self.saldo} REAIS'    
    
        print(f'O SALDO DA CONTA É DE R${self.saldo} REAIS')


p1 = Conta('Maria', 2345, 1000)
p2 = Conta('João', 1234, 20)
p1 = Conta('José', 2345, 1000)

print(p1.AlterarNome())
print(p2.extrato())
print(p2.deposita(10))
print(p2.extrato())
print(p2.saca(32))
print(p2.extrato())
print(p2.saldofinal())
print(p2.deposita(10))
print(p2.saldofinal())
