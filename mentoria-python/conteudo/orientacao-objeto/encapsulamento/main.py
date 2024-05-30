# encapsulamento e quando privamos objetos para nao serem usadas em outra classe
# aquele objeto nao pode ser acessado fora da classe que ele foi inicializado

class ContaBancaria:
    def __init__(self, saldo_inicial):
        # encapsulando o objeto
        self.__saldo = saldo_inicial  # Atributo privado

    def fazer_pix(self, valor: float):
        if valor > 0:
            self.__saldo += valor
            print(f"Pix no valor de R$ {valor} foi realizado. Verifique seu saldo atual.")
        else:
            print("Valor não permitido!")
    
    def sacar(self, valor: float):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor} foi realizado. Verifique seu saldo.")
        else:
            print("Saldo Insuficiente ou valor de saque inválido!")

    def consultar_saldo(self):
        print(f"Seu saldo atual é de R$ {self.__saldo}")

minha_conta = ContaBancaria(100)

# minha_conta.fazer_pix(400)
# # minha_conta.sacar(500)
# minha_conta.sacar(485.00)
# minha_conta.consultar_saldo()