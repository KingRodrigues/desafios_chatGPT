print('='*6, 'DESAFIO 037', '='*6)
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal.
print('')

n = int(input('Digite um número inteiro: '))
print("""[ 1 ] conversão para binário
[ 2 ] conversão para octal
[ 3 ] conversão para hexadecimal""")
e = int(input('Sua opção: '))
if e == 1:
      print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif e == 2:
      print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif e == 3:
      print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
      print('OPÇÃO INVALIDA!')
