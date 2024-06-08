import Clientes
import Contas
import Transacoes

class Main:
    pass



""" ------- testes--------

t_c = Clientes.Pessoa_fisica(cpf= 123, nome="Rhuan", endereco= 'pipoca')

t_c.listar_contas()

t_c.adicionar_conta(Contas.Conta_Poupanca.nova_conta(t_c))

t_c.adicionar_conta(Contas.Conta_Corrente.nova_conta(t_c))

t_c.realizar_transacao(t_c.contas[0], Transacoes.Deposito(valor=123))

t_c.realizar_transacao(t_c.contas[0], Transacoes.Saque(valor=123))

t_c.contas[0].historico.exibir_extrato()

t_c.contas[0].exibir_saldo()

t_c.realizar_transacao(t_c.contas[1], Transacoes.Deposito(valor=123))

t_c.realizar_transacao(t_c.contas[1], Transacoes.Saque(valor=123))

t_c.contas[1].historico.exibir_extrato()

t_c.contas[1].exibir_saldo()

t_c.listar_contas()

"""