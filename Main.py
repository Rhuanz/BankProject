import Clientes
import Contas
import Transacoes

class Main:
    
    @classmethod
    def Menu(self):
        return("\nBem vindo! Selecione uma das opções abaixo:\n[1] Realizar operação\n[2] Abrir conta\n[3] Listar contas\n[4] Sair\nOperação desejada: ")
    
    @classmethod
    def MenuOperacao(self):
        return("\nSelecione a operação desejada:\n1 - Extrato\n2 - Saldo\n3 - Deposito\n4 - Saque\nOperação desejada: ")
    
    @classmethod
    def Cadastro(self):
        
        while(True):

            esc = int(input("\nBem vindo ao sistema bancário!\nSelecione uma opção:\n[1] - Cadastrar PF\n[2] - Cadastrar PJ\n[3] - Sair\nOpção desejada: "))
            
            if esc == 1:
                print("Insira seus dados")
                nome = input("Seu nome: ")
                cpf = input("Seu CPF: ")
                endereco = input("Seu endereço: ")
                return Clientes.Pessoa_fisica(cpf, nome, endereco)
            
            elif esc == 2:
                print("Insira dados da empresa")
                nome = input("Nome da empresa: ")
                cnpj = input("CNPJ da empresa: ")
                endereco = input("Endereço da empresa: ")
                return Clientes.Pessoa_Juridica(cnpj, nome, endereco)
            
            elif esc == 3:
                return None
            
            else:
                print("Escolha uma opção válida!\n")

    @classmethod
    def Main(self):
        
        cliente = Main.Cadastro()
        
        if cliente:
            
            while(True):
                
                escolha = int(input(Main.Menu()))
                
                if escolha == 1: #Realizar operação
                    if cliente.contas:
                        operacao = int(input(Main.MenuOperacao()))
                        
                        if operacao == 1: #Extrato
                            print("Selecione a conta que deseja conferir o extrato:")
                            for i in range(0, len(cliente.contas)):
                                print(f"Digite '{i}' para: {cliente.contas[i]}")
                            conta_extrato = int(input("Conta selecionada: "))
                            cliente.contas[conta_extrato].historico.exibir_extrato()
                        
                        if operacao == 2: #Saldo
                            pass
                        if operacao == 3: #Deposito
                            pass
                        if operacao == 4: #Saque
                            pass
                        else:
                            print("Número de operação inválido! Tente novamente")
                    else:
                        print("Não existem contas para realizar operação")

                elif escolha == 2: #Abrir conta
                    
                    tipo = int(input("Para conta corrente digite 1\nPara conta poupança digite 2\nEscolha: "))
                    
                    if tipo == 1: #Conta corrente
                        
                        cliente.adicionar_conta(Contas.Conta_Corrente.nova_conta(cliente))
                        
                    elif tipo == 2: #Conta poupança
                        
                        cliente.adicionar_conta(Contas.Conta_Poupanca.nova_conta(cliente))
                    
                    else:
                        print("Opção inválida! Tente novamente.")
                        
                elif escolha == 3: #Listar contas
                    pass
                elif escolha == 4: #Sair
                    print("Encerrando o sistema...")
                    break
                else:
                    print("Escolha uma opção válida")
                    continue
        else:
            print("Encerrando o sistema...")
            
Main.Main()
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