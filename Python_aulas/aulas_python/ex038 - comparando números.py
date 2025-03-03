print('='*6, 'DESAFIO 038', '='*6)
#Escreva um programa que leia dois números
# ninteiros e compare-os, mostrando na tela
# numa mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais
print('')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro número é maior!')
elif n2 > n1:
    print('O segundo número é maior!')
else:
    print('Não existe valor maior, os dois são iguais.')
