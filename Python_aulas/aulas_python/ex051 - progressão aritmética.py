print('='*6, 'DESAFIO 051', '='*6)
# desenvolva um programa que leia o primeiro termo e a razão de um PA.
# No final, mostre os 10 primeiros termos dessa progressão.


print('='*6, '10 TERMOS DE UMA PA', '='*6)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + 10 * razao # calcular décimo termo
for pa in range(termo, decimo, razao):
    print(f'{pa}', end=' -> ')
print('Acabou!')