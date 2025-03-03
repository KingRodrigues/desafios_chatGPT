print('='*6,'DESAFIO 020','='*6)
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quadro alunos e mostra a ordem sorteada.

import random
a1 = str(input('Primeiro nome: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro nome: '))
a4 = str(input('Quarto nome: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem será: {}'.format(lista))
