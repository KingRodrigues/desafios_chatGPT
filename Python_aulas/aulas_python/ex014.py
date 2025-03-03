print('='*6, 'DESAFIO 014', '='*6)
#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = int(input('Qual a temperatura em Cº? '))
f = (c * 9/5) + 32
print('—'*10)
print('  {:.0f} Cº'.format(c))
print('  {:.0f} ºF'.format(f))
print('—'*10)
