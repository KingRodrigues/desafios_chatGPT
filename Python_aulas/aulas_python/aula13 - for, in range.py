#laço c no intervalo(1, 10):  | for c in range(1, 10):
#   se $                      |     if $:
#       pega                  |         pega
#   passo                     |     passo 
#   pula                      |     pula
#passo                        | passo
#pega                         | pega

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Pula: '))

for c in range(i, f+1, p):
    print(c)
print('FIM!')