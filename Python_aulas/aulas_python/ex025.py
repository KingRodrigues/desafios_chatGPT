print('='*6, 'DESAFIO 025', '='*6)
#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA!" no nome.

name = input('Digite o nome completo: ').lower()
if 'silva' in name:
    print('Você possuí "Silva" no nome!')
else:
    print('Você não possuí "Silva" no nome!')
