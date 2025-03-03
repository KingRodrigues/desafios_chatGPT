print('='*6, 'DESAFIO 046', '='*6)
# faça um programa que mostre na tela uma contagem regressiva para
# o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print('Contagem Regressiva')
print('Contagem de 10s para a queima dos fogos!')

for tempo in range(10, -1, -1):
    print(tempo)
    sleep(1)
sleep(0.5)
print('*Queima de Fogos*')
