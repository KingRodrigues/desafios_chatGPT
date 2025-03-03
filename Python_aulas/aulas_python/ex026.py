print('='*6, 'DESAFIO 026', '='*6)
#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input('Escreva uma frase: ').lower().replace(' ', '')
print('Quantas letras "A" possui? ', frase.count('a', 0)+1)
print('Em que posição ela aparece a primeira vez? ', frase.find('a', 0)+1)
print('Em que posição ela aparece a última vez? ', frase.rfind('a', 0)+1)
