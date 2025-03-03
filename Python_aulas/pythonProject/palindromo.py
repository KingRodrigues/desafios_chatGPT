while True:
    frase = str(input('Digite uma frase: ')).strip().upper() # strip remove espaços, upper deixa maisculas

    palavras = frase.split() # divide a frase em palavras
    junto = ''.join(palavras) # junta as palavras em uma só

    inverso = junto[::-1] # inverte a ordem da escrita

    if inverso == junto:
        print(f'O inverso de {junto} é {inverso}...\nPortanto, ele é um palíndromo!')
    else:
        print(f'O inverso de {junto} é {inverso}...\nPortanto, não é um palíndromo!')

    r = str(input('Deseja tentar novamente? [s/n]: ')).lower()
    if r != 's':
        break
