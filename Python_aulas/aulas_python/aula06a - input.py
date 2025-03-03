name = input('Olá! Muito prazer! Qual é o seu nome? ')
n1 = int(input('Muito prazer, {}! Agora, digite um número: '.format(name)))
n2 = int(input('Agora escolha outro número para ser somado: '))
s = n1 + n2
print('A soma entre os números {} e {} é {}'.format(n1, n2, s))
