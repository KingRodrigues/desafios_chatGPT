# faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# no final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.

listanum = []
mai = men = 0

for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: '))) # adicionar a lista
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai}')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}....')
print(f'O menor valor digitado foi {men}')
for i, v in enumerate(listanum):
                      if v == men:
                        print(f'{i}...')
print()
