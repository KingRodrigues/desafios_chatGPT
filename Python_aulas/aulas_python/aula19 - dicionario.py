#pessoas = {
#    'nome': 'King',
#    'sexo': 'M',
#    'idade': 22
#}

#print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.') # O King tem 22 anos.
#print(pessoas.keys()) # dict_keys(['nome', 'sexo', 'idade'])
#print(pessoas.values()) # dict_values(['King', 'M', 22])
#print(pessoas.items()) # dict_items([('nome', 'King'), ('sexo', 'M'), ('idade', 22)])

#del pessoas['sexo] # apaga o elemento 'sexo
#pessoas['nome'] = 'Leandro' # altera o nome do elemento
#pessoas['peso'] = 98.5 # adiciona peso

#for k, v in pessoas.items():
#    print(f'{k} = {v}')

#brasil = []
#estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
#estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)

#print(brasil[0]['uf'])

# ------------------------------------------------------------------------------------------------------------

estado = dict() # dicionario
brasil = list() # lista

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) # faz uma cópia [dicionario]
print(brasil)
for e in brasil: # lista
    for k, v in e.items(): # dicionario
        print(f'O campo {k} tem valor {v}.')
        