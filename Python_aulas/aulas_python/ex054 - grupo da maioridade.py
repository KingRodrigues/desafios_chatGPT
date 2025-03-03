print('='*6, 'DESAFIO 054', '='*6)
# crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostrer quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

menor = 0
c = 1
maior = 0

data = date.today().year

for x in range(1, 8):
    aniv = int(input(f'Ano de Nascimento da {x}ª '))
    idade = data - aniv
    if idade <= 17:
        menor = menor + 1
    else:
        maior = maior + 1
print(f'{menor} são menores de idade\n{maior} são maiores de idade')
