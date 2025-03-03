from random import randint

print('='*6,'DESAFIO 016', '='*6)
#Crie um programa que leia em um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#ex: Digite um número: 6.127, o número 6.127 tem parte inteira 6.

#importar funções matemáticas
import math
#Número real [float]
nr = float(input('Digite um valor: '))
#importar arredondamento para baixo
int = math.floor(nr)
#Imprimir na tela
print('A parte inteira de {} é {}.'.format(nr, int))
#print('A parte inteira de {} é {}.'.format(nr, math.trunc(nr))

#from math import trunc
#print('A parte inteira de {} é {}.'. format(nr, trunc(nr))

'''num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))'''