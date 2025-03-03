# faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# no final, mostre o conteúdo da estrutura na tela.

#status = dict()

#status['nome'] = str(input('Nome: '))
#status['media'] = float(input(f'Média de {status["nome"]}: '))

#print(f'O Nome é igual a {status["nome"]}')
#print(f'A Média é igual a {status["media"]}')

#if status['media'] >= 5.1:
#    print(f'Situação é igual a Aprovado!')
#else:
#    print('Situação é igual a Reprovado!')





aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno ['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
