print('='*6, 'DESAFIO 039', '='*6)
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#- Se ele ainda vai se alistar ao serviço militar.
#- Se é a hora de se alistar.
#- Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
print('')

from datetime import *

data_hora_atual = datetime.now() #Obtendo a hora atual
data_formatada = data_hora_atual.strftime('%d-%m-%a')
hora_formatada = data_hora_atual.strftime('%H:%M:%S')
print('Horário atual: {}'.format(hora_formatada))
print('Data atual: {}'.format(data_formatada))
print('')
ano = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - ano

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento.'.format(saldo))
    an = atual + saldo
    print('Seu alistamento será em {}'.format(an))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    an = atual - saldo
    print('Seu alistamento foi em {}'.format(an))
