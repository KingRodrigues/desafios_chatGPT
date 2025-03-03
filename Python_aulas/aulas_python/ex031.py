print('='*6, 'DESAFIO 031', '='*6)
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.-

import time

distancia = float(input('Qual é a distância da sua  viagem? '))
print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
#preço = distância * 0.50 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    preço = distancia * 0.50
    print('calculando valor...')
    time.sleep(0.5)
    print('O valor da passagem será de R$ {:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('calculando valor...')
    time.sleep(0.5)
    print('O valor da passagem será de R$ {:.2f }'.format(preço))

