from bank import Funcionario

class TestClass:
    def test_quando_idade_recebe_21_09_1997_deve_retornar_26(self):
        entrada = '21/09/1997'
        esperado = 26

        funcionario_teste = Funcionario('Teste', entrada, 2000)
        resultado = funcionario_teste.idade()

        assert resultado == esperado