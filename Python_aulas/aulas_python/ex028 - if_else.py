import time

print('='*6, 'DESAFIO 028', '='*6)
#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print('=-'*25)
print('Vamos brincar de adivinhação?')
print('=-'*25)

bot = random.randint(1, 6)
player = int(input('Eu escolhi um número de 1 a 6, tente adivinhar: '))
print('Processando...')
time.sleep(1)
if player == bot:
    print('Parabéns, você acertou!')
else:
    print('Você errou! Eu escolhi o número {}!'.format(bot))
