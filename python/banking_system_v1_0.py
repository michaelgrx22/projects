bemvindo = 'Seja bem-vindo à DIO Bank'
print(bemvindo.center(41, '-'))
print('Por favor, selecione uma das opções abaixo:')
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_cliente = input('Por favor informe o valor do seu depósito: ')

        if valor_cliente.isdigit():
            valor_cliente = float(valor_cliente)
            
            if valor_cliente <= 0:
                print('O valor informado não é válido.')
                continue
            else:
                saldo += valor_cliente
                extrato += f'Depósito: R$ {valor_cliente:.2f}\n'
        else:
            print('O valor informado não é válido')

    elif opcao == 's':

        valor_cliente = input('Por favor, informe o valor que deseja sacar: ')

        if valor_cliente.isdigit():
            valor_cliente = float(valor_cliente)

            if numero_saques >= LIMITE_SAQUES:
                print('Limite de saques diário excedido.') 

            elif valor_cliente > saldo:
                print('Seu saldo é insuficiente para a operação') 

            elif valor_cliente > limite:
                print('Limite máximo de R$ 500,00 excedido.')
            
            else:
                saldo -= valor_cliente
                extrato += f'Saque: R$ {valor_cliente:.2f}\n'
                numero_saques += 1
        else:
            print('Por favor, informe um valor válido')

    elif opcao == 'e':
        print('\n================ EXTRATO ================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('==========================================')
    
    elif opcao == 'q':
        break

    else:
        print('Opção inválida, por favor tente novamente!')



            

        
        

        
        