# crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# no final, mostre a matriz na tela, com a formatação correta.
"""
ddm = []
valores = 0

for c in range(1, 10):
    valores = int(input(f'Digite o {c}º número da matriz: '))
    ddm.append(valores)
print(f"
      [ {ddm[0]} ] [ {ddm[1]} ] [ {ddm[2]} ]
      [ {ddm[3]} ] [ {ddm[4]} ] [ {ddm[5]} ]
      [ {ddm[6]} ] [ {ddm[7]} ] [ {ddm[8]} ]
      ")

"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f' [{matriz[l][c]:^5}]', end= '')
    print()
    