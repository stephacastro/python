from bank import Funcionario
import pytest
from pytest import mark

class TestClass:

    def test_quando_idade_recebe_21_09_1997_deve_retornar_26(self):
        entrada = '21/09/1997'
        esperado = 26

        funcionario_teste = Funcionario('Teste', entrada, 2000)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Stephanie_Castro_deve_retornar_Castro(self):
        entrada =  ' Stephanie Castro ' 
        esperado = 'Castro'

        ste = Funcionario(entrada, '21/09/1997', 5000)

        resultado = ste.sobrenome()

        assert resultado == esperado

    #@mark.skip  # pula um teste especifico
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        entrada_nome = 'Maria Yamato'
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        funcionario_teste.decrescimo_salario()

        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus # tag associado a um determinado teste
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 #given
        esperado = 100

        calcular = Funcionario('Teste', '11/12/1997', entrada)

        resultado = calcular.calcular_bonus() # when

        assert resultado == esperado # then

    @mark.calcular_bonus
    # teste com exceção de erro
    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exeption(self):
        with pytest.raises(Exception):
            entrada = 10000000 #given

            calcular = Funcionario('Teste', '11/12/1997', entrada)

            resultado = calcular.calcular_bonus() # when

            assert resultado # then
        
