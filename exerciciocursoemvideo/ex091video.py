from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(0, 10), 'jogador2': randint(0, 10), 'jogador3': randint(0, 10), 'jogador4': randint(0, 10)}
ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key= itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
