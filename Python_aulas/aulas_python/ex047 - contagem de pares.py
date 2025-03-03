print('='*6, 'DESAFIO 047', '='*6)
# crie um programa que mostre na tela todos os números pares
#que estão no intervalo entre 1 e 50

from time import sleep

print('Números pares!')
for numeros in range(0, 51, 2):
    print(numeros, end=', ')
print('Esses são os números pares!')
sleep(1)
