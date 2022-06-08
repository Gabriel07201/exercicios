# criar um jogo de advinhação
import random
from time import sleep

print('-=-' * 30)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 30)
al = random.randint(0, 5)
nu = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
sleep(3)
if al == nu:
    print(f'PARABÉNS! Eu pensei no número {al} e você acertou!')
else:
    print(f'GANHEI!Eu pensei no número {al} e não no {nu}!')
