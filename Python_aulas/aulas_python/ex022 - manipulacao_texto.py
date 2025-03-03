print('='*6, 'DESAFIO 022', '='*6)
#Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao total (sem considerar o espaços)
# - Quantas letras tem o primeiro nome


name = str(input('Nome Completo: '))
print('Todas as letras Maiúsculas: ', name.upper())
print('Todas as letras Minúsculas: ', name.lower())
print('Quantas letras ao total? ', len(name) - name.count(' '))
dv = name.split()[0]
print('Quantas letras tem o primeiro nome? ', len(dv))
