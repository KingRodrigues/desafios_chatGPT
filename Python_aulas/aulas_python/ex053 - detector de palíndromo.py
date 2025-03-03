print('='*6, 'DESAFIO 053', '='*6)
# crie um programa que leia uma frase qualquer e diga se ela é um palíndromo.
# desconsiderando os espaços.

# ex: apos a sopa
# a sacada da casa
# a torre da derrota
# o lobo arma o bolo
# anotaram a data da maratona

frase = str(input('Digite uma frase: ')).strip().upper() # strip () tira espaços, upper() torna maisculas
palavras = frase.split() # separar a frase em palavras
junto = ''.join(palavras) # desconsidera espaços

# fatiamento
inverso = junto[::-1]
"""for letra in range(len(junto) - 1, -1): # pega o número de letras e faz o inverso
    inverso += junto[letra]"""

print(f'O inverso de {junto} é {inverso}')
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')



