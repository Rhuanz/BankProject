import Transacoes
import Clientes

class Conta:

    AGENCIA = "001"

    def __init__(self, cliente: Clientes) -> None:
        self.cliente = cliente
        self.saldo = 0
        self.ag = Conta.AGENCIA
        self.historico = Transacoes.Historico()

    def exibir_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

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
        
class Conta_Corrente(Conta):
    
    total_contas = 0
    
    def __init__(self, cliente: Clientes):
        self.lim_transacao = False
        self.lim_cheque_especial = 500
        self.numero = Conta_Corrente.total_contas
        super().__init__(cliente)
        
    
    @classmethod
    def nova_conta(cls, cliente: Clientes):
        Conta_Corrente.total_contas += 1
        return cls(cliente)
    
    def __str__(self):
        return f"Conta Corrente - Número: {self.numero}, AG: {self.ag}"


class Conta_Poupanca(Conta):
    
    total_contas = 0
    
    def __init__(self, cliente: Clientes):
        self.lim_transacao = 10
        self.numero = Conta_Poupanca.total_contas
        super().__init__(cliente)
    
    @classmethod
    def nova_conta(cls, cliente: Clientes):
        Conta_Poupanca.total_contas += 1
        return cls(cliente)

    def __str__(self):
        return f"Conta Poupança - AG: {self.ag}, Número: {self.numero}"