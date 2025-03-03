print('='*6, 'DESAFIO 057', '='*6)
# faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

# s = 1
# while s != 'F' or s != 'M':
#    s = str(input('Qual o seu sexo? ')).upper()[0].strip()
#    if s == 'F' or s == 'M':
#        print('Registro Concluido!')
#        break
#    else:
#        print('Opção inválida!\nTente novamente.')


sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
