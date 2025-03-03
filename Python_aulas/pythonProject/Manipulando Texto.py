frase = 'Curso em Video Python'
#• Fatiamento
print(frase[9]) #Pegará o 'V'
print(frase[9:13]) #Começa no 'V'[9] e vai até o 'E', ignorando o 'O'[13]
print(frase[9:21:2]) #Começa no 'V'[9], Vai até o 'E'[20], pulando [2] em 2
print(frase[:5]) #Quando se não adiciona o inicio, ele começará [0] até o [5]
print(frase[15:]) #Não indicando o final, ele começa no [15] e vai até o final [20]
print(frase[9::3]) #Começa no 'V'[9], indo até o final, pulando de [3] em 3

#• Análise

#len('') [comprimento]
print(len(frase))

#count('') [contar]
print(frase.count('o', 0, 13)) #count('', [], []) Inicio, Final

#find('') [encontrar]
print(frase.find('deo')) #Dirá a onde começou [11]

print(frase.find('Android')) #Retornará -1, indicando não encontrado
print('Curso' in frase) #Existe "Curso" EM frase? Sim, TRUE

#• Transformação

#replace('') [substituir]
print(frase.replace('Python', 'Android')) #Trocará 'Pythor' por 'Android'

#Para alterar a string, se deve informar que a "frase = "

print(frase.upper()) #Deixar tudo maiuscula
print(frase.lower()) #Deixar tudo minuscula

print(frase.capitalize()) #Pegar str, deixar tudo minuscula, e deixar a primeira maiscula

print(frase.title()) #Colocar cada primeira palavra maiscula


frase2 = '      Aprenda Python   '
print(frase2)

#strip() [remover espaços inúteis]
print(frase2.strip())

#rstrip() [remove espaços da direita]
print(frase2.rstrip())

#lstrip() [remove espaços da direita]
print(frase2.lstrip())


#• Divisão

#split() [Criar divisão a onde possui espaços]
print(frase.split())

#• Junção

#''.join(variavel) [Juntar com a variavel]
print('-'.join(frase))
