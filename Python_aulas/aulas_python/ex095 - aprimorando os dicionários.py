# aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()  # Lista que armazenará os dados de todos os jogadores
jogador = dict()  # Dicionário que armazenará os dados de um único jogador
partidas = list()  # Lista que armazenará a quantidade de gols em cada partida

while True:
    jogador.clear()  # Limpa os dados do jogador para evitar sobreposição ao adicionar um novo
    jogador['nome'] = str(input('Nome do Jogador: '))  # Solicita o nome do jogador
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))  # Pergunta quantas partidas ele jogou
    partidas.clear()  # Limpa a lista de partidas para armazenar os novos dados

    for c in range(0, tot):  # Loop que coleta a quantidade de gols em cada partida
        partidas.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    
    jogador['gols'] = partidas[:]  # Armazena a lista de gols dentro do dicionário do jogador (cópia da lista)
    jogador['total'] = sum(partidas)  # Calcula e armazena o total de gols feitos pelo jogador
    time.append(jogador.copy())  # Adiciona uma cópia do dicionário `jogador` na lista `time`
    
    while True:  # Loop para validar a resposta do usuário
        resp = str(input('Quer continuar? [s/n]: ')).upper()[0]  # Pergunta se deseja continuar
        if resp in 'SN':  # Verifica se a resposta é válida (S ou N)
            break
        print('ERRO! Responda apenas S ou N.')  # Mensagem de erro caso a resposta seja inválida

    if resp == 'N':  # Se a resposta for 'N', encerra o loop principal
        break

print('-=' * 30)  # Linha de separação para organização visual

# Exibição do cabeçalho da tabela de jogadores cadastrados
print('cod ', end='')  # "cod" representa o código identificador do jogador
for i in jogador.keys():  # Percorre as chaves do dicionário (nome, gols, total)
    print(f'{i:<15}', end='')  # Imprime os títulos alinhados à esquerda
print()

print('-' * 40)  # Linha divisória
for k, v in enumerate(time):  # Percorre a lista `time`, enumerando os jogadores
    print(f'{k:>3} ', end='')  # Exibe o código do jogador (índice da lista)
    for d in v.values():  # Percorre os valores do dicionário (dados do jogador)
        print(f'{str(d):<15}', end='')  # Exibe os valores alinhados
    print()  # Quebra de linha para o próximo jogador
print('-' * 40)  # Linha divisória

while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar): '))  # Pergunta qual jogador mostrar
    if busca == 999:  # Se o usuário digitar 999, encerra a consulta
        break
    if busca >= len(time):  # Verifica se o código informado existe na lista
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')  # Exibe o nome do jogador selecionado
        for i, g in enumerate(time[busca]['gols']):  # Percorre a lista de gols do jogador
            print(f'     No jogo {i+1} fez {g} gols.')  # Mostra os gols por partida
        print('-' * 40)  # Linha divisória para organização visual

print('<< VOLTE SEMPRE! >>')  # Mensagem de encerramento do programa

