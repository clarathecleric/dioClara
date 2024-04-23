
menu = '''
1 Depósito
2 Saque
3 Extrato
4 Sair

==> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

print('Olá! Bem-vindo(a) ao DioBank. Utilize o menu abaixo para selecionar a sua operação:')

while True:

    operacao = input(menu)

    if operacao == '1':
        valor = float(input('Informe o valor do depósito: '))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        
        else:
            print("A operação falhou! Valor inválido.")
        
    elif operacao == '2':
        valor = float(input('Informe o valor do saque:'))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques > LIMITE_SAQUES

        if saldo_excedido:
            print('A operação falhou! Saldo insuficiente.')

        elif limite_excedido:
            print('A operação falhou! Limite de valor excedido.')

        elif saque_excedido:
            print('A operação falhou! Limite de saques diários excedido.')

    elif operacao == '3':
        print("\n================ EXTRATO ================")
        print("Não há movimentações recentes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif operacao == '4':
        print('Obrigado por usar o DioBank! Volte sempre.')
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")