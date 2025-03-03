print('='*6, 'DESAFIO 067', '='*6)
# faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# o programa será interrompido quando o número solicitado for negativo.

while True: 
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Programa encerrado!')
        break
    print('-'*30)
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
    print('-'*30)
    