menu = """ 
            Menu Conta

        [1] Deposito
        [2] Saque
        [3] Extrato
        [4] Sair

            Bank System
"""

saldo = 0
limite_saque = 500
extrato = " "
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    if valor >= 1:
        return print('Valor Depositado: ',valor)
               
while True:

    opção = input(menu)
    
    if opção == "1":
        valor = float(input('Digite um valor: ',))

        if valor > 0:
            print(f'Valor Depositado : R${valor:.2f}')
            saldo += valor
            extrato += f'Deposito : R$ {valor:.2f}\n'
            print(f'Saldo Atual: R$ {saldo:.2f}')

        else:
            print("O deposito falhou : Valor Invalido!")
    
    elif opção == "2":
        saque = float(input('Digite um valor de saque: '))
        
        saldo_insuficiente = saque > saldo

        exedeu_limite = saque > limite_saque
        
        exedeu_numero_saques= numero_saques >= LIMITE_SAQUES

        if exedeu_limite:
            print("Valor maior que o limite de saque")

        elif exedeu_numero_saques:
            print(f"Numero de saques exedido, numero de saques realizados:{LIMITE_SAQUES}")

        elif saque > 0:
            
            saldo -= saque
            extrato += f' Saque : - R$ {saque:.2f}\n'
            numero_saques += 1

            print(f'Valor Sacado : {saque:.2f}')

        else:
            print("Falha:Valor invalido informado")
    
    elif opção == "3":

        print("\n-----------------Extrato-----------------\n")
        print("\nSem movimentações." if not extrato else extrato)
        print(f'\nSaldo Atual : R$ {saldo:.2f}')
        print("\n---------------Bank system---------------")
        
    elif opção == "4":
        print('''Obrigado por usar nosso serviço!!!
                 Saindo....''')
        
        break

    else:
        print("Opção invalida")

            

                  


        
        
       
        

