#                   LAÇOS DE REPETIÇÕES - while
# break ~~ pare
# !=  ~~ flag de parada

from time import sleep

c = 0

while c != 6: # flag
    print(f'{c}')
    sleep(1)
    c += 1
print('FIM!')
print('~'*6)

while c >= 0:
    print(f'0{c}')
    sleep(1)
    c -= 1
print('FIM!')
print('~'*6)

while True:
    print(c)
    sleep(1)
    c += 1
    if c == 6:
        print(c)
        break
