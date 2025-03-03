nome = str(input('Qual é o seu nome? '))
print('Tenha um bom dia {}.'.format(nome))
if nome == 'King':
    print('Bown Down to the King!')
elif nome == 'Queen' or nome == 'Jack':
    print('Run!')
elif nome in 'Ana Cláduia Jéssica Juliana':
    print('Belo nome')
else:
    print('Bem nornaml, hein?')
