dicio = {}
gols = list()
dicio['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dicio["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c}? ')))
dicio['gols'] = gols
dicio['total'] = sum(gols)
print('-='*20)
print(dicio)
print('-='*20)
for k, v in dicio.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*20)
print(f'O jogador {dicio["nome"]} jogou {partidas} partidas.')
for c, n in enumerate(gols):
    print(f'   => Na partida {c}, fez {n} gols.')
print(f'Foi um total de {dicio["total"]}')
