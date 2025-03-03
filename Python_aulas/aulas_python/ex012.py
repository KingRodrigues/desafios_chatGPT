print('====== DESAFIO 012 ======')
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input('Qual o valor total do produto? R$ '))
d = p * 5 / 100
v = p - d
print('O valor do produto com 5% de desconto é: R$ {:.2f}'.format(v))
