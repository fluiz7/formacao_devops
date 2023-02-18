from abc import ABCMeta
import numpy as np


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        """
        Função que representa a alteração do saldo na conta ao depositar mais dinheiro.
        :param valor: a quantia que será depositada na conta.
        :return: saldo da conta com a adição do depósito.
        """
        self.saldo += valor

    @classmethod
    def passa_o_mes(cls):
        pass

    def __str__(self):
        return f"Agência: {self.codigo:5}\nSaldo: R${self.saldo:5.2f}"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self.saldo -= 6


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self.saldo *= 1.006
        self.saldo -= 4


class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo

    def __str__(self):
        return f"Código: {self._codigo}\nSaldo: {self._saldo}"


class ContaMultiploSalario(ContaSalario):
    pass


conta1 = ContaSalario(15)
conta2 = ContaSalario(15)

idades = [14, 66, 48, 23, 47, 65, 35, 42, 15]




#for i, idade in enumerate(idades):
#    print(i, idade)

#for idade in range(len(idades)):
#    print(idade, idades[idade])

#for conta in contas:
#    conta.deposita(500)
#    print(conta)
#    conta.passa_o_mes()
#    print(conta)


#def visualizar(lista=None):
#    if lista is None:
#        lista = list()
#
#    print(len(lista))
#    lista.append(5)
#    print(lista)
