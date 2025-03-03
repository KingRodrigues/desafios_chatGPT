print('='* 6, 'DESAFIO 062', '='*6)
# melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-='*10)

p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = p
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{t} -> ', end='')
        t += r
        cont += 1
    print('PAUSA!')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM!')