print('='*6, 'DESAFIO 024', '='*6)
#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

while True:
    cd = input('Escreva o nome de uma cidade: ').lower().strip()
    if 'santo' in cd:
        print('Essa cidade possui "Santo" no nome!')
    else:
        print('Essa cidade não possui "Santo" no nome!')

    rp = input('Deseja tentar novamente? [s/n] ').lower()
    if rp.lower() != 's':
        break
