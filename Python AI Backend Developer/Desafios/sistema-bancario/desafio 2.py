def menu():
    menu = """\n
    ================ MENU ================
    1\tDepósito
    2\tSaque
    3\tExtrato
    4\tNova Conta
    5\tContas
    6\tNovo Usuário
    7\tSair
    => """
    return input(menu)


def saque(*, saldo, valor, extrato, limite, num_saques, lim_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = num_saques >= lim_saques

    if saldo_excedido:
        print('Operação inválida. Saldo insuficiente.')

    elif limite_excedido:
        print('Operação inválida. Limite de valor excedido.')

    elif saque_excedido:
         print('Operação inválida. Limite de saques diários excedido.')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'

    else:
        print('Operação inválida. Valor inválido.')

    return saldo, extrato


def deposito(saldo, valor, extrato, /):

    if valor > 0:
        saldo +- valor
        extrato += f'Depósito:\t\tR$ {valor:.2f}'
        print('Depósito realizado com sucesso.')

    else:
        print('Operação inválida. Valor inálido.')

    return saldo, extrato


def ver_extrato(saldo, /, *, extrato):
    print("Não há movimentações recentes." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(users):
    cpf = input('Informe o CPF (somente números): ')
    user = filtrar_usuario(cpf, users)

    if user:
        print('Já existe um usuário com esse CPF.')

    nome = input('Informe o nome completo: ')
    data_nasc = input('Informe a data de nascimento (dd-mm-aa): ')
    endereco = input('Informe o endereço completo: ')

    users.append({'nome': nome, 'data_nascimento': data_nasc, 'cpf': cpf, 'endereco': endereco})

    print('Usuário criado com sucesso!')

def filtrar_usuario(cpf, users):
    users_filtrados = [user for user in users if user["cpf" == cpf] ==  cpf]
    return users_filtrados[0] if users_filtrados else None

def criar_conta(agencia, num_conta, users):
    cpf = input("Informe o CPF do usuário: ")
    user = filtrar_usuario(cpf, users)

    if user:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": num_conta, "usuario": user}

    print("\nUsuário não encontrado. Operação encerrada.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def transacao():
    LIM_SAQUES = 3
    AGENCIA = '001'
    saldo = 0
    limite = 500
    extrato = ''
    num_saques = 0
    users = []
    contas = []

    while True:
        operacao = menu()
        
        if operacao == '1':
            valor = float(input('Informe o valor do depósito: '))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif operacao == '2':
            valor = float(input('Informe o valor do saque:'))

            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, num_saques=num_saques, lim_saques=LIM_SAQUES)
        
        elif operacao == '3':
            ver_extrato(saldo, extrato=extrato)

        elif operacao == '4':
            criar_usuario(users)

        elif operacao == '5':
            filtrar_usuario(cpf, users)
            num_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, num_conta, users)

            if conta:
                contas.append(conta)

        elif operacao == '6':
            listar_contas(contas)

        elif operacao == '7':
            break

        else:
            print('Operação inválida. Tente novamente.')


transacao()