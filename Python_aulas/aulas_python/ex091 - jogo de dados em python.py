# crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. guarde esses resultados em um dicionário.
# no final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter 

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()

print(' Valores sorteados:')
for k, v in jogo.items(): # chave e valor [k, v]
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True ) # ordenar, se for 0 coloca em ordem de chave, se for 1 coloca em ordem de valor
print('-=' * 30)

print(' Ranking dos jogadores:')
for i, v in enumerate(ranking): # indice e valor [i, v]
        print(f'{i+1}º lugar: {v[0]} com {v[1]}')
        sleep(1)
