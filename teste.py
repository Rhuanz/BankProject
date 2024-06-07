import Clientes
import Contas
import Transacoes

t_c = Clientes.Pessoa_fisica(cpf= 123, nome="Rhuan", endereco= 'pipoca')

t_c.adicionar_conta(Contas.Conta.nova_conta(t_c))


t_c.realizar_transacao(t_c.contas[0], Transacoes.Deposito(valor=123))


t_c.realizar_transacao(t_c.contas[0], Transacoes.Saque(valor=123))

t_c.contas[0].historico.exibe_extrato()