print('====== DESAFIO 10 ======')
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# US$ 1.00 == R$ 5,61

r = float(input('Quantos R$ você possuí? '))
us = (r / 5.67)
print('Você pode comprar US$ {:.2f}'.format(us))
