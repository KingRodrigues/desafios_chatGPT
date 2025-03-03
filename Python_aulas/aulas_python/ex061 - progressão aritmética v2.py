print('='*6, 'DESAFIO 061', '='*6)
# refaça o Desafio 051, lendo primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
c = 1 # começa no 1º termo

while c <= 10:
    print(f'{termo}', end=' -> ')
    termo += razao # atualiza o termo para o próximo na PA
    c += 1 # incrementa o contador para avançar ao próximo termo

print('Acabou!')

# ===================================================================

"""

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
c = 1

while c <= 10:
    if c < 10: # não é o último termo
        print(f'{termo}', end=' -> ')
    else: # último termo
        print(f'{termo}', end= ' -> acabou!')
    
    termo += razao # calcula o próximo termo
    c += 1 # incrementa o contador

"""
