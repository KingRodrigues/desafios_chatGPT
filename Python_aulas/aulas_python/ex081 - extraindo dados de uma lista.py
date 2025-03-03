# crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# a) Quantos números foram digitados.
# b) A lista de valores ordenada de forma decrescente.
# c) se o valor 5 foi digitado e está ou não na lista.


lista = []
cont = 0

while True:
    num = int(input('Digite um número: '))
    if num != 00:
        lista.append(num)
        cont += 1
    else:
        print('Encerrando...')
        break

print(f'Foram digitados {cont} números;')
lista.sort(reverse=True)
print(f'Lista de valores: {lista};')
if 5 in lista:
    print('Existe o valor 5 na lista!')
if 5 not in lista:
    print('Não existe o valor 5 na lista!')

# ----------------------------------------------------

# MODO GUANABARA

valores = []

while True:
    valores.append(int('Digite um valor: '))
    resp = str(input('Quer continuar? [s/n]: '))
    if resp in 'Nn':
        break

print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
