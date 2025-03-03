nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))

# :20 == Até 20 caracteres
# :< == alinhado a esquerda
# :^ == centralizado
# :=^20 == Centralizado, em até 20 caracteres dentro de =

#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A Soma vale {}'.format(n1+n2))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
# :.3f formatar a divisão com 3 casas decimais
# para não quebrar uma linha para outra == , end=''
# \n == quebra de linha

print('Divisão inteira {} e potência {}'.format(di, e))
