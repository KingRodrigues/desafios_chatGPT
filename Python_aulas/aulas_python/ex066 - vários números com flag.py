print('='*6, 'DESAFIO 066', '='*6)
# crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o usuário digitar o valor
# 999, que é a condição de parada. no final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

c = 0
v = 0

while True:
    n = int(input('Digite um valor [999 para parar]: '))
    if n == 999:
        break
    v += n
    c += 1
print(f'A soma dos {c} valores foi {v}!')
