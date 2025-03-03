print('='*6,'DESAFIO 019','='*6)
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajuda ele, lendo o nome delas e escrevendo o nome do escolhido.

#Importar randomizador de elementos
import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
#criar lista a ser sorteada
lista = [a1, a2, a3, a4]
#Uma escolha dentro da lista
escolha = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolha))
