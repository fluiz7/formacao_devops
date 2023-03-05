from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_09_2001_retorno_esperado_22(self):
        #given-contexto
        entrada = "13/09/2001"
        funcionario_teste = Funcionario("teste", entrada, 1320)

        #when-ação
        esperado = 22
        resultado = funcionario_teste.idade()

        #then-desfecho
        assert resultado == esperado

    def test_quando_nome_recebe_Laura_Azevedo_retorno_esperado_Azevedo(self):
        #given-contexto
        entrada = " Laura Azevedo "
        funcionario_teste = Funcionario(entrada, "12/07/1984", 2400)

        #when-ação
        esperado = "Azevedo"
        resultado = funcionario_teste.sobrenome()

        #then-desfecho

        assert esperado == resultado

    def test_decrescimo_salario_quando_salario_100000_retorna_90000(self):
        #given
        entrada_nome = "Paulo Bragança"
        entrada_salario = 100000
        esperado = 90000

        #when
        funcionario_test = Funcionario(entrada_nome, 11/12/1976, entrada_salario)
        funcionario_test.decrescimo_salario()
        resultado = funcionario_test.salario

        #then
        assert resultado == esperado
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_test = Funcionario("teste", 14/10/1994, entrada)
        resultado = funcionario_test.calcular_bonus()

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calculcar_bonus_recebe_1000000_deve_retornar_Exception(self):
        with pytest.raises(Exception):
            entrada = 100000000

            funcionario_test = Funcionario("teste", 14 / 10 / 1994, entrada)
            resultado = funcionario_test.calcular_bonus()

            assert resultado


