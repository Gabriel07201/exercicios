import random
import time
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pedra = 0
papel = 1
tesoura = 2
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO'), time.sleep(0.5)
print('KEN'), time.sleep(0.5)
print('PO!!!'), time.sleep(1)
computador = random.randint(0, 2)
if jogador > 3 or jogador < 0:
    print('Escolha inválida tente novamente')
    exit()
print('-=' * 20)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*20)
if computador == jogador:
    print('EMPATE')
elif computador == 0 and jogador == 1:
    print('JOGADOR VENCE')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCE')
elif computador == 1 and jogador == 2:
    print('JOGADOR VENCE')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCE')
elif computador == 2 and jogador == 0:
    print('JOGADOR VENCE')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENCE')
