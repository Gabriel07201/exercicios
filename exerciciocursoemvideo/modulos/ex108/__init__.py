def aumentar(p):
    return p * 1.1


def diminuir(p):
    return p * 0.90


def dobro(p):
    return p * 2


def metade(p):
    return p / 2


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
