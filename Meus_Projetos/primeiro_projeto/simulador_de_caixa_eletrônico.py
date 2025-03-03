saldo_inicial = 1000

def depositar():
    global saldo_inicial
    try:
        deposito = int(input('Digite o valor a depositar: '))
        if deposito <= 0:
            print('Valor inválido! Digite um número positivo.')
        else:
            saldo_inicial += deposito
            print(f'Deposito realizado com sucesso! Saldo atual: R$ {saldo_inicial}')
    except ValueError:
        print('Entrada inválida!')
def sacar():
    global saldo_inicial
    try:
        saque = int(input('Digite o valor a sacar: '))
        if saque <= 0:
            print('Valor inválido! Digite um número positivo.')
            return
        if saque > saldo_inicial:
            print(f'Saldo insuficiente! Seu saldo atual é de R$ {saldo_inicial}')
            return
        if saque <= saldo_inicial:
            saldo_inicial -= saque
            print(f'Saque no valor de R$ {saque} realizado com sucesso! Saldo atual: R$ {saldo_inicial}')
        else:
            print(f'Saldo insuficiente! Você tem apenas R$ {saldo_inicial}.')
            return
    except ValueError:
        print('Entrada inválida!')
def transferir():
    global saldo_inicial
    try:
        transferencia = int(input('Qual o valor que deseja transferir? '))
        if transferencia <= 0:
            print('Valor inválido! Digite um número positivo.')
        if transferencia > saldo_inicial:
            print(f'Valor inválido! Seu saldo atual é de R$ {saldo_inicial}')
            return
        if transferencia <= saldo_inicial:
            saldo_inicial -= transferencia
            print(f'Transferência realizada com sucesso! Saldo atual: R$ {saldo_inicial}')
        else:
            print(f'Valor insuficiente! Saldo atual: R$ {saldo_inicial}')
    except ValueError:
        print(f'Entrada inválida!')
def verificar():
    print(f'Saldo atual: R$ {saldo_inicial}')
def sair():
    print('Obrigado por usar o caixa eletrônico! Até logo!')

opcoes = {
    1: depositar,
    2: sacar,
    3: transferir,
    4: verificar,
    5: sair
}

# menu
while True:
    print('\n', '-=' * 30)
    print("""
        [1] Depositar dinheiro
        [2] Sacar dinheiro
        [3] Transferir para outra conta
        [4] Verificar saldo
        [5] Sair do programa
    """)
    print('\n', '-=' * 30)

    try:
        usuario = int(input('Escolha uma opção: '))
        if usuario in opcoes:
             opcoes[usuario]()
             if usuario == 5:
                  break
        else:
            print('Opção inválida! Escolha entre 1 a 5.')             
    except ValueError:
        print('Opção inválida! Escolha entre 1 a 5.')
        continue
