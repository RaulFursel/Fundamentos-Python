def menu():
    menu = """\n 
            Menu Conta

        [1]\tDeposito
        [2]\tSaque
        [3]\tExtrato
        [4]\tNova conta
        [5]\tListar contas
        [6]\tNovo usuário
        [7]\tSair

            Bank System
"""
    return input(menu)

def deposito(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        print(f'Valor Depositado : R${valor:.2f}')
        extrato += f'Deposito :\t R$ {valor:.2f}\n'
        print(f'Saldo Atual: R$ {saldo:.2f}')
    else:
        print("O deposito falhou : Valor Invalido!")
    
    return saldo, extrato

def sacar(*,saldo,valor,extrato,limite_saque,numero_saques,LIMITE_SAQUES):
    saldo_insuficiente = valor > saldo
    exedeu_limite = valor > limite_saque
    exedeu_numero_saques= numero_saques >= LIMITE_SAQUES

    if saldo_insuficiente:
        print(f'Saldo Insuficiente para Saque')
    
    elif exedeu_limite:
        print("Valor maior que o limite de saque")

    elif exedeu_numero_saques:
        print(f"Numero de saques exedido, numero de saques realizados:{LIMITE_SAQUES}")

    elif valor > 0:
            
        saldo -= valor
        extrato += f'Saque :\t\t-R$ {valor:.2f}\n'
        numero_saques += 1

        print(f'Valor Sacado : {valor:.2f}')
    
    else:
        print("Falha:Valor invalido informado")
    
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("\n-----------------Extrato-----------------\n")
    print("\nSem movimentações." if not extrato else extrato)
    print(f'\nSaldo Atual : R$ {saldo:.2f}')
    print("\n---------------Bank system---------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'  
    saldo = 0
    limite_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios= []
    contas = []
      

    while True:
        opção = menu()
        
        if opção == '1':
            valor = float(input("Insira o valor para deposito:"))
            saldo, extrato = deposito(saldo,valor,extrato) 
        elif opção == '2':
            valor = float(input('Insira o valor para saque:'))
            
            saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_saque=limite_saque,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )
        
        elif opção == '3':
            exibir_extrato(saldo,extrato=extrato)
        
        elif opção == "6":
            criar_usuario(usuarios)

        elif opção == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opção == "5":
            listar_contas(contas)
            
        elif opção == '7':
            print('''Obrigado por usar nosso serviço!!!
                    Saindo....''')
            
            break

        else:
            print("Opção invalida")

main()
            

                  


        
        
       
        

