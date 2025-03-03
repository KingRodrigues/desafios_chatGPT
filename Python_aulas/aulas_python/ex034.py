print('='*6, 'DESAFIO 034', '='*6)
#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, um aumento é de 15%.

salario = float(input('Qual o salário do funcionário? R$'))
if salario <= 1250.00:
    aumento = salario + (salario * 15 / 100)
    print('Reajuste: 15% | Novo Valor: R${:.2f}'.format(aumento))
else:
    aumento = salario + (salario * 10 / 100)
    print('Reajuste: 10% | Novo Valor: R${:.2f}'.format(aumento))
