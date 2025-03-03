# crie um programa que recebe uma frase e verifica se é um palíndromo, ignorando espaços e pontuação.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Portanto, ele é um palindromo!')
else:
    print('Portando, ele não é um palindromo!')
