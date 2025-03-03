print('='*6, 'DESAFIO 030', '='*6)
#Crie um program que leia um número inteiro e mostre na tela se ele é Par ou Impar.

escolha = int(input('Escolha um número inteiro: '))
if escolha % 2 == 0: #Se [escolha] tiver o resto de divisão 0 = par
    print('O número {} é par!'.format(escolha))
else:
    print('O número {} é impar!'.format(escolha))
