print('='*6, 'DESAFIO 027', '='*6)
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separado.
#Ex: Ana Maria de Souza
#Primeiro: Ana
#Último: Souza

name = input('Escreva seu nome completo: ')
print('Primeiro nome: ', name.split()[0])
print('Último nome: ', name.split()[-1])
