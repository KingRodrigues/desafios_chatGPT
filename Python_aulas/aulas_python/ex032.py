rint('='*6, 'DESAFIO 032', '='*6)
#Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.


from datetime import date

ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year #Pegar ano atual do pc

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))

