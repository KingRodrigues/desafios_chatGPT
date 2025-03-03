# CRIANDO UM CHAT DE MENSAGENS

# "import os" = Usada para interagir com o sistema operacional
# 1. 'os.getcwd()': Obtém o diretório de trabalho atual
# 2. 'os.listdir(path)': Lista os arquivos e diretórios em um caminho específico.
# 3. 'os.path.join(path, *paths)': Combina partes de caminhos para formar um novo caminho.
# 4. 'os.path.exists(path)': Verifica se um caminho existe.
# 5. 'os.mkdir(path)': Cria um novo diretório.
# 6. 'os.remove(path)': Remove um arquivo
# 7. 'os.rename(src, dst)': Renomeia um arquivo ou diretório.
# 8. 'os.environ': Dicionário com variáveis de ambiente do sistema.
# 9. 'os.system(command)': Executa um comando do sistema.
# 10. 'os.chdir(path)': Altera o diretório de trabalho

import os

mensagens = [] #lista para mensagens

nome = input('Nome: ') #Nome do usuário

while True: #Loop infinito

    # limpando terminal
    os.system('cls')

    if len(mensagens) > 0: #Faz uma verificação se a lista for maior que 0
        for m in mensagens: #percorre a lista de mensagens
            print(m['nome'], '-', m['texto']) #Faz um print do nome - texto

    print('__________________________')

    # obtendo texto
    texto = input('mensagem: ') # local onde usuário irá digitar
    if texto == 'fim': # faz uma verificação
        break # quebra o loop

    # adiciona mensagem na lista
    mensagens.append({ # adiciona a mensagem, chama a lista mensagens e adiciona um append com nome e texto.
        'nome': nome,
        'texto': texto
    })