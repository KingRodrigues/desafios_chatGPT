# armazena informações que precisam de algum tipo de identificador
emails_gerentes = {
    'Iguatemi': 'iguatemi@gmail.com',
    'Plaza': 'plaza@gmail.com',
    'Barra': 'barra@gmail.com'
}

# se quiser descobrir qual o e-mail do shopping 'iguatemi'
email = emails_gerentes['Iguatemi']
print(email)

# se quiser adicionar um shopping novo
emails_gerentes['Leblon'] = 'leblon@gmail.com'
print(emails_gerentes)

# se quiser descobrir todos os shoppings
#   forma 1: fazer um for
for shopping in emails_gerentes:
    print(shopping)
# forma 2: dicionario.keys()
print(emails_gerentes.keys())

# se quiser todos os valores/emails
#    forma 1
for shopping in emails_gerentes:
    email = emails_gerentes['Iguatemi']
#   forma 2
print(emails_gerentes.values())

# retirar um shopping
emails_gerentes.pop('Leblon')
print(emails_gerentes)

# verificar se um shopping existe
if 'Leblon' in emails_gerentes:
    print('Existe')
else:
    print('Não existe')
