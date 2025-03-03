# crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
# boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()

while True:
    nome = str(input('Nome: ')) 
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]) # lista composta

    cont = str(input('Deseja continuar? [s/n]: '))
    if cont in 'Nn':
        break
print('-=' * 30)

print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha): # indice, aluno
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True: #flag pra parar
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999: # stop
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1: # se digitar um número que tenha na lista
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}') # opc é o número do aluno, 0 é nome dele dele, 1 são as notas
    else:
        print(f'Aluno não encontrado! Números disponíveis: 0 a {len(ficha)-1}')
print('<<< VOLTE SEMPRE >>>')