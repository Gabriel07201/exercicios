def aumentar(p, taxa, format=False):
    res = p * (1 + (taxa / 100))
    return res if format is False else moeda(res)


def diminuir(p, taxa, format=False):
    res = p * (1 - (taxa / 100))
    return res if format is False else moeda(res)


def dobro(p, format=False):
    res = p * 2
    return res if format is False else moeda(res)


def metade(p, format=False):
    res = p / 2
    return res if format is False else moeda(res)


def moeda(p=0, moeda='R$'):
    return f'{moeda}{p:.2f}'.replace('.', ',')


def resumo(p, taxaa, taxad):
    print('-'*20)
    print('RESUMO DO VALOR'.center(20))
    print('-'*20)
    print(f'Preço analisado: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(p, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(p, taxad, True)}')
