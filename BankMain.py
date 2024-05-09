import time as tm
from random import randint

dia = tm.localtime(tm.time())
dia = f"{dia.tm_mday}/{dia.tm_mon}/{dia.tm_year}"


def menu():
    print("""
    [1] Extrato
    [2] Saldo
    [3] Deposito
    [4] Saque
    [5] Cadastro cliente
    [6] Criar conta
    [7] Listar contas
    [8] Sair

    """)
    
def sacar(*, valor_sacado, saldo_conta, saques):
    
    if valor_sacado <= 0:
        print("Valor inválido! Tente novamente.")
        return saldo_conta, None
    
    elif saldo_conta < valor_sacado:
        print("Operação falhou! Saldo insuficiente.")
        return saldo_conta, None


    elif valor_sacado > 500:
        print("Operação falhou! Valor de saque solicitado excete o limite de R$ 500,00")
        return saldo_conta, None
    
    else:
        saldo_conta -= valor_sacado
        hora = tm.localtime(tm.time())
        hora = f"{hora.tm_hour}:{hora.tm_min}:{hora.tm_sec}"
        print(f"Operação concluída com sucesso!\nSaldo atual: R$ {saldo_conta}")
        return saldo_conta, [dia, hora, valor_sacado, "saque"]

def depositar(saldo_conta, valor_depositado, /):
    
    if valor_depositado <= 0:
        print("Operação falhou! Valor inválido")
    else:
        saldo_conta += valor_depositado
        hora = tm.localtime(tm.time())
        hora = f"{hora.tm_hour}:{hora.tm_min}:{hora.tm_sec}"
        print(f"Operação concluída com sucesso!\nSaldo atual: R$ {saldo_conta}")
        return saldo_conta, [dia, hora, valor_depositado, "deposito"]
        
def exibir_extrato(saldo_conta, /, *, historico):
    
    if not historico: print("Não constam movimentações")
    
    else:
        print("\nSeu extrato:\n")
        
        for d, h, v, op in historico: 
            print(f"{d}, {h}, {op} no valor de: R$ {v:.2f}")
        
        print(f"\nSaldo atual: R$ {saldo_conta:.2f}")
        
        tm.sleep(5)
    
def cadastro_cliente(user, cpf_user, clientes):
    
    if not cpf_user in [i['cpf'] for i in clientes]:
        print("Novo usuário cadastrado com sucesso")
        return {"nome": user, "cpf": cpf_user, "conta": None}
    else:
        print("Operação falhou! O CPF já possui cadastro.")
        return None
    
def criar_conta(lista_clientes,cpf_cliente, lista_contas, ag):

    if not cpf_cliente in [i["cpf"] for i in lista_clientes]:
        print("Operação falhou! O usuário não está cadastrado na base de dados")
        return None, None
    
    else:

        for cliente in lista_clientes:

            if cliente["cpf"] == cpf_cliente and not cliente["conta"]:
                
                nova_conta = len(lista_contas) + 1
                digito_conta = randint(0,9)

                cliente["conta"] = f"{ag} {nova_conta}-{digito_conta}"

                lista_contas.append([cliente["nome"],cliente["cpf"], cliente["conta"]])

                print("Conta criada com sucesso")
                print(f"Nome: {cliente['nome']}, CPF: {cliente['cpf']}, Conta: {cliente['conta']}")
                return lista_contas, lista_clientes
            
        print("Cliente já possui conta vinculada")
        return None, None
        
def listar_contas(lista_contas):

    if not lista_contas:
        print("Operação falhou! Não existem contas cadastradas")
    else:
        for conta in lista_contas:
            print(f"Cliente: {conta[0]}, Conta: {conta[2]}")

def main():
    
    AGENCIA = "001"
    MAX_SAQUES = 3
    
    extrato = []
    saldo = 0
    saques_efetuados = 0
    limiteSaque = 500
    clientes = []
    contas = []

    while (True):
        menu()
        ope = input("Digite a opção desejada: ")

        if ope == '1':

            exibir_extrato(saldo, historico=extrato)
                
                
        elif ope == '2': print(f"Seu saldo em {dia}:\nR$ {saldo:.2f}")


        elif ope == '3':

            valor = float(input("Digite o valor a ser depositado: "))

            saldo, transacao = depositar(saldo, valor)
            extrato.append(transacao)


        elif ope == '4':

            if saques_efetuados >= 3: print("Operação falhou! Número de saques diários excedidos")
            
            else:
                
                valor = float(input("Digite o valor a ser sacado: "))
                
                saldo, transacao = sacar(valor_sacado= valor, saques= saques_efetuados, saldo_conta= saldo)
                if transacao: 
                    extrato.append(transacao)
                    saques_efetuados += 1
                
        elif ope == '5':
            
            new_user_name = input("Digite seu nome:\n")
            new_user_cpf = input("Digite seu cpf:\n")

            cadastro_novo_user = cadastro_cliente(new_user_name, new_user_cpf, clientes)
            if cadastro_novo_user:
                clientes.append(cadastro_novo_user)
            
        elif ope == '6':
            
            user_cpf = input("Digite o cpf do cliente que deseja criar conta:\n")
            nova_lista_conta, nova_lista_clientes = criar_conta(clientes, user_cpf, contas, AGENCIA)
            if nova_lista_conta and nova_lista_clientes:
                contas = nova_lista_conta
                clientes = nova_lista_clientes
            
        elif ope == '7':
            listar_contas(contas)

        elif ope == '8':
            break

        else:
            print("Operação inválida")

main()
