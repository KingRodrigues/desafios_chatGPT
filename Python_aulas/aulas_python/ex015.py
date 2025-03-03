print('='*6,'DESAFIO 015','='*6)
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.

kp = float(input('Quilometragem percorrida: '))
da = int(input('Dias alugados: '))
aluguel = (60 * da) + (0.15 * kp)
print('Valor do Aluguel: R$ {:.2f}'.format(da*60))
print('Valor por km: R$ {:.2f}'.format(kp * 0.15))
print('Valor total a ser pago: R$ {:.2f}'.format(aluguel))
