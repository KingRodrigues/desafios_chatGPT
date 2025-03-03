print('='*6, 'DESAFIO 052', '='*6)
# faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Digite um número: '))
tot = 0

for c in range (1, num + 1, 1):
    if num % c == 0:
        print('\033[33m', end=' ') # cor amarelo
        tot += 1
    else:
        print('\033[31m', end=' ') # cor vermelha
    print(f'{c}', end=' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes') # zerar a cor
if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
    