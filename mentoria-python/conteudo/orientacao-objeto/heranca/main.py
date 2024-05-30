# Herança é quando as classes filhas herdam na classe pai 

class Veiculo:
    def __init__(self, cor, velocidade, marca, tipo):
        self.marca = marca 
        self.cor = cor 
        self.__velocidade = velocidade
        self.tipo = tipo 

    def velocidade_atual(self):
        return f'O carro está a {self.__velocidade} km/H'

    def acelerar(self, incremento):
        self.__velocidade += incremento

    def frear(self, decremento):
        self.__velocidade -= decremento

        if self.__velocidade < 0:
            self.__velocidade = 0

class Carro(Veiculo):
    # mesmo herdando da classe pai Veiculo, a classe Carro tbm pode ter seus próprios atributos 
    def __init__(self, cor, velocidade, marca, tipo, qtd_portas=0):
        # usamos o super init para podermos puxar da nossa classe que estamos herdando os atributos definidos nela
        super().__init__(cor, velocidade, marca, tipo) 
        self.qtd_portas = qtd_portas

    def buzinar(self):
        print("PAPANN!")

    def __str__(self):
        return f'Carro de marca {self.marca}, modelo {self.modelo} e com {self.qtd_portas} portas'


class Moto(Veiculo):

    def __init__(self, cor, velocidade, marca, tipo, cilindradas) -> None:
        super().__init__(cor, velocidade, marca, tipo)
        self.cilindradas = cilindradas

    def xingar_motorista_carro(self):
        print("Cuidado, seu bosta!")


meu_carro = Carro(cor="Vermelho", velocidade=20, marca="Renaul", tipo="sedan", qtd_portas=4)


print(meu_carro)
# meu_carro.acelerar(60)

# print(meu_carro.velocidade_atual())

# meu_carro.frear(30)

# print(meu_carro.velocidade_atual())

# meu_carro.buzinar()

minha_moto = Moto("preta", 0, "yamaha", "scooter", 600)

# print(minha_moto)


# print(f"a moto tem {minha_moto.qnt_portas} portas")
# minha_moto.xingar_motorista_carro()