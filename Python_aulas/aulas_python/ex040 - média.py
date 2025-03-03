print('='*6, 'DESAFIO 040', '='*6)
#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final
#de acordo com a média atingida
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado"
print('')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if (m < 5.0):
    print('Média: {:.2f} | status: reprovado!'.format(m))
elif (m > 7.0):
    print('Média: {:.2f} | Status: Aprovado!'.format(m))
else:
    print('Média: {:.2f} | Status: Recuperação!'.format(m))
