print('='*6, 'DESAFIO 023', '='*6)
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#Ex: Digite um número: 1834
#Unidade: 4 | Dezena: 3 | Centena: 8 | Milha: 1

while True:
    nt = input('Escolha um número de 0 a 9999: ')
    if nt.isnumeric() and 0 <= int(nt) <= 9999: #Verifica se é número e está no intervalo
        nt = nt.zfill(4) #Preenche com zeros à esquerda para garantir que tenha 4 dígitos
        print('Unidade: ', nt[3])
        print('Dezena: ', nt[2])
        print('Centena: ', nt[1])
        print('Milha: ', nt[0])

        repetir = input('Deseja continuar utilizando o programa? [s/n] '.lower())
        if repetir.lower() != 's':
            break
    else:
        print('Escolha um >> NÚMERO << de 0 a 9999!')
