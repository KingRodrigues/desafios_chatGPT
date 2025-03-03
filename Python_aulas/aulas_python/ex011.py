print('====== DESAFIO 011 ======')
#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

a = float(input('Qual a altura da parede? '))
l = float(input('Qual a largura da parede? '))
at = a * l
t = 2
g = at / t
print('Quantidade de tinta necessária: {:.1f}'.format(g))
