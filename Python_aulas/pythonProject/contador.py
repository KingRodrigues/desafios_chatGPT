import time

start = str(input('Vamos começar? [s/n]: ')).lower()
if start == 's':
    print('Vamos começar!')
    contador = 0
    while True:
        if contador != 10:
            contador = contador + 1
            print(contador)
            time.sleep(1)

            if contador == 10:
                print('Terminei de contar!')
                time.sleep(1)
                print('Tchau! Tchau!')
                time.sleep(1)
                break


#from time import *

#print('Vamos começar!')
#for contador in range(0, 11):
#    print(contador)
#    sleep(1)
#print('Terminei de contar!')
#sleep(1)
#print('Tchau! Tchau!')