print('='*6, 'DESAFIO 044', '='*6)
#Elabore um programa que calcule o valor a ser pago por um, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 50% de desconto
# - Em até 2x no cartão: Preço normal
# - 3x ou mais no cartão: 20% de juros.
print('')

valor = float(input('Qual o valor a ser pago? R$ '))
adc = valor - (valor * 10 / 100)
ac = valor - (valor / 2)
c3x = valor + (valor * 20 / 100)
print('À vista - Dinheiro/Chegue: R$ {}'.format(adc))
print('À vista - Cartão: R$ {}'.format(ac))
print('2x - Cartão: R$ {}'.format(valor))
print('3x a 12x - Cartão: R$ {}'.format(c3x))
