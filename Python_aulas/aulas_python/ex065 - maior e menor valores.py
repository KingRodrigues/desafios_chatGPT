print('='*6, 'DESAFIO 065', '='*6)
# crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

valores = contador = maior = menor = 0

while True:
    numero_inteiro = int(input('Digite um Número Inteiro: '))
    valores += numero_inteiro
    contador += 1
    if contador == 1:
        maior = numero_inteiro
        menor = numero_inteiro
    else:
        if numero_inteiro > maior:
            maior = numero_inteiro
        if numero_inteiro < menor:
            menor = numero_inteiro

    print('~'*15)
    repetir = str(input('Deseja adicionar um novo valor? [s/n]: ')).lower()
    print('~'*15)
    if repetir != 's':
        break

print(f"""
    Quant. Número: {contador}
    Média: {valores / contador}
    Maior Nº: {maior}
    Menor Nº: {menor}
      """)


"""

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm

    resp = str(input('Quer continuar? [s/n]: )).upper().strip()[0]
média = soma / quant
print(f'Você digitou {quant} números e a média foi {média}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

"""