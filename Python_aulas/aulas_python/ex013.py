print('====== DESAFIO 013 ======')
#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Qual o salário atual? R$ '))
p = (s / 100) * 15
a = s + p
print('O salário, com o reajuste de 15%, será alterado para R$ {:.2f}'.format(a))
