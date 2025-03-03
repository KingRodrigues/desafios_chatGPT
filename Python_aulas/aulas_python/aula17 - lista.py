# num = [2, 5, 9, 1] # lista
# num[2] = 3 # deixa de ser 2 e vira 3
# num.append(7) # adiciona valor 7
# num.sort() # coloca em ordem
# num.sort(reverse=True) # organiza de forma reversa
# num.insert(2, 0)
# num.pop() # elinima valor 1
# num.remove(2) # remove elemento 2
# num.pop(2)

# if 4 in num:
#    num.remove(5) # se tiver o numero 5, ele remove
# else:
#    print('Não achei o número 5')

# print(f'Essa lista tem {len(num)} elementos.') # quanta elementos
# print(num)

# ----------------------------------------------------------------------------

valores = [] # lista vazia

valores.append(5)
valores.append(9)
valores.append(4)

for v in valores: # pra cada v em valores
    print(f'{v}...', end='')

for c, v in enumerate(valores): # pega chave e valores
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# -----------------------------------------------------------------------------

valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

# ------------------------------------------------------------------------------

a = [2, 3, 4, 7]
b = a[:] # b recebe todas as strings de a
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
