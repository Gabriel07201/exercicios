from random import randint
from time import sleep


def valores(lista):
    print('Valores sorteados da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 100)
        print(n, end=' ')
        sleep(0.5)
        lista.append(n)
    print('FIM')
    return lista


numeros = list()
valores(numeros)


def soma_pares(lista):
    pares = 0
    for c in lista:
        if c % 2 == 0:
            pares += c
    print(f'Somando os valores pares de {lista}, temos {pares}')


soma_pares(numeros)
