# escreva um script que leia um arquivo de texto e conte quantes vezes cada palavra aparece.

escreva = str(input('Digite um texto: '))
palavras = escreva.split()
print('O texto digitado tem um total de {} palavras.'.format(len(palavras))) # len(palavras) retorna o número total de itens na lista palavras, ou seja, a contagem de palavras.
