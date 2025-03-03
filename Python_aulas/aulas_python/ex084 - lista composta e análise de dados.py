# faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# a) quantas pessoas foram cadastradas.
# b) uma listagem com as pessoas mais pesadas.
# c) uma listagem com as pessoas mais leves.

temp = [] # cria lista temporária
princ = [] # cria lista principal
mai = men = 0

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))

    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]

    princ.append(temp[:]) # cria uma cópia
    temp.clear()

    resp = str(input('Quer continuar? [s/n]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.') # cria um contador
print(f'O maior peso foi de {mai}Kg. Peso de ', end='')
for p in princ: # pra cada pessoa em principal
    if p[1] == mai:
        print(f'{p[0]} ', end='') 
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for p in princ:
    if p[1] == men:
        print(f'{p[0]} ', end='')
print()
