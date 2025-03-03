print('='*6, 'DESAFIO 063', '='*6)
# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.
# ex:
# 0 > 1 > 1 > 2 > 3 > 5 > 8

print('=' * 20)
print('Sequência de Fibonacci')
print('=' * 20)

n = int(input('Quantos termos você quer mostrar? '))
print('~'*20)
t1 = 0 # primeiro termo
t2 = 1 # segundo termo
print(f'{t1}  -->  {t2}', end='')

cont = 3 # contador

while cont <= n: # enquanto o contador for menor ou igual ao n
    t3 = t1 + t2 # terceiro termo
    print(f' -->  {t3}', end='')
    t1 = t2 # t1 vira t2
    t2 = t3 # t2 vira t3
    cont += 1 # contador recebe ele +1
print(' =x= FIM')
