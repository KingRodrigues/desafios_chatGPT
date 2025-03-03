# crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# no final, mostre:
# a) quantas pessoas foram cadastradas
# b) a média de idade do grupo
# c) uma lista com todas as mulheres
# d) uma lista com todas as pessoas com idade acima da média

galera = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']

    galera.append(pessoa.copy()) # adiciona uma cópia do dicionário na lista

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if resp == 'N':
        break
media = soma / len(galera)

# exibição dos resultados
print('-=' * 30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('       ')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('<<ENCERRADO>>')
