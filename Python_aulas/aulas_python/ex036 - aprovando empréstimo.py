print('='*6, 'DESAFIO 036', '='*6)
#Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. O programa vai
# perguntar o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.
print('')

casa = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o salário do comprador? R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa R$ {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R$ {:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
