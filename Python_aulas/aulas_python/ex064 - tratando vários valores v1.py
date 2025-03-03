print('='*6, 'DESAFIO 064', '='*6)
# crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

from time import sleep

print('Digite um valor ou " 999 " para finalizar')
print('~'*20)


c = s = n = 0

while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    c += 1 
    s += n

print(f"""
    Quant. Números Digitados: {c}
    Soma entre os Números: {s}
""")
sleep(0.5)

if n == 999:
    print('O programa será encerrado...')
    sleep(1.5)

print('PROGRAMA ENCERRADO!')
sleep(1)
