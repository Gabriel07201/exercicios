from time import sleep
from random import randint
jogo = {'jogador1': randint(0, 10), 'jogador2': randint(0, 10), 'jogador3': randint(0, 10), 'jogador4': randint(0, 10)}
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-='*20)
print('== RANKING DOS JOGADORES ==')
for i in sorted(jogo, key= jogo.get, reverse=True):
    print(f'{i} com {jogo[i]}')
    sleep(1)
