import Transacoes
import Clientes

class Conta:

    total_contas = 0

    def __init__(self, cliente: Clientes) -> None:
        self.cliente = cliente
        self.saldo = 0
        self.numero = Conta.total_contas
        self.ag = 1
        self.historico = Transacoes.Historico()

    @classmethod
    def nova_conta(cls, cliente: Clientes):
        Conta.total_contas += 1
        return cls(cliente)

    def exibir_saldo(self):
        print(self.saldo)

    def sacar(self, valor: float):
        if valor > self.saldo: return False
        else:
            self.saldo -= valor
            return True

    def depositar(self, valor: float):
        if valor <= 0: return False
        else:
            self.saldo += valor
            return True