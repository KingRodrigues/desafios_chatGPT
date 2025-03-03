print('====== DESAFIO 008 ======')
#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

md = float(input('Digite um valor em metros: '))
print('km = {}\nhm = {} \ndam = {} \nm = {} \ndm = {} \ncm = {} \nmm = {}.'.format((md / 1000),(md / 100),(md / 10),md,(md * 10),(md * 100),(md * 1000)))
