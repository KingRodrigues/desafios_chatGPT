print('='*6, 'DESAFIO 071', '='*6)
# crie um programa que simule o funcionamento de um caixa eletrônico. no inicio, pergunte ao usuário
# qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# obs: considere que o caixa possui cédulas de R$ 50, R$20, R$10, R$ 2 e R$ 1.

print('='*30)
print(f'{'Branco CEV':^30}')
print('='*30)

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50 # cédulas
totcéd = 0 # total cédulas
while True: # loop infinito
    if total >= céd: # se o total maior ou igual céd
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R$ {céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
