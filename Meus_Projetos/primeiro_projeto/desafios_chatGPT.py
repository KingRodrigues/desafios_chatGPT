# Desenvolvido por Adriano Júnio Rodrigues
# Data: 25/02/2025

from time import sleep
from random import randint

# facilitadores
def menu_padrão():
    while True:
        try:
            return int(input('Digite um número: '))
        except ValueError:
            print('.*.Opção Inválida! Digite um número válido.*.')
def sair():
            print()
            print('Obrigado por jogar! Encerrando programa...')
            sleep(1)

# JOGOS
def par_ou_impar():
    while True:
        player = menu_padrão()
        if player == 0:
            sair()
            break
        elif player % 2 == 0:
            print(f'O número {player} é PAR.')
        else:
            print(f'O número {player} é ÍMPAR.')

def contagem_regressiva():
    while True:
        player = menu_padrão()
        if player == 0:
            sair()
            break
        else:
            for p in range(player, -1, -1):
                print(p)
                sleep(1)
    
def soma_dos_numeros():
    while True:
        player = menu_padrão()
        
        if player == 0:
            sair()
            break
        
        soma = sum(range(1, player + 1))
        print(f'A soma de 1 até {player} é {soma}.')

def maior_e_menor_numero():
    while True:
        primeiro_numero = menu_padrão()
        maior = menor = primeiro_numero

        if primeiro_numero == 0:
            sair()
            break
        else:
            for p in range(4):
                player = menu_padrão()
                if player > maior:
                    maior = player
                if player < menor:
                    menor = player
            print(f'O maior número é {maior}')
            print(f'O menor número é {menor}')

def adivinhacao():
    cpu = randint(1, 10)

    while True:
        try:
            player = int(input('Tente adivinhar o número entre 1 e 10: '))
        except ValueError:
            print('.*.Opção Inválida! Digite um número válido.*.')
            continue
        if player == 0:
            sair()
            break
        elif player == cpu:
            print('Parabéns! Você acertou.')
            sleep(1)
            break
        elif player < 1 or player > 10:
            print('Opção inválida! Tente novamente.')
            print()
            continue
        else:
            print('Errou! Tente novamente.')
        
opcoes = {
    1: par_ou_impar,
    2: contagem_regressiva,
    3: soma_dos_numeros,
    4: maior_e_menor_numero,
    5: adivinhacao,
    6: sair
}

# MENU
while True:
    print()
    print('\n' + '-=' * 30)
    print("""
                OPÇÕES
      [1] Par ou Ímpar
      [2] Contagem Regressiva
      [3] Soma dos Números
      [4] Maior e Menor Número
      [5] Adivinhação
      [6] Sair
""")
    print('\n' + '-=' * 30)

    try:
        make_your_choice = int(input('Escolha uma opção entre 1 a 6: '))
        if make_your_choice in opcoes:
            opcoes[make_your_choice]()
            if make_your_choice == 6:
                break
        else:
            print('.*. Opção inválida! Digite um número entre 1 e 6 .*.')
    except ValueError:
        print('.*. Opção inválida! Digite um número entre 1 e 6 .*.')
        continue
print()