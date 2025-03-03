print('='*6, 'DESAFIO 041', '='*6)
#A confederação nacional de natação precisa de um programa  que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: Mirim
#- Até 14 anos: Infântil
#- Até 19 anos: Junior
#- Até 20 anos: Sênior
#- Acima: Master.
print('')

from datetime import date 
ano = date.today().year

i = int(input('Qual o ano de nascimento? '))
if ano - i <= 9:
    print('Categoria: Mirim')
elif ano - i <= 14:
    print('Categoria: Infantil')
elif ano - i <= 19:
    print('Categoria: Junior')
elif ano - i <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')
