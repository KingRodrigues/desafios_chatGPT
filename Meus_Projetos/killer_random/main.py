kill = morte = assistencia = 0

mapas = []

while True:
    # dicionário para armazenar os dados do mapa
    mapa = {}
    mapa['nome'] = input('Nome do Mapa: ')

    # lista para armazenar os agentes do mapa
    mapa['agentes'] = []

    while True:
        # dicionário para armazenar as informações do agente
        agente = {}
        agente['nome'] = input('Nome do Agente: ')
        agente['vitórias'] = int(input('Número de Vitórias: '))
        agente['derrotas'] = int(input('Número de Derrotas: '))
        agente['abates'] = int(input('Número de Abates: '))
        agente['mortes'] = int(input('Número de Mortes: '))
        agente['assistências'] = int(input('Número de Assistências: '))

        # adiciona agente a lista de agentes do mapa
        mapa['agentes'].append(agente)

        # continue
        continuar = input('Adicionar outro agente a este mapa? [S/N]: ').strip().upper()
        if continuar == 'N':
            break

    # adiciona o mapa a lista de mapas
    mapas.append(mapa)

    # adicionar outro mapa
    continuar = input('Adicionar outro mapa? [S/N]: ').strip().upper()
    if continuar == 'N':
        break

# exibe os dados coletados
print('-=' * 20)
for mapa in mapas:
    print(f'    Mapa: {mapa["nome"]}')
    for agente in mapa['agentes']:
        print(f'    Agente: {agente["nome"]}')
        print(f'    Vitórias: {agente["vitórias"]}')
        print(f'    Derrotas: {agente["derrotas"]}')
        print(f'    Abates: {agente["abates"]}')
        print(f'    Mortes: {agente["mortes"]}')
        print(f'    Assistências: {agente["assistências"]}')
        print(f'    Winrate: {agente["winrate"]}')
    print('-=' * 20)
