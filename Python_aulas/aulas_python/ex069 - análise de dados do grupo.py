print('='*6, 'DESAFIO 069', '='*6)
# crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada, o programa deverá
# perguntar se o usuário quer ou não continuar. No final, mostre:
# a) quantas pessoas tem mais de 18 anos.
# b) quantos homens foram cadastrados.
# c) quantas mulheres tem menos de 20 anos.

cont = homem = mulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF': # enquanto não digitar MF, vai forçar a pergunta
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]

    if idade > 18:
        cont += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {cont}')
print(f'Total de Homens: {homem}')
print(f'Mulheres com menos de 20 anos: {mulher}')
    