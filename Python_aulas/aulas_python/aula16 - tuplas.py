# variáveis compostas (Tuplas) - ex:
# AS TUPLAS SÃO IMUTÁVEIS
#       variável composta, ou tupla, é uma variável que guarda vários valores.


# lanche (0 hamburguer, 1 suco, 2 pizza, 3 pudim)
# print(lanche[1:]) == Suco, pizza, pudim
# print(lanche[1::2])


# c = lanche
# for c in lanche:
#   print(c)


# variável simples - ex:
# lanche = 'hamburguer'
#       variável simples é uma variável a onde apenas se guarda um valor.


#--------------------------------------------------------------------------------------------

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') #() não é necessário

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')

for comida in lanche:
    print(f'Eu vou comer {'comida'}')
print('Comi pra caramba!')



print(lanche) # tupla
print(lanche[1]) # vai mostrar suco
print(lanche[2]) # pizza
print(lanche[3]) # pudim
print(lanche[-1]) # último item
print(lanche[-2]) # o penúltimo
print(lanche[1:3]) # os elementos [1] e [2]
print(lanche[2:]) # após o espaço 2
print(lanche[:2]) # vai mostrar os itens a seleção



a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.index(5, 1))

