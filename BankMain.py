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
    [5] Nova conta
    [6] Listar contas
    [7] Sair

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
        
def exibir_extrato(historico, saldo_conta):
    
    print("\nSeu extrato:\n")
    
    for d, h, v, op in historico: 
        print(f"{d}, {h}, {op} no valor de: R$ {v:.2f}")
    
    print(f"\nSaldo atual: R$ {saldo_conta:.2f}")
    
    tm.sleep(5)
    
def gerar_conta():
    
    numero_conta = randint(10000, 99999)
    digito_conta = randint(0, 9)
            
    return f"{numero_conta}-{digito_conta}"
    
def listar_contas(lista_contas):
    for cliente, numero_conta in lista_contas:
        print(f"Cliente: {cliente}, conta: {numero_conta}")
        
def main():
    
    AGENCIA = "001"
    MAX_SAQUES = 3
    
    extrato = []
    saldo = 0
    saques_efetuados = 0
    limiteSaque = 500
    contas = []

    while (True):
        menu()
        ope = input("Digite a opção desejada: ")

        if ope == '1':

            if not extrato: print("Não constam movimentações")

            else: exibir_extrato(extrato, saldo)
                
                
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
            
            new_user = input("Digite seu nome:\n")
            
            contas.append([new_user, gerar_conta()])
            
        elif ope == '6':
            
            listar_contas(contas)
            
        elif ope == '7':
            break

        else:
            print("Operação inválida")

main()
