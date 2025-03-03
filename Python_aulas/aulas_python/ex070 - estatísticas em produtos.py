print('='*6, 'DESAFIO 070', '='*6)
# crie um programa que leia o nome e o preço de vários produtos. o programa deverá perguntar se o usuário vai continuar. no final, mostre:
# a) qual é o total gasto na compra.
# b) quantos produtos custam mais de R$ 1000.
# c) qual é o nome do produto mais barato.

""" 

g = p = 0

while True:
    nome = str(input('Produto: ')).capitalize()
    valor = int(input('Preço: R$ '))
    g += valor

    if valor >= 1000:
        p += 1
    if p == 1:
        barato = nome
        preço = valor
    if valor < preço:
        barato = nome

    resp = str(input('Deseja continuar? [s/n]: '))
    if resp != 's':
        break

print(f'Total Gasto: R$ {g}')
print(f'Quant. acima de R$ 1000: {p}')
print(f'O produto mais barato foi: {barato}')

"""

total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$ '))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
        
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
   
print('{:-^40}'.format(' Fim do Programa '))
print(f'O total de compra foi de R$ {total:10.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi: {barato} com o preço de R$ {menor}')
