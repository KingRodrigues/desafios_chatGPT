print('='*6, 'DESAFIO 058', '='*6)
# melhore o jogo do Desafio 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogaddor vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

# from random import randint


# bot = randint(0, 10)
# c = 1

# print('Eu escolhi um número entre 0 e 10, tente adivinhar!')

# escolha = int(input('Escolha um número entre 0 e 10: '))
# while escolha != bot:
#     if escolha < bot:
#        op = 'maior'
#    else:
#        op = 'menor'
#    escolha = int(input(f'Você errou! O número que escolhi é {op}... Tente novamente: '))
#    c += 1
# print(f'Parabéns, você acertou!\nNúmero de tentativas: {c}')
 


from random import randint

escolha_cpu = randint(0, 10)
palpites = 1

print('Oi, eu sou o Teddy! Eu escolhi um número entre 0 e 10.')
acertou = False
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == escolha_cpu:
        acertou = True
    else:
        if jogador < escolha_cpu:
            print('Mais... tente mais uma vez.')
        elif jogador > escolha_cpu:
            print('Menos... tente mais uma vez.')
print(f'Acertou!\nNúmero de tentativas: {palpites}')
