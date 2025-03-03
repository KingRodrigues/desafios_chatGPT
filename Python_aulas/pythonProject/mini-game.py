import random
print('='*44)
#Jogadores
player1 = input('Jogador 1 - Enter to name: ')
player2 = input('Jogador 2 - Enter to name: ')
inic1 = random.randint(1, 20)
inic2 = random.randint(1, 20)
print('==== Iniciativa ==== || ==== Iniciativa ====')
print('{: ^20} || {:^20}'.format(player1, player2))
print('{: ^20} || {:^20}'.format(inic1, inic2))
print('='*44)

if inic1 >= inic2:
    print('{} rola 1d20 de atk'.format(player1))
    atk1 = random.randint(1, 20)
    print('{: ^44}'.format(atk1))
    print('{} rola 1d20 de def'.format(player2))
    def2 = random.randint(1, 20)
    print('{: ^44}'.format(def2))
    if atk1 > def2:
        print('{} recebe {} de dano.'.format(player2, (def2-atk1)))
    else:
        print('{} defendeu!'.format(player2))

else:
    print('{} rola 1d20 de atk:'.format(player2))
    atk2 = random.randint(1, 20)
    print('{: ^44}'.format(atk2))
    print('{} rola 1d20 de def'.format(player1))
    def1 = random.randint(1, 20)
    print('{: ^44}'.format(def1))
    if atk2 > def1:
        print('{} recebe {} de dano.'.format(player1, (def1-atk2)))
    else:
        print('{} defendeu!'.format(player1))

print('='*44)