from time import sleep
from random import randint
sorteio = []
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, pergunta):
    sorteio.clear()
    sleep(0.5)
    cont = 0
    while cont < 6:
        valores = randint(1, 60)
        if valores in sorteio:
            valores = randint(1, 60)
        else:
            sorteio.append(valores)
            cont += 1
    print(f'Jogo {c+1}: {sorteio}')

