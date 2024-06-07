from abc import ABC, abstractmethod
import Contas
import time as tm

dia = tm.localtime(tm.time())
dia = f"{dia.tm_mday}/{dia.tm_mon}/{dia.tm_year}"

class Transacao(ABC):
    
    @abstractmethod
    def registrar(self, conta: Contas):
        pass

class Saque(Transacao):

    def __init__(self, valor: float) -> None:
        self.valor = valor
        self.data = dia

    def registrar(self, conta: Contas):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"{self.__class__.__name__} - Valor: {self.valor} - Data: {self.data}"

class Deposito(Transacao):

    def __init__(self, valor: float) -> None:
        self.valor = valor
        self.data = dia

    def registrar(self, conta: Contas):
        conta.historico.adicionar_transacao(self)

    def __str__(self):
        return f"{self.__class__.__name__} - Valor: {self.valor} - Data: {self.data}"

class Historico:
    def __init__(self) -> None:
        self.historico = []

    def adicionar_transacao(self, transacao: Transacao):
        self.historico.append(transacao)

    def exibe_extrato(self):
        for i in self.historico: print(i)