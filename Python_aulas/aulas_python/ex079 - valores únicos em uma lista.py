# crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista.
# caso o número já exista lá dentro, ele não será adicionado.
# no final, serão exibidos todos os valores únicos digitados, em ordem crescente.

números = list() # lista vazia
while True: # loop infinito
    n = int(input('Digite um valor: '))
    if n not in números: # se o n não tiver em numeros
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [s/n]: '))
    if r in 'Nn':
        break

números.sort() # coloca números em ordem
print(f'Você digitou os valores {números}')
