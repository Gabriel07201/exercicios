from time import sleep


def contador():
    print('-=' * 25)
    print('Contador de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')
    print('-=' * 25)
    print('Contador de 10 até 0 de 2 em 2')
    for z in range(10, -1, -2):
        print(z, end=' ')
        sleep(0.5)
    print('FIM')
    print('-=' * 25)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    if f > 0:
        f = f + 1
    elif f < 0:
        f = f - 1
    p = int(input('Passo: '))
    if f < i and p > 0:
        p = -p
    for x in range(i, f, p):
        print(x, end=' ')
        sleep(0.5)
    print('FIM')


contador()
