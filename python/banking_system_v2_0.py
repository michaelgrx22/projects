def menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato 
[q] Sair


=> """
    return input(menu)

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()

        if opcao == 'd':
            valor_cliente = input('Por favor informe o valor do seu depósito: ')

            saldo, extrato = depositar(saldo, valor_cliente, extrato)

        elif opcao == 's':

            valor_cliente = input('Por favor informe o valor que deseja sacar: ')
            saldo, extrato, numero_saques = sacar(saldo=saldo,valor_cliente=valor_cliente,extrato=extrato,limite=limite,numero_saques=numero_saques,limite_saques=LIMITE_SAQUES)

            

        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 'q':
            break

        else:
            print('Opção inválida, por favor tente novamente!')

def depositar(saldo, valor_cliente,extrato, /):

    if valor_cliente.isdigit():
        valor_cliente = float(valor_cliente)
                
        if valor_cliente <= 0:
            print('Por favor informe um valor válido.')
            
        else:
            saldo += valor_cliente
            extrato += f'Depósito: R$ {valor_cliente:.2f}\n'
    else:
        print('Por favor informe um valor válido.')
    return saldo, extrato

def sacar (*, saldo, valor_cliente,extrato, limite,numero_saques, limite_saques):
    if valor_cliente.isdigit():
        valor_cliente = float(valor_cliente)

        if numero_saques >= limite_saques:
            print('Limite de saques diário excedido.') 

        elif valor_cliente > saldo:
            print('Seu saldo é insuficiente para a opereção de saque.') 

        elif valor_cliente > limite:
            print('O valor informado excede o limite para a operação.')
                
        else:
            saldo -= valor_cliente
            extrato += f'Saque: R$ {valor_cliente:.2f}\n'
            numero_saques += 1
            print('Saque realizado com sucesso!')
    else:
        print('O valor informado é inválido, tente novamente!')
    return saldo, extrato, numero_saques

def exibir_extrato(saldo,/, *,extrato):
    print('\n================ EXTRATO ================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('==========================================')

main()


                

            
            

            
            