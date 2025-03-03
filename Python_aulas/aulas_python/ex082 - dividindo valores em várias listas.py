# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares
# e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

valores = []
vp = []
vi = []

while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        vp.append(n)
    elif n % 2 == 1:
        vi.append(n)
    resp = str(input('Quer continuar? [s/n]: '))
    if resp in 'Nn':
        break
    
print(f'Lista de Valores: {valores}')
print(f'Lista de Nº Pares: {vp}')
print(f'Lista de Nº Ímpares: {vi}')



# --------------------------------------------------------

# MODO GUANABARA

num = list()
pares = list()
impares = list()

while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [s/n]: '))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)

print(f'Lista de Valores: {num}')
print(f'Lista de Nº Pares: {pares}')
print(f'Lista de Nº Ímpares: {impares}') 
       