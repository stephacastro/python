# Polimorfismo, quando precisamos utilizar a mesma função em outras classes filhas mas com 
# funções diferentes, declaramos ela na classe Pai e damos a suas funcionalidades nas classes filhas 

class ContaBancaria:
    def __init__(self, titular:str, saldo:float):
        self.titular = titular
        self.__saldo = saldo

    def ver_saldo(self):
        return round(self.__saldo, 2)    

    def calcular_taxa(self):
        raise NotImplementedError("Esse método precisa ser implementado na sua classe filha!!")

    def __str__(self):
        return f"Conta de {self.titular} com saldo de R$ {round(self.__saldo, 2)}"


class ContaCorrente(ContaBancaria):
    def calcular_taxa(self):
        return f"Sua taxa de manutenção é de R$ 20,00"


class ContaPoupanca(ContaBancaria):
    def calcular_taxa(self):
        return f"Seu rendimento mensal é de 0.02%, seu saldo de rendimento é R${self.ver_saldo()*0.02}"

conta_corrente = ContaCorrente("Stephanie Castro", 200)
conta_poupanca = ContaPoupanca("Emanuelli Brito", 500)

print(conta_corrente.calcular_taxa())
print(conta_poupanca.calcular_taxa())