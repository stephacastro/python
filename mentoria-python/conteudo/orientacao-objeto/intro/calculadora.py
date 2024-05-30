class Calculadora:

    def soma(self, n1:int, n2:int):
        soma = n1 + n2 
        return f'A soma de {n1} e {n2} é = {soma}'
    
    def multiplicacao(self, n1:int, n2:int):
        mult = n1 * n2
        return f'A  multiplicalção de {n1} e {n2} é = {mult}'
    
    def divisao(self, n1:int, n2:int):
        div = n1 / n2 
        return f'A  devisão de {n1} e {n2} é = {div}'

    def subtracao(self, n1:int, n2:int):
        sub = n1 - n2
        return f'A  subtração de {n1} e {n2} é = {sub}'

# instanciando o objeto
calculadora = Calculadora()

# chamando a função dentro do objeto
soma = calculadora.multiplicacao(10, 2)
print(soma)

    