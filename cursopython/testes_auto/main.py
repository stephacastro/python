from bank import Funcionario

# Teste
def teste_idade():
    funcionario_teste = Funcionario('Teste', '21/09/1997', 2000)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()

