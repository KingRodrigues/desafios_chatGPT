print('='*6, 'DESAFIO 042', '='*6)
#Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes
print('')

print('-='*20)
print('Analisador de Triângulo')
print('-='*20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triângulo!')
    print('')
    print('Tipo de triângulo que será formado:')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')

else:
    print('Os segmentos acima não podem format triângulo!')