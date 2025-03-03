# crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar')

for p in palavras: # analisa cada elemento da tupla
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p: # analisa cada letra 
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
