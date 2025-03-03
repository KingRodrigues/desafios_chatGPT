print('='*6, 'DESAFIO 048', '='*6)
# faça um programa que calcule a soma entre todos os números impares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0 # acumulador
cont = 0 # contador

for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 # um contador conta +1
        soma = soma + c # um acumulador soma o valor
print(f'A soma de todos os valores solicitados é {soma}\nO número de valores é de {cont}')
