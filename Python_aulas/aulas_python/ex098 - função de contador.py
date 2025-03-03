# faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem.
# seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(i, f, c):
    if c < 0:
        c *= 1
    if c == 0:
        c = 1
    print(f'Contagem de {i} até {f} de {c} em {c}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) # flush desliga buffer pra contar
            sleep(0.5)
            cont += c
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= c
        print('FIM!')


# main
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')

ini = int(input('Inicio: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

contador(ini, fim, pas)
