def aumentar(p, format=False):
    res = p * 1.1
    return res if format is False else moeda(p)


def diminuir(p, format=False):
    res = p * 0.9
    return res if format is False else moeda(p)


def dobro(p, format=False):
    res = p * 2
    return res if format is False else moeda(p)


def metade(p, format=False):
    res = p / 2
    return res if format is False else moeda(p)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')
