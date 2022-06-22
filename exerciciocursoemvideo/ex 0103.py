def ficha_jogador(nome='', gols=''):
    if nome == '':
        nome = '< desconhecido >'
    if gols == '':
        gols = 0
    return print(f'O jogador {nome} fez {gols} gols(s) no campeonato.')


jogador = str(input('Nome do jogador: '))
gol = (input('Número de Gols: '))
if gol.isnumeric() == False:
    gol = ''
ficha_jogador(jogador, gol)
