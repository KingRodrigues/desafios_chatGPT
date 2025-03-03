
# crie um programa que leia dois valores e mostre um menu na tela.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

# seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

escolha = 1
print('-='*10)
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('-='*10)
while escolha != 5:

    print('[1]: Somar\n[2]: Multiplicar\n[3]: Maior\n[4]: Novos números\n[5]: Sair')
    print('-='*10)
    escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        print(f'{n1} + {n2} = {n1+n2}')
        sleep(1)
    elif escolha == 2:
        print(f'{n1} x {n2} = {n1*n2}')
        sleep(1)
    elif escolha == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            sleep(1)
        else:
            print(f'{n2} é maior que {n1}')
            sleep(1)
    elif escolha == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        sleep(1)
    elif escolha == 5:
        print('Finalizando...')
        sleep(1.5)
    elif escolha >= 6:
        print('Opção Inválida!')
    print('-='*10)
print('FIM DO PROGRAMA!')
sleep(2)
