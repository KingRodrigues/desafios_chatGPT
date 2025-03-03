# crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#  a) Apenas os 5 primeiros colocados.
#  b) Os últimos 4 colocados da tabela.
#  c) Uma lista com os times em ordem alfabética.
#  d) Em que posição na tabela está o time da Chapecoense.

nba = ('Cavaliers', 'Celtics', 'Knicks', 'Magic', 'Bucks', 'Heat', 'Hawks', 'Pacers', 'Bulls', 'Nets', 'Pistons', '76ers', 'Hornets', 'Raptors', 'Wizards')

print(f'TOP 5 NBA:\n{nba[0:5]}') # escolhe os 5 primeiros da lista
print('')
print(f'4 últimos Colocados:\n{nba[-4:]}') # os 4 últimos
print('')
print(f'Lista em ordem alfabética:\n{sorted(nba)}') # lista em ordem alfabética
print('')
select = str(input('Escolha um time para saber sua posição: ')).capitalize()
print(f'O {select} está na {nba.index(select)+1} posição') # posição que está o time selecionado
print('')