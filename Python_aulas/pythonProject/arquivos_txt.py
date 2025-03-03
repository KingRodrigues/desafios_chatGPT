
# 'r' > usado somante para ler algo
valores = [850, 2230, 1500]

with open('save.txt', 'r') as arquivo:
    for valor in arquivo:
        print(valor)

# 'w' > usado somente para escrever algo
valores = [850, 2230, 1500]

with open('save.txt', 'w') as arquivo:
    for valor in valores:
        arquivo.write(str(valor) + '\n')

# 'r+' > usado para ler e escrever algo
valores = [850, 2230, 1500]

with open('save.txt', 'r+') as arquivo:
    for valor in arquivo:
        print(valor)
    arquivo.write('9000')

# 'a' > usado para acrescentar algo
valores = [850, 2230, 1500]

with open('save.txt', 'a') as arquivo:
    for valor in valores:
        arquivo.write(str(valor) + '\n')
