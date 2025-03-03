print('='*6, 'DESAFIO 060', '='*6)
# faça um programa que leia um número qualquer e mostre o seu fatorial.

# ex:
# 5! = 5x4x3x2x1 = 120

from math import factorial

n = int(input('>>>> Digite um número: '))
f = factorial(n)
print(f'Calculando {n}! = ', end='')
for n in range(n, 0, -1):
    print(f'{n}', end='')
    if n > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
print(f)

# ===============================================

# while, if, elif e else

'''

n = int(input('Digite um número: '))
print(f'Calculando {n}! = ', end='')
c = n
f = 1

while c > 1:
    if c > 1:
        print(f'{c} x ', end='')
        f *= c
        c -= 1
    elif c == 1:
        print(f'{c}', end='')
        f *= c
        c -= 1
    else:
        break
print('1 = ', end='')
print(f'{f}')

'''

# ================================================

'''

n = int(input('>>> Escolha um número: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

'''