import time as tm
import sys

dia = tm.localtime(tm.time())
dia = f"{dia.tm_mday}/{dia.tm_mon}/{dia.tm_year}"

extrato = []
saldo = float(0)
saques = 0
MAX_SAQUES = 3
limiteSaque = 500

menu = """
[1] Extrato
[2] Saldo
[3] Deposito
[4] Saque
[5] Sair

"""

while (True):
    print(menu)
    ope = int(input("Digite a opção desejada: "))

    if ope == 1:

        if not extrato: print("Não constam movimentações")

        else:
            print("\nSeu extrato:\n")
            for d, h, v, op in extrato: print(f"{d}, {h}, {op} no valor de: R$ {v:.2f}")
            print(f"\nSaldo atual: R$ {saldo:.2f}")
            tm.sleep(5)


    elif ope == 2:
        print(f"Seu saldo {dia}:\nR$ {saldo:.2f}")


    elif ope == 3:

        valor = float(input("Digite o valor a ser depositado: "))

        if valor <= 0:
            print("Operação falhou! Valor inválido")

        else:
            saldo += valor
            hora = tm.localtime(tm.time())
            hora = f"{hora.tm_hour}:{hora.tm_min}:{hora.tm_sec}"
            extrato.append([dia, hora, valor, "deposito"])
            print("Operação concluída com sucesso!")


    elif ope == 4:

        if saques >= 3:
            print("Operação falhou! Número de saques diários excedidos")
        
        else:
            valor = float(input("Digite o valor a ser sacado: "))

            if valor <= 0:
                print("Valor inválido! Tente novamente.")

            elif valor > 500:
                print("Operação falhou! Valor de saque solicitado excete o limite de R$ 500,00")


            elif saldo < valor:
                print("Operação falhou! Saldo insuficiente.")

            else:
                saldo -= valor
                hora = tm.localtime(tm.time())
                hora = f"{hora.tm_hour}:{hora.tm_min}:{hora.tm_sec}"
                extrato.append([dia, hora, valor, "saque"])
                print("Operação concluída com sucesso!")
                saques += 1

    elif ope == 5:
        break

    else:
        print("Operação inválida")


