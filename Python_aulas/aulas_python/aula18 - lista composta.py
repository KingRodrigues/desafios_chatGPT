teste =  list() # cria lista
teste.append('Gustavo') # adiciona 'Gustavo' a lista
teste.append(40) # adiciona '40' a lista

galera = list() # cria lista
galera.append(teste) # cria uma lista dentro de outra lista, interligando os dois
teste[0] = 'Maria' # as duas listas terá 'Maria'
teste[1] = 22 # as duas listas terá '22'
galera.append(teste[:]) # faz uma cópia da lista 'teste'
print(galera)


galera = [['João, 19'], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(p[0]) # pra cada item, printa o nome [0] 


totmai = totmen = 0
galer = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galer.append(dado[:]) # faz uma cópia do dado
    dado.clear() # exclui a lista dado para não gerar lista vazia

for p in galer:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
