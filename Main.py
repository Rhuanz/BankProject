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
                       
                       
                        #Criar sistema de verificação da conta selecionada
                        
                        
                        operacao = int(input(Main.MenuOperacao()))
                        
                        if operacao == 1: #Extrato
                            print("Selecione a conta que deseja conferir o extrato:")
                            cliente.listar_contas()
                            conta_extrato = int(input("Conta selecionada: "))
                            cliente.contas[conta_extrato].historico.exibir_extrato()
                        
                        elif operacao == 2: #Saldo
                            print("Selecione a conta que deseja conferir o saldo:")
                            cliente.listar_contas()
                            conta_saldo = int(input("Conta selecionada: "))
                            cliente.contas[conta_saldo].exibir_saldo() 
                             
                        
                        elif operacao == 3: #Deposito
                            
                            print("Selecione a conta que deseja realizar depósito:")
                            cliente.listar_contas()
                            conta_deposito = int(input("Conta selecionada: "))
                            valor = int(input("Digite o valor a ser depositado: "))
                            cliente.realizar_transacao(cliente.contas[conta_deposito], Transacoes.Deposito(valor))
                            
                        elif operacao == 4: #Saque
                            print("Selecione a conta que deseja realizar o saque:")
                            cliente.listar_contas()
                            conta_saque = int(input("Conta selecionada: "))
                            valor = int(input("Digite o valor a ser sacado: "))
                            cliente.realizar_transacao(cliente.contas[conta_saque], Transacoes.Saque(valor))
                        else:
                            print("Número de operação inválido! Tente novamente")
                    else:
                        print("Não existem contas para realizar operação!")

                elif escolha == 2: #Abrir conta
                    
                    tipo = int(input("Para conta corrente digite 1\nPara conta poupança digite 2\nEscolha: "))
                    
                    if tipo == 1: #Conta corrente
                        
                        cliente.adicionar_conta(Contas.Conta_Corrente.nova_conta(cliente))
                        
                    elif tipo == 2: #Conta poupança
                        
                        cliente.adicionar_conta(Contas.Conta_Poupanca.nova_conta(cliente))
                    
                    else:
                        print("Opção inválida! Tente novamente.")
                        
                elif escolha == 3: #Listar contas
                    cliente.listar_contas()
                elif escolha == 4: #Sair
                    print("Encerrando o sistema...")
                    break
                else:
                    print("Escolha uma opção válida")
                    continue
        else:
            print("Encerrando o sistema...")
            
Main.Main()
