lista = []
dicio = {}
gols = []
while True:
    dicio.clear()
    dicio['nome'] = str(input('Nome do jogador: '))
    dicio['partidas'] = int(input('Quantas partidas o jogador jogou? '))
    for c in range(0, dicio['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))
    dicio['gols'] = gols[:]
    dicio['total'] = sum(dicio['gols'])
    gols.clear()
    lista.append(dicio.copy())
    cont = str(input('Quer continuar? [S/N]')).strip().upper()
    while cont not in 'SN':
        print('Opção inválida. Responda apenas S ou N.')
        cont = str(input('Quer continuar? [S/N]')).strip().upper()
    if cont == 'N':
        break
print('-='*30)
print(f'{"cod":<4}{"nome":<15}{"gols":<25}{"total":<20}')
print('-'*60)
for c, n in enumerate(lista):
    print(f'{c:<4}{lista[c]["nome"]:>10}  {lista[c]["gols"]}{lista[c]["total"]:>15}')
while True:
    jogador = int(input('Mostrar os dados de qual jogador? (999 para parar): '))
    if jogador == 999:
        break
    if jogador >= len(lista):
        print(f'ERRO! Não existe jogador com código {jogador}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[jogador]["nome"]}:')
        for a, b in enumerate(lista[jogador]['gols']):
            print(f'No jogo {a+1} fez {b} gols')
