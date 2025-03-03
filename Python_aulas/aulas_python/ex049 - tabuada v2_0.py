print('='*6, 'DESAFIO', '='*6)
# refaça o Desafio 009, mostrando a tabuada de um número que o usuário
# escolher, só que agora utilizando um laço for.

# tabuada = 0

# n = int(input('Escolha um número para ver sua tabuada: '))
# for t in range(1, 11):
#    tabuada = tabuada + 1
#    r = n * tabuada
#    print(f'{n} x {tabuada} = {r}')


n = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = {n*1}')
    