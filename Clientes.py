import Contas
import Transacoes

class Cliente:
    def __init__(self, endereco) -> None:
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta: Contas, transacao: Transacoes):
        
        if type(transacao) == Transacoes.Saque:
            
            if conta.sacar(valor=transacao.valor):

                print("Saque realizado com sucesso")
                transacao.registrar(conta)
                
            else:

                print("Saque não efetuado! Verifique seu saldo e tente novamente")

        elif type(transacao) == Transacoes.Deposito:

            if conta.depositar(transacao.valor): 
                
                print("Deposito efetuado")
                transacao.registrar(conta)

            else:
                print("Deposito não realizado! Revise o valor")

    def adicionar_conta(self, conta: Contas):

        if len(self.contas) < 2:

            self.contas.append(conta)
        else:
            print("Número de contas excedido")
    
class Pessoa_fisica(Cliente):
    def __init__(self, cpf, nome, endereco) -> None:
        self.cpf = cpf
        self.nome = nome
        super().__init__(endereco)

class Pessoa_Juridica(Cliente):
    def __init__(self, cnpj, nome_fantasia, endereco) -> None:
        self.cnpj = cnpj
        self.nome = nome_fantasia
        super().__init__(endereco)