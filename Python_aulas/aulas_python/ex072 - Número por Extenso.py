print('='*6, 'DESAFIO 075', '='*6)
# crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20), e mostrará esse valor por extenso.

from time import sleep

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    while True:
        num = int(input('Digite um número entre 00 e 10: '))
        if 0 <= num <= 10: # se não for entre 0 e 10, ele repete
            break
        print('Número Inválido! Tente novamente.')
    print(f'Você digitou o número {lista[num]}')
    sleep(1)

    while True:
        resp = input('Deseja continuar? [s/n]: ').strip().lower()
        if resp in 'sn':
            break
        print('Resposta Inválida! Digite "S" ou "N".')

    if resp == 'n':
        print('Encerrando o programa...')
        sleep(1)
        break
