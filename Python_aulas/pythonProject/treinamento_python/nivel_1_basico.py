# solicite um número ao usuário e determine se ele é par ou ímpar.
while True:
    print('Escolha uma opção:\n1. Par ou Ímpar\n2. Maior Número\n3. Calculadora Simples\n4. Tabuada.\n5. Fatorial\n0. Sair')
    esc = int(input('Qual opção você deseja escolher? '))
    n1 =n2 = 0

    if esc == 1:
        n1 = int(input('Digite um número: '))
        if n1 % 2 == 0:
            print('Esse número é Par!')
        else:
            print('Esse número é Ímpar!')
    
        print('=-'*10)

    elif esc == 2:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))

        if n1 > n2:
            print(f'{n1} é o número maior!')
        elif n2 > n1:
            print(f'{n2} é o número maior!')
        else:
            print('Os números são iguais!')
    
        print('=-'*10)

    elif esc == 3:
        n1 = int(input('Digite um primeiro número: '))
        n2 = int(input('Digite outro número: '))
        m = str(input('Escolha [ * | + | - ]: '))
        if m == '*':
            print(f'{n1} x {n2} = {n1*n2}')
        elif m == '+':
            print(f'{n1} + {n2} = {n1+n2}')
        elif m == '-':
            print(f'{n1} - {n2} = {n1-n2}')
        else:
            print('Opção Inválida!')
        print('=-'*10)

    elif esc == 4:
        n1 = int(input('Escolha um número para ver sua tabuada: '))
        c = 1

        while c <= 10:
            print(f'{n1} x {c} = {n1*c}')
            c += 1
        print('=-'*10)

    elif esc == 5:
        from math import factorial
    
        n1 = int(input('Digite um número para ver o seu favorial: '))
        f = factorial(n1)
        print(f'O fatorial de {n1} é {f}')
        print('=-'*10)


    elif esc == 0:
        print('O programa fechará em breve!')
        break

    else:
        print('Opção Inválida!')

print('O programa será encerrado!')
