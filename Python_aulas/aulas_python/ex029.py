import time
print('='*6, 'DESAFIO 029', '='*6)
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

velocidade = int(input('Qual é a velocidade atual do carro? '))
limite = 80
if velocidade > 80:
    print('O limite máximo de velocidade é 80Km/h!')
    print('A multa está sendo aplicada...')
    time.sleep(1)
    print('Valor da multa aplicada! Valor: R$ {}'.format((velocidade - limite) * 7))

else:
    print('Dirija com cuidado e tenha um ótimo dia!')
