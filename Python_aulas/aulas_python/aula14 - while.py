# enquanto não apple
#   se chão
#       passo
#   se buraco
#       pula
#   se moeda
#       pega
# pega

# while not apple:
#   if chão:
#       passo
#   if buraco:
#       pula
#   if moeda:
#       pega:
# pega

# --------------------------------------------------

# for c in range(1, 10):
#    print(c)
# print('Fim!')

# c = 1
# while c < 10:
#    print(c)
#    c += 1
# print('Fim')

# --------------------------------------------------

# r = 's'
# while r == 's':
#    n = int(input('Digite um valor: ')).lower()
#    r = str(input('Quer continuar? [s/n]: '))
# print('Fim')

# --------------------------------------------------

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
