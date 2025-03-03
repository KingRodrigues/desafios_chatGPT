print('='*6, 'DESAFIO 055', '='*6)
# faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for p in range (1, 6):
    peso_ps = float(input(f'Digite o peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso_ps
        menor = peso_ps
    else:
        if peso_ps > maior:
            maior = peso_ps
        if peso_ps < menor:
            menor = peso_ps
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')
