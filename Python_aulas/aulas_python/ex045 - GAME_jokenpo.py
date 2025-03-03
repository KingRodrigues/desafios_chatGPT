print('='*6, 'DESAFIO 045', '='*6)
#Crie um programa que faça o computador jogar jokenpô com você.

from random import *
import time

score_player = 0
score_bot = 0
score_empate = 0

while True: 
    lista = ['pedra', 'papel', 'tesoura']
    bot = choice(lista)
    print('=-'*20)
    print('Jokenpo - Regras: Pedra ganha de Tesoura, Tesoura ganha de Papel, Papel ganha de Pedra.')
    escolha = input('Faça a sua escolha: ').lower()

    print('JO!')
    time.sleep(1)
    print('KEN!')
    time.sleep(1)
    print('PO!')
    time.sleep(1)

    if escolha == bot:
        print('Bot: {} | Player: {} \nResultado: Empate!'.format(bot, escolha))
        score_empate = score_empate + 1

    elif (escolha == 'pedra') and (bot == 'papel') or (escolha == 'tesoura') and (bot == 'pedra') or (escolha == 'papel') and (bot == 'tesoura'):
        print('Bot: {} | Player: {} \nResultado: Derrota!'.format(bot, escolha))
        score_bot = score_bot + 1

    else:
        print('Bot: {} | Player: {} \nResultado: Vitória!'.format(bot, escolha))
        score_player = score_player + 1

    print('=-'*20)
    print(':=:-PLACAR-:=:\nPlayer: {}\nBot: {}\nEmpate: {}'.format(score_player, score_bot, score_empate))
    repetir = str(input('Deseja jogar novamente? [s/n]: ')).lower()
    if repetir != 's':
        break
