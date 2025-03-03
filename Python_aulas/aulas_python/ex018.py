print('='*6,'DESAFIO 018','='*6)
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
'''Importando a biblioteca'''

a = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(a))
print('Valor do Seno: {:.2f}'.format(seno))
cosseno = math.cos(math.radians(a))
print('Valor do Cosseno: {:.2f}'.format(cosseno))
tangente = math.tan(math.radians(a))
print('Valor do Tangente: {:.2f}'.format(tangente))

''' from math import radians, sin, cos, tan
a = float(input('Digite o ângulo: '))
seno = sin(radians(a))
print('Valor do Seno: {:.2f}'.format(seno))
cosseno = cos(radians(a))
print('Valor do Cosseno: {:.2f}'.format(cosseno))
tangente = tan(radians(a))
print('Valor do Tangente: {:.2f}'.format(tangente))
'''