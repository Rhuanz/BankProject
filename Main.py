import Clientes
import Contas
import Transacoes

class Main:
    
    @classmethod
    def Menu(self):
        print("""
[1] Extrato
[2] Saldo
[3] Deposito
[4] Saque
[5] Abrir conta
[6] Listar contas
[7] Sair

        """)
    
    @classmethod
    def Inicio(self):
        
        while(True):
            
            print("Bem vindo ao sistema bancário!\nSelecione uma opção:\n1 - Cadastrar PF\n2 - Cadastrar PJ\n3 - Sair\n")
            
            esc = int(input())
            
            if esc == 1:
                print("Insira seus dados:")
                nome = input("Seu nome: ")
                cpf = input("Seu CPF: ")
                endereco = input("Seu endereço: ")
                return Clientes.Pessoa_fisica(cpf, nome, endereco)
            
            elif esc == 2:
                print("Insira dados da empresa:")
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
        
        cliente = Main.Inicio()
        
        if cliente:
            while(True):
                Main.Menu()
                escolha = int(input("Operação desejada: "))
                
                if escolha == 1: #Extrato
                    if cliente.contas:
                        print("Selecione a conta que deseja conferir o extrato:")
                        for i in range(0, len(cliente.contas)):
                            print(f"Digite '{i}' para: {cliente.contas[i]}")
                        conta_extrato = int(input())
                        cliente.contas[conta_extrato].historico.exibir_extrato()
                    else:
                        print("Não existem contas para exibir extrato")
                elif escolha == 2: #Saldo
                    pass
                elif escolha == 3: #Deposito
                    pass
                elif escolha == 4: #Saque
                    pass
                elif escolha == 5: #Abrir conta
                    
                    tipo = int(input("Para conta corrente digite 1\nPara conta poupança digite 2\nEscolha: "))
                    
                    if tipo == 1:
                        
                        cliente.adicionar_conta(Contas.Conta_Corrente.nova_conta(cliente))
                        
                    elif tipo == 2:
                        
                        cliente.adicionar_conta(Contas.Conta_Poupanca.nova_conta(cliente))
                    
                    else:
                        print("Opção inválida! Tente novamente.")
                        
                elif escolha == 6: #Listar contas
                    pass
                elif escolha == 7: #Sair
                    break
                else:
                    print("Escolha uma opção válida")
                    continue

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